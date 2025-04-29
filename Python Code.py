import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

file = pd.read_csv("Chocolate Sales.csv")
print(file.shape)

# turning date into datetime format
file['Date'] = pd.to_datetime(file['Date'], format='%d-%b-%y')



#function to remove dollar
def remov_dollar(x):
    return x.replace('$', '').replace(',', '').replace(' ', '')
#converting the column to float
file['Amount'] = file['Amount'].apply(remov_dollar)
file.Amount = pd.to_numeric(file.Amount, errors='coerce').astype('float', 2)
file['Amount'] = round(file.Amount,2) # not sure why it still shows 1 decimal place if anyone know pls comment to tell me

# grouping by country and their average price 
country_vs_avgprice = file.groupby("Country")['Amount'].mean()
print(country_vs_avgprice)

#Bar graph the countries vs avg price
plt.bar(country_vs_avgprice.index, country_vs_avgprice.values)
plt.title("Average Price of Chocolates by Country")
plt.xlabel("Country")
plt.ylabel("Average Price")
plt.ylim(5400, max(country_vs_avgprice.values) + 100) # starts plot at 5400 on Yaxis
plt.show()

# Result, Uk, USA, India top 3 countries, Uk highest with ~5900, USA ~5780(100 less ish)

# want to know country with the avg boxes orders.
country_boxshipping = file.groupby('Country')['Boxes Shipped'].mean()
print (country_boxshipping)

'''
Canada with the highest number of boxes ordered followed by UK (178 and 170 box shipped respectivly) 
USA has the lowest, indicates that orders the most expensive chocolate (high price per box)(150 box shipped)
'''
#price per box by country
price_per_box = file['Amount']/file['Boxes Shipped'] #for all rows
#sort it by country avg price/avg box shipped


#print(file['Country'].value_counts())
#print (file.describe())
