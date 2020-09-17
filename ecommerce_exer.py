import numpy as np
import pandas as pd 

# get the .head()
ecom = pd.read_csv("Ecommerce Purchases.csv")
print(ecom.head())

# How many rows and columns are there?
        # ecom.columns
print(ecom.info())

# what is the average purchase price

aveprice = ecom['Purchase Price'].mean()
print(aveprice)

# what were the highest and lowest purchase prices
highestPr = ecom['Purchase Price'].max()
print(highestPr)
lowestPr = ecom['Purchase Price'].min()
print(lowestPr) 

# how many ppl have English 'en' as their language of choice?
print(ecom[ecom['Language']=='en'].count())

# how many ppl have job title of 'Lawyer'
print(ecom[ecom['Job']=='Lawyer'].count())
# or 
print(len(ecom[ecom['Job']=='Lawyer'].index))

# how many people made the purchase during the AM and how many during PM

AMorPM = ecom['AM or PM'].value_counts()
print(AMorPM)


# what are the 5 most common Job Titles

print(ecom['Job'].value_counts().head(5))

# someone made a purchase that came from Lot: "90 WT", what was the purchase 
    # price for this transaction

print(ecom[ecom['Lot']=="90 WT"]['Purchase Price'])

# what is the email of the person with the following Credit Card: 4926535242672853
print(ecom[ecom['Credit Card']==4926535242672853]['Email'])

# how many people have American Express as the CC provider and make a purchase > $95

print(ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]> 95)].count())

# how many ppl have a CC that expires in 2025
def expdate(x):
    if "25" in x.split('/'):
        return True
    else: 
        return False

expires = sum(ecom['CC Exp Date'].apply(lambda x: expdate(x)))
print(expires)
# or 
eexpires = sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25')) 

# what are the top 5 most popular email providers/hosts (gmail.com, yahoo.com)
ecom['email_prov'] = ecom['Email'].apply(lambda email: email.split("@")[1])

print(ecom['email_prov'].value_counts().head(5))