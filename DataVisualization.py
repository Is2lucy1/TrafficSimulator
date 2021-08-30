import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# Open output file
df = pd.read_csv("output.csv")

df['Arrive'] = df['Arrive'].values // 3600 # convert to hours



#test_1 = df.Test_No == 1
#print(test_1)
#To print one column
#print(df.head(4))
#print(df.dtypes)
#sum = 0
j = 1
wait = 0
hour = 1
list = []
test = 1

#To look for only Test_No == 1
byTest = df.loc[df['Test_No'] == 3]
#print(byTest)
byCar = byTest.groupby('Arrive').mean()
print(byCar)
print('whatsup')

set = df.groupby('Test_No').Wait.agg(['count', 'min', 'max', 'mean'])

set1 = df.groupby('Test_No').Wait.mean()

set2 = df.groupby('Test_No').mean()
#print(set)
#print(set1)
#print(set2)
#while df.Test_No[j] == test:
  #while hour < 12:
    #while df.Arrive[j] < hour:
     # wait = wait + df.Wait[j]
     # j += 1
      #print(Wait)
    #print(j, test, hour, wait) 
    #wait = 0
    #j += 1
    #hour = hour + 1
  #print('test is: ', test)
  #test = test + 1
  #hour = 0
  #j = j + 1
  #print('test is: ', test)
  #print(hour, test, wait)
    

#print(j, wait, test, hour)
#print(list)

#if df.Test_No[i] == '1':
  #print(sum + df.Arrive[i])
  #i = i + int(df.Arrive[i])
  #print(i)
  #print(df.Arrive[0:5])
  #print(df['Arrive'])

#test = Test_1['Arrive'].values
#print("the test is: ", test)

#dataset =  df.groupby('Arrive')['Car_Number'].count()

#dataset = df.groupby('Arrive')['Wait'].mean()
#print(dataset)
#wait = data['Wait'].values
#plt.style.use('fivethirtyeight')
#dataset.plot.bar()
#plt.show()

#To look for only Test_No == 1


#print(len(test))
#tester = []
#if df['Test_No'] == '1':
  #tester.append['Arrive']


#Read each column
#print(df.columns)

#Read first 5 index for Arrive column
#print(df['Arrive'][0:5])

#Read first 4 rows
#print(df.head(4))

#Read each row
#print(df.iloc[1:4])

#for index, row in df.iterrows():
  #print(index, row['Car_Number'])


#Create total and displaying total for first 5 columns
#df['Total'] = df['Arrive'] + df['Wait']
#print(df['Total'][0:5])


#df['Arrive'] = df['Arrive'].values // 3600 # convert to hours
#dataset =  df.groupby('Arrive')['Car_Number'].count()
#dataset = df.groupby('Arrive')['Wait'].mean()
#print(dataset)
#wait = data['Wait'].values
#plt.style.use('fivethirtyeight')
#dataset.plot.bar()
#plt.show()
