
import datetime
from sqlalchemy import DateTime, ForeignKey, String, Column

from model import Base



class ModalCard(Base):
    __tablename__ = "modal_card"

    id = Column("pk_modal_card", String(28), primary_key=True)
    name = Column(String(12))
    img_url = Column(String)
    description = Column(String)
    date_insert = Column(DateTime, default=datetime.now())
    modal = Column(String(28), ForeignKey("modal.pk_modal"), nullable=False)

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

