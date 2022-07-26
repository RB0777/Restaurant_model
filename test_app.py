# Importing all libraries
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

#FASTAPI

client=TestClient(app)
    
data_1={"Dish name":"Mutton handi","Price":"780","Description":"Good taste","Non_Veg":1,"Veg":0,"SpiceLevel":"Low"}
output_1 = "Dish_added"

data_2={"DISH_NAME":"Mutton Handi","QUANTITY":"5","SPL_REQ":"Less spicy"}
output_2 = "order_created"

data_3={"DISH_NAME":"Chicken Handi","VEG/NON-VEG":"Non-Veg","PRICE:QUARTER":"200","PRICE:HALF":"400","PRICE:FULL":"800"}
output_3="Menu_Created"

data_4={"id":"62ba088db2f020420d4206a1","Order_Status":"Order_Cooking"}
output_4="Order status updated successfully"


# Testing add_Dish
def test_read_app():
    response=client.post('/add_Dishinfo',json=data_1)
    assert response.status_code == 200
    assert response.json() == output_1


# Testing orders

def test_read_order():
    response=client.post('/orders',json=data_2)
    assert response.status_code == 200
    assert response.json() == output_2

# Testing Menu Created

def test_read_cmenu():
    response=client.post('/menu_created',json=data_3)
    assert response.status_code == 200
    assert response.json() == output_3

# Testing Order Status
def test_read_orderstat():
    response=client.post('/status-update',json=data_4)
    assert response.status_code == 200
    assert response.json() == output_4

