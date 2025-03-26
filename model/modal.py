import datetime
from sqlalchemy import DateTime, ForeignKey, String, Column
from sqlalchemy.orm import relationship
from model import Base, ModalCard


class Modal(Base):
    __tablename__ = 'modal'

    id = Column("pk_modal", String(28), primary_key=True)
    name = Column(String(26))
    description = Column(String(26))
    data_insert = Column(DateTime, default=datetime.now())
    menu_card = Column(String(28), ForeignKey("side_menu_card.pk_menu_card"), nullable=False)

    modal_card = relationship("Modal_Card")

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


    def add_modal_card(self, modal_card: ModalCard):
        self.card_table.append(modal_card)


