from sqlalchemy import select

class AsyncCRUD:
    def __init__(self, model):
        self.model = model

    async def create(self, conn, **kwargs):
        obj = self.model(**kwargs)
        conn.add(obj)
        await conn.commit()
        await conn.refresh(obj)
        return obj

    async def read(self, conn, id):
        return await conn.get(self.model, id)

    async def read_all(self, conn):
        stmt = select(self.model).order_by(self.model.id)
        result = await conn.execute(stmt)
        return result.scalars().all()

    async def update(self, conn, id, **kwargs):
        obj = await conn.get(self.model, id)
        if not obj:
            return None
        for k, v in kwargs.items():
            setattr(obj, k, v)
        await conn.commit()
        await conn.refresh(obj)
        return obj

    async def delete(self,conn, id):
        obj = await conn.get(self.model, id)
        if not obj:
            return None
        await conn.delete(obj)
        await conn.commit()
        return obj