#Importing required libraries
import pandas as pd

# Function for creating menu
def Create_Menu(Name,Choice,Quarter,Half,Full):
        try:
            # Reading  excel file    
            df = pd.read_excel("Create_Menu.xlsx")
            # Adding required columns
            df = df.append({"DISH_NAME":Name,"VEG/NON-VEG":Choice,"PRICE:QUARTER":Quarter,"PRICE:HALF":Half,"PRICE:FULL":Full}, ignore_index=True)
            # Saving excel file
            df.to_excel("Create_Menu.xlsx",index=False)
            return "Menu_Created"
        except:
            return "Menu can't be created"