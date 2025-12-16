import asyncio
import time

from database import engine, session
from models import Base, Warehouse, Item, Order
from crud import AsyncCRUD

start_time = time.time()

print("Очистка базы")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
print("База очищена!")

crud_Warehouse = AsyncCRUD(session, Warehouse)
crud_Item = AsyncCRUD(session, Item)
crud_Order = AsyncCRUD(session, Order)

async def main():
    w1 = await crud_Warehouse.create(name="Склад №1", address="Москва, ул. Ленина 10", capacity=1000)
    w2 = await crud_Warehouse.create(name="Склад №2", address="СПб, Невский проспект 25", capacity=1500)
    w3 = await crud_Warehouse.create(name="Склад №3", address="Казань, ул. Баумана 5", capacity=800)

    i1 = await crud_Item.create(name="Молоток", price=500.0, warehouse_id=1)
    i2 = await crud_Item.create(name="Отвёртка", price=200.0, warehouse_id=1)
    i3 = await crud_Item.create(name="Дрель", price=3000.0, warehouse_id=2)
    i4 = await crud_Item.create(name="Пила", price=1500.0, warehouse_id=2)
    i5 = await crud_Item.create(name="Гвозди", price=50.0, warehouse_id=3)

    o1 = await crud_Order.create(amount=1000.0, item_id=1)
    o2 = await crud_Order.create(amount=3200.0, item_id=3)

    print("\nREAD")
    it1 = await crud_Item.read(1)
    it2 = await crud_Order.read(2)
    print(it1, it2)

    print("\nREAD ALL")
    warehouses = await crud_Warehouse.read_all()
    for w in warehouses: print(w)

    print("\nUPDATE")
    it_upd = await crud_Item.update(1, price=600.0, warehouse_id=2)
    print(f"Обновлено: {it_upd}")

    print("\nDELETE")
    print(f"Удаляется: {await crud_Item.read(5)}")
    it_del = await crud_Item.delete(5)
    print(f"Удалено!")

asyncio.run(main())

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")