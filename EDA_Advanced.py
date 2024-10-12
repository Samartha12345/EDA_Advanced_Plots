#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import seaborn as sns


# In[4]:


pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\customer_shopping_data (1).csv')


# In[6]:


sm = pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\customer_shopping_data (1).csv')


# In[6]:


list(sm.shopping_mall.unique())


# In[7]:


df1 = pd.DataFrame(sm.shopping_mall.value_counts())


# In[8]:


df1.columns=['count_cust']
df1
##shopping mall is the index and count_cust is column name .count is the name of fucntion in python so column name canr ben same


# In[9]:


plt.figure(figsize=(7,5))
plt.pie(df1.count_cust,labels  = df1.index,autopct='%1.0f');


# In[10]:


df1.index


# In[30]:


sm.category.value_counts()


# In[14]:


df2 = pd.DataFrame(sm.category.value_counts())


# In[15]:


df2.columns=['Category_counts']


# In[35]:


df2


# In[11]:


plt.figure(figsize=(7,5))
plt.pie(df2.Category_counts,labels  = df2.index,autopct='%1.0f',explode = (.1,0,0,0,0,0,0,0));


# In[ ]:


plt.figure(figsize=(10, 6))
sns.barplot(x=df2.index, y=df2.values)


# In[8]:


plt.figure(figsize=(10, 6))
plt.bar(df1.index,df1.count_cust,color=['pink','skyblue','yellow','lightgreen'])
plt.xticks(rotation=60);
plt.grid()
plt.title("Footfall of different malls")


# In[63]:


plt.figure(figsize=(10,6))
plt.bar(df2.index,df2.Category_counts,color='pink')
plt.xticks(rotation=60);
##bar graph takes 1d array only


# In[64]:


plt.figure(figsize=(10, 6))
sns.barplot(x=category1.index, y=category1.values)


# In[17]:


var2 = sm.category.value_counts()


# In[18]:


plt.figure(figsize=(10, 6))
sns.barplot(x=var2.index, y=var2.values)
plt.grid()


# In[85]:


plt.figure(figsize=(10,6))
sns.countplot(x = 'shopping_mall',data = sm, order=sm['shopping_mall'].value_counts().index,hue='category')
plt.xticks(rotation=60);

##below  graph shows the footfalls of different malls with counts where kanyon mall has highest number of count or footfall 


# In[9]:


plt.figure(figsize = (10,6))
sns.countplot(x='category',data = sm,order=sm['category'].value_counts().index,hue = 'gender', palette='viridis')
plt.xticks(rotation = 60);palette='viridis'
##order=sm['category'].value_counts().index---> this line of code is used to sort the graph in particular order
##hue just splits the data again into the values you give it the hue for ex it is splitted into gender with male and female


# In[89]:


sm.head()


# In[ ]:





# In[91]:


df3 = pd.DataFrame(sm.groupby('category').price.sum())
#basically converted into 1d data 
##here category is index and column name is price


# In[ ]:





# In[112]:


plt.figure(figsize=(7,5))
plt.pie(df3.price[0:4],labels = df3.index[0:4],autopct='%1.0f%%');


# In[102]:


df3 = pd.DataFrame(sm.groupby('category').price.sum())
df3 = df3.sort_values('price',ascending=False)
##data for the top 4


# In[108]:


df3.price[0:4]
df3.index[0:4]


# In[113]:


plt.figure(figsize=(7,5))
plt.pie(df3.price[4::],labels = df3.index[4::],autopct='%1.0f%%');
##data for the bottom 4


# In[114]:


df3


# In[115]:


plt.figure(figsize=(10,6))
plt.bar(df3.index,df2.price,color='pink')
plt.xticks(rotation=60);


# In[ ]:


plt.figure(figsize=(10, 6))
sns.barplot(x=var2.index, y=var2.values)
plt.grid()


# In[117]:


var4 = sm.groupby('category').price.sum()


# In[120]:


plt.figure(figsize=(10, 6))
sns.barplot(x=var4.index, y=var4.values)
plt.grid()


# In[121]:


df3


# In[125]:


df3['price_in_million']=df3.price/1000000


# In[126]:


df3


# In[130]:


plt.bar(df3.index,df3.price_in_million,color='pink')
plt.xticks(rotation=60);


