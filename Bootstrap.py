# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:34:51 2018

@author: Sandy
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
np.random.seed(100) 
pd.set_option('display.max_columns',10)
pd.set_option('display.width',None)
## Bootstrapping- Roadmap 
bvec = [-0.1,-0.2,0,0.1,0.2,0.25] #Beta
#bvec=[0.25]
T=250
nsim = 500
b0 = 1
boots=[10,25,50,100]
nboots=10
sig=0.5
mu_x=1
count=0
outp =np.zeros((len(bvec),len(boots),6))
outp.shape
for bdx,b1 in enumerate(bvec):      
    for btx,boot in enumerate(boots):
        #reject = 0
        reject_boot = 0
        reject_both = 0
        reject_orig=0
        for isim in range(nsim):
            count+=1
            e = np.random.normal(0,sig,size=(T,1))
            x = np.random.normal(mu_x,sig,size=(T,1))
            y=b0+(b1*x)+e
            x = sm.add_constant(x)
            model_orig=smf.OLS(y,x).fit()
            #if model_orig.pvalues[1]<0.05: reject+=1
            # Create confindence interval for b1
            ci=np.zeros(int(boot))
            for b in range(boot):
                # Create a resample index
                resamp=np.random.randint(T, size=int(0.5*T))#Re-sampling with replacement
                model = smf.OLS(y[resamp],x[resamp]).fit()
                ci[b] = model.params[1]
                #print(model.params[1])
            ci.sort()
            ci_lower = ci[int(boot*0.025)]
            ci_upper = ci[int(boot*0.975)]
            if not(0>=ci_lower and 0<=ci_upper): reject_boot+=1
            if not(0>=ci_lower and 0<=ci_upper) and model_orig.pvalues[1]<0.05: reject_both+=1
            if model_orig.pvalues[1]<0.05: reject_orig+=1
            #print(str(ci_lower),str(ci_upper))
            #print(str(count),'-',str(reject_orig),'-',str(reject_both),'-',str(reject_boot))
        outp[bdx,btx] = np.array((b1,boot,nsim,reject_orig,reject_boot,reject_both))

df=pd.DataFrame(np.vstack(outp))
df.columns=['Betas','Bootstraps','No_of_Simulation','Reject_Actual','Reject_Bootstrap','Reject_Both']
df['Actual Reject Rate']=(df['Reject_Actual']/df['No_of_Simulation'])*100
df['Bootstrap Reject Rate']=(df['Reject_Bootstrap']/df['No_of_Simulation'])*100
df['Power of the Test(when Beta=0, its Size of Test)']=(df['Reject_Both']/df['No_of_Simulation'])*100
