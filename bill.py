import pandas as pd
import get_location as gl
def bill_generate(UID):
    
    order = pd.read_excel("orders.xlsx")
    oi=gl.getIndexes(order,UID)
    print(order)
bill_generate(1.38148922895775E+38)