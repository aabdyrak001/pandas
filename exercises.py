import numpy as np 
import pandas as pd 

# read salaries.csv
sal = pd.read_csv("Salaries.csv")
print(sal)
# check the head of the DF 
print(sal.head())
# use the .info() method to find out how many entries there are
print(sal.info())

# what is the 'ave base pay' 
    # By setting errors=’coerce’, you’ll transform the non-numeric values into NaN.
sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors = 'coerce')
print(sal['BasePay'].mean()) 

# what is the highest amount of OVertimePay
    # transfer to int first 
sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors = 'coerce')
print(sal['OvertimePay'].max())

# what is the job title of Josehp Driscoll
jobtitle = sal[sal['EmployeeName'] =='JOSEPH DRISCOLL']['JobTitle']
print(jobtitle)

# how much does J.Driscoll make?
DriscollSalary = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(DriscollSalary)

# What is the name of the highest paid person 
highestPaid = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
print(highestPaid)
        # or
highest = sal.loc[sal['TotalPayBenefits'].idxmax()]
print(highest)

# what is the lowest paid employee
lowestPaid = sal.iloc[sal['TotalPayBenefits'].argmin()]
print(lowestPaid)

# what is the mean BasePay of all employees per year (2011-2014)
BasePayMean = sal.groupby('Year')['BasePay'].mean()
print(BasePayMean)

# how many unique job titles 

uniqueTitles = sal['JobTitle'].nunique()
print(uniqueTitles)

# what are the top 5 most common jobs
mostCommon = sal['JobTitle'].value_counts().head(5)
print(mostCommon)

# how many Job Titles were represented by only one person in 2013 
onlyOne = sum(sal[sal['Year'] ==2013]['JobTitle'].value_counts()==1)
print(onlyOne)

# how many people have the word "Chief " in their job title 
    # split job title and for that if Chief then count
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

chief = sum(sal['JobTitle'].apply(lambda x: chief_string(x)))
print(chief)

#correl 
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal['title_len'])


correl = sal[['title_len', 'TotalPayBenefits']].corr()
print(correl)