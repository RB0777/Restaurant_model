# Importing all libraries
import pandas as pd
import pymongo
from openpyxl import load_workbook
from fastapi import FastAPI,Request
from typing import Optional

# Importing all helper functions
import add_dish as add
import orders as ord
# import order_status as os
import create_menu as mcr
# import bill as bl

# FastAPI 
app = FastAPI()

# Defining all the end-points of API

# Adding Dishes to excel file
@app.post('/add_Dishinfo')
async def post_form(request: Request):
        req_info = await request.json()
        result=add.my_Dish(req_info["Dish name"],req_info["Price"],req_info["Description"],req_info["Non_Veg"],req_info["Veg"],req_info["SpiceLevel"])
        return result

# Creating orders        
@app.post('/orders')
async def post_form(request: Request):
        req_info = await request.json()
        result=ord.order_details(req_info["DISH_NAME"],req_info["QUANTITY"],req_info["SPL_REQ"],["Order_Status"])
        return result


# Creating menu
@app.post('/menu_created')
async def post_form(request: Request):
        req_info = await request.json()
        result=mcr.Create_Menu(req_info["DISH_NAME"],req_info["VEG/NON-VEG"],req_info["PRICE:QUARTER"],req_info["PRICE:HALF"],req_info["PRICE:FULL"])
        return result

