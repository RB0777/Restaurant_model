# Importing required Libraries
import pandas as pd
import pymongo
connectionstring="mongodb+srv://rb0777:Galaxys9plus@cluster0.zuny1ac.mongodb.net"
myclient = pymongo.MongoClient(connectionstring)
# importing MongoClient from pymongo
from pymongo import MongoClient
import pprint
# importing ObjectId from bson library
from bson.objectid import ObjectId
#Defining Database
mydb = myclient["Restaurant_model"]
collections = mydb["orders"]
my_col = mydb["add_dishes"]
#Creating Collections
posts_5=mydb.bill_generate
print(collections)
# Function for fetching DISH NAME and QUANTITY from ORDERS
def fetch_quantity(id):
    try:
# create object of type ObjectId
        objInstance = ObjectId(id)
        q=collections.find_one({'_id':objInstance})
        d_name=(q.get('DISH_NAME'))
        qty=int(q.get('QUANTITY'))
        print(d_name,qty)
#Defining nested function for getting Price of dish from Menu
        def fetch_price(d_name):
#Searching for name in menu and geeting dish price
            m=my_col.find_one({'Name':d_name})
            d_price=int(m.get('Price'))            
            print(d_price)
#Total Bill Amount
            total=qty*d_price
            print(total)
            
#Adding required Columns to database
            post_id5 = posts_5.insert_one({"DISH_NAME":d_name,"PRICE":d_price,"QUANTITY":qty,"TOTAL":total}).inserted_id
            print(post_id5)            
        fetch_price(d_name)    
        return "Bill generated sucessfully"
    except:
        return "dish not available"



