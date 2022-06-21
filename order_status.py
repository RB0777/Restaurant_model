#Importing required libraries
import pandas as pd

#Importing helper function
import get_location as gl

# Function for updating order status
def change_status(UID,Order_Status):
    try:
            # Reading  excel file
            df = pd.read_excel("orders.xlsx")
            index=gl.getIndexes(df,UID)
            
            df.at[ index[0] , 'Order_Status'] = Order_Status
        # Saving excel File    
            df.to_excel("orders.xlsx")
            return "updated"
    except:
         return "Failed to update"   