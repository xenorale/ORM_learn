import sys
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

sys.stdout.reconfigure(encoding='utf-8')

class Base(DeclarativeBase):
    pass

class Warehouse(Base):
    __tablename__ = 'Warehouses'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str]
    capacity: Mapped[int]
    items: Mapped[list["Item"]] = relationship(back_populates="warehouse")
    def __repr__(self):
        return f'Warehouse(id={self.id}, name={self.name}, address={self.address}, capacity={self.capacity})'

class Item(Base):
    __tablename__ = 'Items'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("Warehouses.id"))
    warehouse: Mapped["Warehouse"] = relationship(back_populates="items")

    def __repr__(self):
        return f'Item(id={self.id}, name={self.name}, price={self.price})'

class Order(Base):
    __tablename__ = 'Orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(default=0)
    item_id: Mapped[int] = mapped_column(ForeignKey("Items.id"))
    item: Mapped["Item"] = relationship()
    def __repr__(self):
        return f'Order(id={self.id}, amount={self.amount})'