
import datetime
from sqlalchemy import DateTime, ForeignKey, String, column



class CardTable:
    __tablename__ = "card_table"

    id = column("pk_CardTable", String(28), primary_key=True)
    name = column(String(12))
    description = column(String(12))
    date_insert = column(DateTime, default=datetime.now())
    table = column(String(28), ForeignKey("table.pk_Table"),nullable=False) 

    def __init__(self, id, name, description):
        self.id = id,
        self.name = name,
        self.description = description

