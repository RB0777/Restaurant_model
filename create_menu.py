#Importing required libraries
import pandas as pd
import pymongo
connectionstring="mongodb+srv://rb0777:Galaxys9plus@cluster0.zuny1ac.mongodb.net/test"
myclient = pymongo.MongoClient(connectionstring)
#Creating database
mydb = myclient["Restaurant_model"]
posts_3=mydb.create_menu
# Function for creating menu
def Create_Menu(Name,Choice,Quarter,Half,Full):
        
    try:
            # Adding required columns
            post_id3 = posts_3.insert_one({"DISH_NAME":Name,"VEG/NON-VEG":Choice,"PRICE:QUARTER":Quarter,"PRICE:HALF":Half,"PRICE:FULL":Full}).inserted_id
            print(post_id3)
            return "Menu_Created"
    except:
        return"Menu not created"    