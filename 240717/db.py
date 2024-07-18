import pandas as pd
import sqlite3
import seaborn as sns
from matplotlib import pyplot as plt

#Importing all tables from the relational database 

brands = pd.read_csv('data/brands.csv')
categories = pd.read_csv('data/categories.csv')
customers = pd.read_csv('data/customers.csv')
order_items = pd.read_csv('data/order_items.csv')
orders = pd.read_csv('data/orders.csv')
products = pd.read_csv('data/products.csv')
staffs = pd.read_csv('data/staffs.csv')
stocks = pd.read_csv('data/stocks.csv')
stores = pd.read_csv('data/stores.csv')

#Create the database conection
connection = sqlite3.connect('bike_store.db')

# Insert data into database
brands.to_sql('brands', connection, if_exists='replace', index=False)
categories.to_sql('categories', connection, if_exists='replace', index=False)
customers.to_sql('customers', connection, if_exists='replace', index=False)
order_items.to_sql('order_items', connection, if_exists='replace', index=False)
orders.to_sql('orders', connection, if_exists='replace', index=False)
products.to_sql('products', connection, if_exists='replace', index=False)
staffs.to_sql('staffs', connection, if_exists='replace', index=False)
stocks.to_sql('stocks', connection, if_exists='replace', index=False)
stores.to_sql('stores', connection, if_exists='replace', index=False)
