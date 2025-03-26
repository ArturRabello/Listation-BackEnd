from pydantic import BaseModel
from typing import Optional, List

from model.modal_card import ModalCard
from 

class ModalCardSchema(BaseModel):

    """  Define como um modalCard será estruturado
    """

    id: str = "dwadi2193ad"
    name: str = "Chocolate"
    description: str ="Receita de um bolo de chocolate"

class ModalCardSearchSchema(BaseModel):
    id: str = "dwadi2193ad"

class ModalCardViewSchema(BaseModel):
    name: str = "Chocolate"
    description: str ="Receita de um bolo de chocolate"

class ModalDelSchema(BaseModel):
    id: str = "dwadi2193ad"

class listingModalSchema(BaseModel):
    modalCards: List[ModalCard]

def to_present_ModalCard(modalCards: List[ModalCard]):

    result=[]
    for ModalCard in ModalCards:
        result.append({
            "id": ModalCard.id,
            "name": ModalCard.name,
            "description": ModalCard.description
        })

    return {"ModalCard": result}


class ModalCardViewSchema(BaseModel):

    id: str = "1ksj22kdk234kalwl"
    name: str = "Chocolate"
    description: str ="Receita de um bolo de chocolate"


def apresenta_modalCard(modalCard: ModalCards):
    return {
        "id": modalCard.id,
        "name": modalCard.name,
        "description": modalCard.description
    }