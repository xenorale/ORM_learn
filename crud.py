from sqlalchemy import select

class AsyncCRUD:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    async def create(self, **kwargs):
        async with self.session() as conn:
            obj = self.model(**kwargs)
            conn.add(obj)
            await conn.commit()
            await conn.refresh(obj)
            return obj

    async def read(self, id):
        async with self.session() as conn:
            return await conn.get(self.model, id)

    async def read_all(self):
        async with self.session() as conn:
            stmt = select(self.model).order_by(self.model.id)
            result = await conn.execute(stmt)
            return result.scalars().all()

    async def update(self, id, **kwargs):
        async with self.session() as conn:
            obj = await conn.get(self.model, id)
            if not obj:
                return None
            for k, v in kwargs.items():
                setattr(obj, k, v)
            await conn.commit()
            await conn.refresh(obj)
            return obj

    async def delete(self, id):
        async with self.session() as conn:
            obj = await conn.get(self.model, id)
            if not obj:
                return None
            await conn.delete(obj)
            await conn.commit()
            return obj