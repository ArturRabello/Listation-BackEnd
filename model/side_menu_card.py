from datetime import datetime
from typing import Union
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .modal import Modal


class SideMenuCard(Base):
    __tablename__ = 'sideMenuCard'

    id = Column("pk_side_menu_card", String(28), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um produto.
    # Aqui está sendo definido a coluna 'produto' que vai guardar
    # a referencia ao produto, a chave estrangeira que relaciona
    # um produto ao comentário.

    modal = relationship('Modal', backref='sideMenuCardRef')
    
    def __init__(self, id:str, name:str, description:str,
                 data_insercao:Union[DateTime, None] = None):
        
        self.id = id
        self.name = name
        self.description = description
        self.data_insercao = data_insercao

    def add_modal(self, modal: Modal):
        self.modal.append(modal)