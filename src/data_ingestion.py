import os
import pandas as pd

df = pd.read_csv(r'C:\Users\XM891JZ\Downloads\Ecommerce Customers.csv')
df = df[df['Length of Membership'] > 2]
df = df.drop(columns = ['Email','Address','Avatar'])
df.to_csv('./data/customers.csv')
