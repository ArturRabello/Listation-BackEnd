from datetime import datetime
from typing import Union
from sqlalchemy import Column, DateTime, ForeignKey, String

from .base import Base


class ModalCard(Base):
    __tablename__ = 'ModalCard'

    id = Column("pk_modal_card", String(28), primary_key=True)
    name = Column(String)
    description = Column(String)
    data_insercao = Column(DateTime, default=datetime.now())
    modal_id = Column(String, ForeignKey('modal.pk_modal'), nullable=False)

    def __init__(self, id:str, name:str, description:str, data_insercao:Union[DateTime, None] = None, modal_id:str = None):
        self.id = id
        self.name = name
        self.description = description
        self.data_insercao = data_insercao
        self.modal_id = modal_id
