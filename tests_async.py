import asyncio
import time
import httpx

from database import session
from models import Warehouse
from async_crud import AsyncCRUD

crud_Warehouse = AsyncCRUD(Warehouse)

async def api_request_1():
    print("LOG: Начало API запроса 1")
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com")
    print(f"LOG: Конец API запроса 1, статус: {response.status_code}")
    return response

async def api_request_2():
    print("LOG: Начало API запроса 2")
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"LOG: Конец API запроса 2, статус: {response.status_code}")
    return response

async def sql_request_1():
    print("LOG: Начало SQL запроса 1")
    async with session() as conn:  # Открыл сессию ЗДЕСЬ
        w1 = await crud_Warehouse.create(conn, name="Склад", address="Москва", capacity=1000)
        print(f"LOG: Конец SQL запроса 1, создан: {w1}")
        return w1

async def sql_request_2():
    print("LOG: Начало SQL запроса 2")
    async with session() as conn:
        warehouses = await crud_Warehouse.read_all(conn)  # ← Передай conn!
        print(f"LOG: Конец SQL запроса 2, найдено: {len(warehouses)} записей")
        return warehouses

async def main():
    start = time.time()

    tasks = []
    for i in range(35):
        tasks.append(api_request_1())
        tasks.append(api_request_2())
        tasks.append(sql_request_1())
        tasks.append(sql_request_2())

    await asyncio.gather(*tasks)

    end = time.time()
    print(f"\nАСИНХРОННО (140 запросов): {end - start} секунд")


asyncio.run(main())