import pandas as pd
s=pd.Series([1,2,3,4,5])
print(s)
print(type(s))

# d=pd.Series({"one":10,"two":20,"three":30},index={'one','two','three','a','b','c'})
# print(d)
# print(type(d))

# extraxct element 
a=pd.Series([1,2,3,4,5,6])
print(a[4])
print(a[-3])
print(a[:5])

b = pd.Series(['p','q','r','s','t'], index = [10,11,12,13,14], name = 'alphabets')

# addition
print(a+10)

# Dataframe => Two dimensional labelled data structure 
data=pd.DataFrame({"name":["radha","krishna"],"marks"[100,200]})
b = {'RollNo.':pd.Series([1,2,3,4,5]), 
    'Maths':pd.Series([67,89,23,90,56]), 
    'Physics':pd.Series([12,98,44,90,78])}      

df = pd.DataFrame(b)
# read any csv file
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(data)
data.head()

data.tail()

data.describe()
data.shape

data.iloc[5:9 ,1:3]

# locaion 

data.loc[0:3,('sepal_lengh','petal_width','species')]

# dropan data
data.drop([128,121,123],axis=0)
data.iloc[120:125,:].head()

data.drop([1,2,3],axis=0)

data.drop('petal_width' , axis=1)


# minimum row and column facth in iloc 
data.iloc[ 120: 130 ,: ].head()

ans=data.drop([120,121,123], axis=0)
print(ans)
#data.iloc[ 120: 130 ,: ].head()

# data.iloc[ 115: 125 ,: ].head()


ans=data.drop([1,2,3], axis=0)
print(ans.shape)
print(data.shape)
data.shape

ans=data.drop([120,122,123], axis=0)

ans.iloc[ 115 : 130 , ]

data.min()

data.max()

data.median()

'''---handling missing value----'''
df.isnull()
df.isnull().sum()
df2 = df.dropna()
df3 = df.dropna(axis = 1)    # axis = 1 for columns
df.dropna(how = 'any')    # if any row value is null then remove that row
df.dropna(how = 'all')    # if all row values is null then remove that row

# Filling the Null Values
df.fillna(0)
df.fillna(method = 'ffill')
