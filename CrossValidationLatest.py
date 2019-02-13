# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 01:40:48 2018

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

### Cross Validation  Complete code as explained by professor         
sig=0.5
bigT=T*2
mu_x=1
sig_x=2
k=4
b0=0.5
b1=1
nsim = 1000
kvec = [2,4,8,10]
Tvec = [25,50,75,100]
outp =np.zeros((nsim,len(Tvec),len(kvec),5))
for tdx,T in enumerate(Tvec):
    bigT = T*2
    for kdx,k in enumerate(kvec):
        for isim in range(nsim):
            e = np.random.normal(0,sig,size=(bigT,1))
            x = np.random.normal(mu_x,sig_x,size=(bigT,1))
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

outp[:,:,:].mean(0)
df=pd.DataFrame(np.vstack(outp[:,:,:].mean(0)))
df.columns=['T','k','mspe_actual','mspe_crossvalid','difference']
df
