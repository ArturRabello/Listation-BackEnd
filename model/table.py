import datetime
from sqlalchemy import DateTime, ForeignKey, String, Column
from sqlalchemy.orm import relationship
from model.base import Base, Card_Table


class Table(Base):
    __tablename__ = 'table'

    id = Column("pk_Table", String(28), primary_key=True)
    name = Column(String(26))
    description = Column(String(26))
    data_insert = Column(DateTime, default=datetime.now())
    menu_Card = Column(String(28), ForeignKey("side_menu_card.pk_CardMenu"), nullable=False)

    card_table = relationship("CardTable")

    def __init__(self, id, name, description):
        self.id = id,
        self.name = name,
        self.description = description

    def add_card_table(self, card_table: Card_Table):
        self.card_table.append(card_table)


