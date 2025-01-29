import pandas as pd

##load data

#set file path to excel data file
file_path = 'data/sus_results.xlsx'

#read excel
df = pd.read_excel(file_path)

#display first few rows of dataframe to check data
print(df.head())

##clean data

#check for missing values
print(df.isnull().sum())

#fill missing values with 0
df = df.fillna(0)

#check cleaned data
print(df.head())

