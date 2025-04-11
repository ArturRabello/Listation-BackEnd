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

def to_present_modalCards(modalCards: List[ModalCard]):

    result=[]
    for modalCard in modalCards:
        result.append({
            "id": modalCard.id,
            "name": modalCard.name,
            "description": modalCard.description,
            "modal_id": modalCard.modal_id
        })

    return {"modalCards": result}


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