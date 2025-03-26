

import datetime
from sqlalchemy import DateTime, String, Column
from sqlalchemy.orm import relationship
from model import base, Modal


class SideMenuCard(base):
    __tablename__ = 'side_menu_card'

    """
        modelo de um card do menu lateral

        arguments:
            id {string} -- id do card
            name {string} -- nome do card
            description {string} -- descrição do card

    """

    id = Column("pk_menu_card", String(28), primary_key=True)
    name = Column(String(12))
    description = Column(String(12))
    date_insert = Column(DateTime, default=datetime.now())
    modals = relationship("Modal")


    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


    def add_modal(self, modal:Modal):
        """
            adiciona uma tabela ao card
        """
        self.tables.append(modal)
 