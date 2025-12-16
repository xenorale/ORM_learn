from database import engine, session_sync
from models import Base, Warehouse, Item, Order
from sync_crud import CRUD

print("Очистка базы")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("База очищена!")

crud_Warehouse = CRUD(session_sync, Warehouse)
crud_Item = CRUD(session_sync, Item)
crud_Order = CRUD(session_sync, Order)

w1 = crud_Warehouse.create(name="Склад №1", address="Москва, ул. Ленина 10", capacity=1000)
w2 = crud_Warehouse.create(name="Склад №2", address="СПб, Невский проспект 25", capacity=1500)
w3 = crud_Warehouse.create(name="Склад №3", address="Казань, ул. Баумана 5", capacity=800)

i1 = crud_Item.create(name="Молоток", price=500.0, warehouse_id=1)
i2 = crud_Item.create(name="Отвёртка", price=200.0, warehouse_id=1)
i3 = crud_Item.create(name="Дрель", price=3000.0, warehouse_id=2)
i4 = crud_Item.create(name="Пила", price=1500.0, warehouse_id=2)
i5 = crud_Item.create(name="Гвозди", price=50.0, warehouse_id=3)

o1 = crud_Order.create(amount=1000.0, item_id=1)
o2 = crud_Order.create(amount=3200.0, item_id=3)

print("\nREAD")
it1 = crud_Item.read(1)
it2 = crud_Order.read(2)
print(it1, it2)

print("\nREAD ALL")
warehouses = crud_Warehouse.read_all()
for w in warehouses: print(w)

print("\nUPDATE")
it_upd = crud_Item.update(1, price=600.0, warehouse_id=2)
print(f"Обновлено: {it_upd}")

print("\nDELETE")
print(f"Удаляется: {crud_Item.read(5)}")
it_del = crud_Item.delete(5)
print(f"Удалено!")