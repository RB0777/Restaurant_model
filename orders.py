# Importing required Libraries
import pandas as pd
import uuid
import pymongo
connectionstring="mongodb+srv://rb0777:Galaxys9plus@cluster0.zuny1ac.mongodb.net/test"
myclient = pymongo.MongoClient(connectionstring)
#Creating database
mydb = myclient["Restaurant_model"]
posts_4=mydb.orders

# Function for getting order details
def order_details(Name,Quantity,Spl_req,Order_Status):
    try:
        id = str(uuid.uuid1())
        # Adding required columns
        posts_id4=posts_4.insert_one({"UID":id,"DISH_NAME":Name,"QUANTITY":Quantity,"SPL_REQ":Spl_req,"Order_Status":'Order_Accepted'}).inserted_id
        print(posts_id4)
        return "order_created"
    except:
        return "Order not created"
    
