from sqlalchemy import select

class CRUD:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj

    def read(self, id):
        return self.session.get(self.model, id)

    def read_all(self):
        stmt = select(self.model).order_by(self.model.id)
        return self.session.execute(stmt).scalars().all()

    def update(self, id, **kwargs):
        obj = self.session.get(self.model, id)
        if not obj:
            return None
        for k, v in kwargs.items():
            setattr(obj, k, v)
        self.session.commit()
        return obj

    def delete(self, id):
        obj = self.session.get(self.model, id)
        if not obj:
            return None
        self.session.delete(obj)
        self.session.commit()
        return obj