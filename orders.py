# Importing required Libraries
import pandas as pd
import uuid

# Function for getting order details
def order_details(Name,Quantity,Spl_req,Order_Status):
    try:
        id = uuid.uuid1()
        # Reading  excel file 
        df = pd.read_excel("orders.xlsx")
        # Adding required columns
        df = df.append({"UID":id.int,"DISH_NAME":Name,"QUANTITY":Quantity,"SPL_REQ":Spl_req,"Order_Status":'Order_Accepted'}, ignore_index=True)
        # Saving excel file
        df.to_excel("orders.xlsx",index=False)
        return "order_created"

    except:
        return "Order can't be created"
