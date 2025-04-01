

from typing import Union
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base
from .modal_card import ModalCard



class Modal(Base):
    __tablename__ = 'modal'

    id = Column("pk_modal", String(28), primary_key=True)
    name = Column(String)
    description = Column(String)
    data_insercao = Column(DateTime, default=datetime.now())
    side_menu_card_id = Column(String, ForeignKey('sideMenuCard.pk_side_menu_card'), nullable=False)
    modal_card = relationship('ModalCard', backref='modalRef')

    def __init__(self, id:str, name:str, description:str,
                 data_insercao:Union[DateTime, None] = None, side_menu_card_id:str = None):
        
        self.id = id
        self.name = name
        self.description = description
        self.data_insercao = data_insercao
        self.side_menu_card_id = side_menu_card_id
    def add_modal_card(self, modal_card:ModalCard):
        self.modal_card.append(modal_card)
    
