
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
mydb = myclient["Restaurant_model"]
collections = mydb["orders"]
print(collections)
def order_update(id,Order_Status):
# create object of type ObjectId
    objInstance = ObjectId(id)
#Updating Order Status
    d=collections.update_one({"_id":objInstance},{"$set":{"Order_Status":Order_Status}})    
    return "Order status updated successfully"