# In[19]:


ist = sm[sm.shopping_mall=='Mall of Istanbul']


# In[20]:


ist


# In[135]:


sns.boxplot(x='category',y='price', data = ist)
plt.xticks(rotation=45);


# In[138]:


sm.age.describe()


# In[139]:


sm.age.skew()


# In[140]:


sm.age.median()


# In[141]:


sm


# In[142]:


sm.payment_method.value_counts()


# In[21]:


df5 = pd.DataFrame(sm.payment_method.value_counts())


# In[22]:


df5


# In[23]:


df5.columns=['Payment_count']


# In[24]:


df5


# In[ ]:


##mall of istanbul and kanyon


# In[27]:


sm.groupby('gender').price.sum()/1000000


# In[1]:


plt.pie(df5.Payment_count,labels=df5.index);


# In[31]:


##purchasing power of people in age group less than or equal to 30 and compare it with equal to 40 and 50


# In[35]:


sm.groupby('age').price.sum()


# In[38]:


sm.groupby('age').price.sum()


# In[43]:


var1_income= sm[sm.age<=30]


# In[45]:


var2_income = sm[(sm.age>40) & (sm.age<=50)]


# In[48]:


var1_income.age.mean()


# In[49]:


var2_income.age.mean()


# In[ ]:


##seperate notebook on adidas 


# In[1]:


import pandas as pd


# In[2]:


import plotly as px


# In[3]:


import cufflinks as cf


# In[14]:


pip install cufflinks


# In[4]:


import cufflinks as cf


# In[2]:


from plotly import __version__
print(__version__)


# In[5]:


from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot


# In[6]:


init_notebook_mode(connected = True) ##to connect to the notebook


# In[7]:


cf.go_offline()


# In[7]:


import pandas as pd


# In[8]:


pd.read_csv(r"C:\Users\Dell\Desktop\Pandas file\LungCapData.csv")


# In[8]:


lc  = pd.read_csv(r"C:\Users\Dell\Desktop\Pandas file\LungCapData.csv")


# In[10]:


lc.iplot(kind = 'scatter',x='Age',y = 'LungCap',mode = 'markers',color='blue')
##with the increase in the age,the  lungcapacity of people is increasing 
#showing it through scatter plot


# In[16]:


lc.iplot(kind = 'bar',x= 'Gender',y = 'LungCap')


# In[18]:


lc.iplot()


# In[19]:


lc.iplot(kind = 'box')


# In[20]:


pd.read_csv(r"C:\Users\Dell\Desktop\Pandas file\CreditRisk.csv")


# In[11]:


cr  = pd.read_csv(r"C:\Users\Dell\Desktop\Pandas file\CreditRisk.csv")


# In[14]:


cr.iplot(kind = 'box')


# In[27]:


lc.iplot(kind = 'hist')


# In[28]:


countries = ('USA','CHINA','JAPAN','GERMANY','UK','INDIA')
GDP = (19.4,11.8,4.8,3.4,2.5,2.4)
count_gdp = pd.DataFrame({'GDP':(19.4,11.8,4.8,3.4,2.5,2.4),
                         'countries':('USA','CHINA','JAPAN','GERMANY','UK','INDIA')})


# In[30]:


count_gdp


# In[33]:


import plotly.express as pe


# In[41]:


pe.pie(count_gdp,names='countries',values='GDP',title='GDP of Different countries',hole=.4)


# In[ ]:


##sun burst Chart


# In[6]:


sm = pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\customer_shopping_data (1).csv')


# In[3]:


import plotly.express as px


# In[4]:


sm['Sales_Values'] = sm.price*sm.quantity


# In[5]:


fig = px.sunburst(sm,path = ['shopping_mall','category'],values = 'Sales_Values' , width= 700,height=700)
fig.show()


# In[44]:


sm.head()


# In[51]:


fig = px.treemap(sm,path=[px.Constant('Shopping Mall data'),'shopping_mall','category'],values = 'Sales_Values',color_discrete_sequence=px.colors.qualitative.Pastel)


# In[52]:


fig


# In[ ]:


plt.figure(figsize=(6,10))
plt.scatter(Prod_sales['Number_of_product'],Prod_sales['Sales_in_million'],
                        s=Prod_sales['Sales_in_million']*100,color='red',alpha=0.4)
