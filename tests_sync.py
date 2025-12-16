import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Warehouse
from sync_crud import CRUD

DB_URL = "postgresql+psycopg://postgres:1234@localhost:5432/mydatabase"
engine = create_engine(DB_URL, echo=False)
session_sync = Session(engine)

crud_Warehouse = CRUD(session_sync, Warehouse)

def api_request_1():
    print("LOG: Начало API запроса 1")
    response = requests.get("https://api.github.com")
    print(f"LOG: Конец API запроса 1, статус: {response.status_code}")
    return response

def api_request_2():
    print("LOG: Начало API запроса 2")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"LOG: Конец API запроса 2, статус: {response.status_code}")
    return response

def sql_request_1():
    print("LOG: Начало SQL запроса 1")
    w1 = crud_Warehouse.create(name="Склад", address="Москва", capacity=1000)
    print(f"LOG: Конец SQL запроса 1, создан: {w1}")
    return w1

def sql_request_2():
    print("LOG: Начало SQL запроса 2")
    warehouses = crud_Warehouse.read_all()
    print(f"LOG: Конец SQL запроса 2, найдено: {len(warehouses)} записей")
    return warehouses

start = time.time()

for i in range(50):
    api_request_1()
    api_request_2()
    sql_request_1()
    sql_request_2()

end = time.time()
print(f"\nСИНХРОННО (140 запросов): {end - start} секунд")