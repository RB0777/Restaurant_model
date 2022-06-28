import pandas as pd
import get_location as gl
import generate_bill as gb
def bill_generate(UID):
    try:
        order = pd.read_excel("orders.xlsx")
        oi=gl.getIndexes(order,UID)
        print(oi)
        menu = pd.read_excel("Menu.xlsx")
        d_name=(order['DISH_NAME'].iloc[oi[0]])
        d_qty=(order['QUANTITY'].iloc[oi[0]])
        
        di=gl.getIndexes(menu,d_name)
        print(di)
        qty=(d_qty)
        # mn=gl.getIndexes(menu,Price)
        price=(menu['Price'].iloc[di[0]])
        total=(qty*price)
        bl=gb.report(UID,d_name,qty,total)

        return"Bill generated successfully"
    except:
        return"Bill generation failed"