plt.grid()


# In[54]:


prod_sales = pd.DataFrame()
prod_sales['Number_of_product']=[16,25,30,45,60,75,100]
prod_sales['Sales_in_million']=[10,20,34,45,60,78,120]


# In[55]:


prod_sales


# In[57]:


import matplotlib.pyplot as plt


# In[61]:


plt.figure(figsize=(10,10))
plt.scatter(prod_sales['Number_of_product'],prod_sales['Sales_in_million'],
                        s=prod_sales['Sales_in_million']*70,color='red',alpha=0.4)
plt.grid()


# In[62]:


pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\customer_shopping_data (1).csv')


# In[63]:


sm = pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\customer_shopping_data (1).csv')


# In[64]:


sm.gender.value_counts()


# In[65]:


df1 = pd.DataFrame(sm.gender.value_counts())


# In[66]:


df2 = pd.DataFrame(sm.category.value_counts())


# In[67]:


df2


# In[68]:


df3 = pd.DataFrame(sm.payment_method.value_counts())


# In[69]:


df3


# In[70]:


df4 = pd.DataFrame(sm.shopping_mall.value_counts())


# In[71]:


df4


# In[78]:


df1.columns=['Gender_counts']


# In[79]:


df1


# In[80]:


df2.columns=['Category_count']


# In[83]:


df3.columns=['PayMethod']


# In[85]:


df4.columns=['Mall-Count']


# In[87]:


fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(10,8),constrained_layout=True)
ax[0,0].bar(df1.index,df1.Gender_counts,color='green')
ax[0,1].bar(df2.index,df2.Category_count,color='blue')
ax[1,0].bar(df3.index,df3.PayMethod,color='red')
ax[1,1].bar(df4.index,df4.Mall-Count,color='pink')


# In[91]:


df4.columns=['mall']


# In[95]:


fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(10,8),constrained_layout=True)
ax[0,0].bar(df1.index,df1.Gender_counts,color='green')
ax[0,1].bar(df2.index,df2.Category_count,color='blue')
ax[1,0].bar(df3.index,df3.PayMethod,color='red')
ax[1,1].bar(df4.index,df4.mall,color='pink')

ax[0,1].tick_params(axis='x',rotation=60)
ax[0,1].title.set_text("Sales based on malls")


# In[96]:


pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\train.csv')


# In[97]:


tr = pd.read_csv(r'C:\Users\Dell\Desktop\Pandas file\train.csv')


# In[98]:


tr.head()


# In[99]:


tr.info()


# In[101]:


df5 = pd.DataFrame(tr.mobile_wt.value_counts())


# In[103]:


df5.columns=['MobWt']


# In[105]:


df5


# In[106]:


df6 = pd.DataFrame(tr.ram.value_counts())


# In[107]:


df6


# In[108]:


plt.bar(df5.index,df5.MobWt)


# In[109]:


plt.pie(df5.MobWt,labels = df5.index)


# In[111]:


var1=tr.groupby('price_range').ram.mean()


# In[117]:


var1


# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import seaborn as sns


# In[120]:


sns.barplot(x= var1.index,y = var1.values,palette= 'viridis')


# In[122]:


df6 = pd.DataFrame(tr.groupby('price_range').ram.mean())


# In[123]:


df6


# In[135]:


plt.figure(figsize=(12,6))
plt.scatter(df6.index,df6['ram'],
                        s=df6['ram']*2,color='blue',alpha=0.4)
plt.grid()
plt.xlabel("Price Range")
plt.ylabel("Ram")
plt.title("Ram vs Price Range")


# In[139]:


tr.groupby('price_range').battery_power.mean()


# In[142]:


df7 = pd.DataFrame(tr.groupby('price_range').battery_power.mean())


# In[143]:


df7


# In[144]:





# In[154]:


var2=tr.groupby('price_range').clock_speed.sum()


# In[157]:


var2.values


# In[158]:


sns.barplot(x= var2.index,y = var2.values,palette= 'viridis')


# In[ ]:


fig = px.treemap(tr,path=[px.Constant('Mobile'),'price_range','mobile_wt'],values = 'Sales_Values',color_discrete_sequence=px.colors.qualitative.Pastel)

