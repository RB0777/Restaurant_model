import pandas as pd

def my_Dish(Name,Price,Description,Non_Veg,Veg,SpiceLevel):

    df = pd.read_excel("Menu.xlsx")

    YourDataInAList = [12.34,17.56,12.45]

    df = df.append(["Name",Name,"Price",Price,"Description",Description,"Non_Veg",Non_Veg,"Veg",Veg,"SpiceLevel",SpiceLevel], ignore_index=True)
    # df=df.transpose()
    df.to_excel("Menu.xlsx",index=False,startcol=1,startrow=5)
    
my_Dish("Mutton_tikka",6262,"Rich_curry_cooked_with_roasted_paneer",0,1,"Low")