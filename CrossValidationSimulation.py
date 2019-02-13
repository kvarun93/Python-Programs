# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 01:40:48 2018

@author:Santhosh Shankar
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
np.random.seed(100)
## The code takes atleast a minute to run
### Change T and k values and run 1000 simulations under each group        
sig=0.5
mu_x=1
k=4
b0=1
b1=2
nsim = 1000
kvec = [2,4,8,10]
Tvec = [25,50,100,250]
outp =np.zeros((nsim,len(Tvec),len(kvec),5))
for tdx,T in enumerate(Tvec):
    bigT = T*2
    for kdx,k in enumerate(kvec):
        for isim in range(nsim):
            e = np.random.normal(0,sig,size=(bigT,1))
            x = np.random.normal(mu_x,sig,size=(bigT,1))
            x_t=x
            y=b0+(b1*x_t)+e
            x_t = sm.add_constant(x)
            sample = np.random.permutation(bigT)
            train = sample[:int(bigT/2)]
            test = sample[int(bigT/2):]
            ytr = y[train]
            xtr = x_t[train]
            model=smf.OLS(y[train],x_t[train]).fit()
            z=model.predict(x_t[test])
            mspe_true = ((y[test]-model.predict(x_t[test]))**2).mean()
            sample = np.random.permutation(T)
            mspe =np.zeros(k)
            for j in range(k):    
                train_l = sample[:int((k-1-j)*T/k)]
                train_u = sample[int((k-j)*T/k):]
                train = np.concatenate((train_l,train_u),0)
                test = sample[int((k-1-j)*T/k):int((k-j)*T/k)]
                model = smf.OLS(ytr[train],xtr[train]).fit()
                mspe[j] = ((ytr[test]-model.predict(xtr[test]))**2).mean()
            mspe_cv = mspe.mean()
            outp[isim,tdx,kdx] = np.array((T,k,mspe_true,mspe_cv,mspe_cv-mspe_true))

## Convert Array to DataFrame for analysis
df=pd.DataFrame(np.vstack(outp[:,:,:].mean(0)))
df.columns=['T','k','mspe_actual','mspe_crossvalid','difference']
df
## Comments: 
##         T     k  mspe_actual  mspe_crossvalid  difference
## 0    25.0   2.0     2.194780         2.124124   -0.070655
## 1    25.0   4.0     2.144915         1.965594   -0.179321
## 2    25.0   8.0     2.188232         1.606972   -0.581261
## 3    25.0  10.0     2.173658         1.425812   -0.747846
## 4    50.0   2.0     2.210486         2.193026   -0.017460
## 5    50.0   4.0     2.263002         2.111197   -0.151805
## 6    50.0   8.0     2.224239         1.926984   -0.297255
## 7    50.0  10.0     2.244215         1.885812   -0.358403
## 8   100.0   2.0     2.231211         2.218871   -0.012340
## 9   100.0   4.0     2.219561         2.166059   -0.053502
## 10  100.0   8.0     2.240535         2.083263   -0.157272
## 11  100.0  10.0     2.232311         2.042789   -0.189522
## 12  250.0   2.0     2.249152         2.251024    0.001871
## 13  250.0   4.0     2.248519         2.226119   -0.022400
## 14  250.0   8.0     2.247794         2.191580   -0.056214
## 15  250.0  10.0     2.230500         2.163938   -0.066563
# MSPE Actual is around 2.23 for all different values of T - 25,50,100,250
# MSPE Cross Validation decreases for evey T and k combination as 
# number of splits increases ---> as k increases more data are feeded
# into training the model and therefore MSPE cross validation decreases
############################
# Result:
# From the simulation results we can comment that for any value of T,
# k=2 splits seems optimum as difference between MSPE Actual 
# and MSPE Cross Validation seems minimum
############################################################################