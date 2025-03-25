

import datetime
from sqlalchemy import DateTime, String, Column
from sqlalchemy.orm import relationship
from model import Base, Table

class SideMenuCard(Base):
    __tablename__ = 'side_menu_card'

    """
        modelo de um card do menu lateral

        arguments:
            id {string} -- id do card
            name {string} -- nome do card
            description {string} -- descrição do card

    """

    id = Column("pk_CardsMenu", String(28), primary_key=True)
    name = Column(String(12))
    description = Column(String(12))
    date_insert = Column(DateTime, default=datetime.now())

    tables = relationship("Table")

    def __init__(self, id, name, description):
        self.id = id,
        self.name = name,
        self.description = description

    def add_table(self, table: Table):
 