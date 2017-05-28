
# coding: utf-8

# In[277]:

import numpy as nm
import pandas as pd
import random
import matplotlib.pyplot as pl


# In[37]:

score_card=pd.read_csv("/home/anurag/Downloads/Data/Most-Recent-Cohorts-Scorecard-Elements.csv")
post_earning=pd.read_csv("/home/anurag/Downloads/Data/Most-Recent-Cohorts-Scorecard-Elements.csv")
recent_data=pd.read_csv("/home/anurag/Downloads/Data/Most-Recent-Cohorts-All-Data-Elements.csv",low_memory=False)


# In[27]:

score=score_card[['UNITID','OPEID6','SAT_AVG_ALL','NPT4_PRIV']]
#earn=score_card[['UNITID','OPEID6','CDR3_DENOM']]
score_cols=list(score_card.columns.values)
print(score_cols)
#print(score.head(10))


# In[39]:

earn=post_earning[['UNITID','OPEID6','SAT_AVG_ALL','MD_EARN_WNE_P10']]
earn_cols=list(post_earning.columns.values)
print(earn_cols)
#print(earn.head(10))


# In[61]:

recent_cols=list(recent_data.columns.values)
print(recent_cols)


# In[356]:

recent=recent_data[['UNITID','OPEID','OPEID6','LOCALE','UG','SAT_AVG_ALL','NPT4_PRIV','CDR2','CDR3','MD_EARN_WNE_P10']]
corr_data=recent_data[['COMPL_RPY_1YR_RT']]
corr_data=corr_data[corr_data.COMPL_RPY_1YR_RT!='PrivacySuppressed']
print("Before the nan ",corr_data.shape)
#recent=recent.dropna()
print("After the nan ",corr_data.shape)
corr_data=corr_data.dropna()
corr_data.iloc[random.sample(range(1,1000),10)]
#print(recent.head(20))
#test=recent_data[recent_data['LOCALE']==12]
#print(test[['UNITID','OPEID']])
#print(recent.shape)


# In[192]:

y=recent_data.corr(method='pearson', min_periods=100)['CDR2']
print((y[y[:]>0.2]).shape)


# In[408]:

#list_features=recent_data.filter(regex='UGDS')
#list_features=list_features.append(recent_data.filter(regex='CDR'))
list_features=recent_data[['OPEID','LOCALE','UGDS','NPT4_PUB','TUITIONFEE_IN','TUITIONFEE_OUT','ADM_RATE_ALL','SAT_AVG_ALL','CUML_DEBT_N','PCTPELL','CDR2','CDR3','COMPL_RPY_1YR_RT']]
list_val=['OPEID','LOCALE','UGDS','NPT4_PUB','TUITIONFEE_OUT','TUITIONFEE_IN','ADM_RATE_ALL','SAT_AVG_ALL','CUML_DEBT_N','PCTPELL','CDR2','COMPL_RPY_1YR_RT']
list_features=list_features[list_features.COMPL_RPY_1YR_RT!='PrivacySuppressed']
list_features=list_features[list_features.CUML_DEBT_N!='PrivacySuppressed']
list_features=list_features.dropna()
#print(list_features.head(10))
#target_features=list(recent_data.columns.values)
#list_features.dropna()
corr_score=[]
data={}
print(list_features.shape)
for feat in target_features:
    y=list_features.corr(method='pearson')[feat]
    #corr_score.append((y[y[:]>0.2]).shape)
    data[feat]=((y[y[:]>0.5]).shape)
get_ipython().magic('matplotlib inline')
#print(corr_score)
#pl.bar(range(len(data)),list(data.values()),align='center')
#pl.xticks(range(len(data)),list(data.keys()),align='center')
#pl.show
print(data)
#data={int(k):int(v) for k,v in data.items()}
#pl.plot(list(data.keys()), list(data.values()))
#pl.xlabel("Correlation Value")
#pl.ylabel("Features")
#corr_score.append(y.shape)e


# In[399]:

list_features.corr(method='pearson')['CDR2']


# In[406]:

list_features.plot.scatter(x='CDR2', y='PCTPELL')
list_features.plot.scatter(x='CDR3', y='PCTPELL')
list_features.plot.scatter(x='TUITIONFEE_IN', y='SAT_AVG_ALL')
list_features.plot.scatter(x='TUITIONFEE_OUT', y='SAT_AVG_ALL')


# In[ ]:



