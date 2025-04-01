from pydantic import BaseModel, ConfigDict
from typing import Optional, List

from model.modal_card import ModalCard

class ModalCardSchema(BaseModel):

    """  Define como um modalCard será estruturado
    """
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str = "dwadi2193ad"
    name: str = "Chocolate"
    description: str ="Receita de um bolo de chocolate"
    modal_id: str = "lflefs21321"

class ModalCardSearchSchema(BaseModel):
    id: str = "dwadi2193ad"

class GetAllModalCardSchema(BaseModel):
    modal_id: str = "lflefs21321"

class ModalCardViewSchema(BaseModel):
    name: str = "Chocolate"
    description: str ="Receita de um bolo de chocolate"

class ListingModalCardSchema(BaseModel):
    modalCards: List[ModalCardSchema]

def to_present_modalCards(modalCard: List[ModalCard]):

    
    result=[]
    for modalCards in modalCard:
        result.append({
            "id": modalCards.id,
            "name": modalCards.name,
            "description": modalCards.description
        })

    return {"ModalCard": result}


class ModalCardViewSchema(BaseModel):

    id: str = "dwadi2193ad"
    name: str = "Chocolate"
    description: str ="Receita de um bolo de chocolate"


def to_present_modalCard(modalCard: ModalCard):
    return {
        "id": modalCard.id,
        "name": modalCard.name,
        "description": modalCard.description
    }