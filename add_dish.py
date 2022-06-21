#Importing required libraries

import pandas as pd

# Function for adding dishes
def my_Dish(Name,Price,Description,Non_Veg,Veg,SpiceLevel):
    try:    
        # Reading  excel file    
            df = pd.read_excel("Menu.xlsx")
            # Adding required columns
            df = df.append({"Name":Name,"Price":Price,"Description":Description,"Non_Veg":Non_Veg,"Veg":Veg,"SpiceLevel":SpiceLevel}, ignore_index=True)
            # Saving excel file
            df.to_excel("Menu.xlsx",index=False)    
            return "Dish_added"
    except:
        return "Dish can't be added"        

