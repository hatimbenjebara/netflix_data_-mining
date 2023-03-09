#we are going to work with data of netflix. this dataset is available in kaggle
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
#importing the data set
df= pd.read_csv("netflix_titles.csv")
#getting some information about data
print(df.head()) #show the first 5 records of the dataset
print(df.describe().transpose()) 
print(df.tail()) #show bottom 5 records of the dataset
a1=df.shape
print(a1) # show the number of rows and columns 
print(df.size) #show number of total values in the dataset
print(df.columns) #show each column name 
print(df.dtypes)#show the data type of each column
print(df.info())# to show indexes, columns, data types of each column memory at once 
# find duplicate record in this dataset and if there's any one remove it 
print(df.duplicated()) # check every row wise nd detect the duplicate rows
print(df[df.duplicated()]) # show duplicated rows
df.drop_duplicates(inplace = True)# remove the duplicate rows permanently and inplace = True to make a changes
a2=df.shape
print(a2)
if a1==a2 :
    print("there's no duplicate in data")
else:
    print("we had a duplicate and we had removed it ")
#check if there s any null values in our data
print(df.isnull())# to show where null value is present if is null then true if not then its false 
print(df.isnull().sum()) #show the count of null values in each column
# let s show the head map
print(sns.heatmap(df.isnull()))
plt.show()
# for House of Cards what is the show Id and who is the director of this show ? 
#getting information about particular element in the dataset
print(df[df['title'].isin(['House of Cards'])]) # we get all row of title = house of cards
a = df[df['title'].isin(['House of Cards'])]
print(a['show_id'])
print(a['director'])
print(a['description'])
print(df[df['title'].str.contains('House of Cards')]) #show all records of a particular string in any column 
# find the highest number of the TV shows and movies were released 
print(df.dtypes)# check for of time 
df['new_col'] =pd.to_datetime(df['release_year'], format='%Y-%m-%d', origin='2000-01-01')
print(df['new_col'])
print(df['new_col'].dt.year.value_counts())#it counts the occurence of all individual years in date column.
df['new_col'].dt.year.value_counts().plot(kind='bar')
plt.show()
# how many movie and tv shows are in the dataset
print(df.groupby('type').type.count()) # groupe all unique items of a column and show their count 
sns.countplot(df['type'])
plt.show()
#show all the movie realese only in 2000
df['new_year'] = df['new_col'].dt.year # new colonne take only year
#filtring the years and type
print(df[(df['type']== 'Movie')&(df['new_year']==2000)])
# show only titles of all tv shows that were only release in usa
#print(df['country'])
print(df[(df['country']=='United States')&(df['type']=='TV Show')])
print(df[(df['country']=='United States')&(df['type']=='TV Show')]['title']) #only title
#show top 10 of directors tv show and movies the highest number
print(df['director'].value_counts().head(10)) # top 10 directors
#find a movie or tv show where Jesse Eisenberg was cast 
new_df=df.dropna() # drop all nan values to use str.contains function 
print(new_df[new_df['cast'].str.contains('Jesse Eisenberg')]['title']) # after drop nan values , we can find it 
# what are the different rating defined by netflix
print(df['rating'].nunique()) # sum of rating 
print(df['rating'].unique())
#how many movies got the 'TV-14' rating in canada 
print(df[(df['country']=='canada')&(df['rating']=='TV-14')&(df['type']=='movie')].shape)
#max duration of movie or show 
print(df['duration'].unique()) #saison and minutes
print(df['duration'].dtypes) # object
df[['minutes','unit']] = df['duration'].str.split(' ',expand=True) # seperate by space
print(df.head())
df['minutes']=pd.to_numeric(df['minutes'])
print(df['minutes'].max())





