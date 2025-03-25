

import datetime
from sqlalchemy import DateTime, String, column
from model import base

class SideMenuCard(base):
    __tablename__ = 'side_menu_card'

    """
        Cria um card do menu lateral

        arguments:
            id {string} -- id do card
            name {string} -- nome do card
            description {string} -- descrição do card

    """

    id = column("pk_CardsMenu", String(28), primary_key=True)
    name = column(String(12))
    description = column(String(12))
    date_insert = column(DateTime, default=datetime.now())

    def __init__(self, id, name, description):
        self.id = id,
        self.name = name,
        self.description = description
 