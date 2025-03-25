import datetime
from sqlalchemy import DateTime, String, column
from model.base import Base


class Table(Base):
    __tablename__ = 'table'

    id = column("pk_Table", String(12), primary_key=True)
    name = column(String(26))
    description = column(String(26))
    data_insert = column(DateTime, default=datetime.now())

    def __init__(self, id, name, description):
        self.id = id,
        self.name = name,
        self.description = description

        
