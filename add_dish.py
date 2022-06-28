#Importing required libraries

import pandas as pd
import pymongo
connectionstring="mongodb+srv://rb0777:Galaxys9plus@cluster0.zuny1ac.mongodb.net/test"
myclient = pymongo.MongoClient(connectionstring)
#Creating database
mydb = myclient["Restaurant_model"]
#Creating collection
posts_1=mydb.add_dishes

# Function for adding dishes
def my_Dish(Name,Price,Description,Non_Veg,Veg,SpiceLevel):
        
    try:
        # Adding required columns
        post_id2 = posts_1.insert_one({"Name":Name,"Price":Price,"Description":Description,"Non_Veg":Non_Veg,"Veg":Veg,"SpiceLevel":SpiceLevel}).inserted_id

        print(post_id2)
        return "Dish_added"
    except:
        return "Dish not added"        
    
                
