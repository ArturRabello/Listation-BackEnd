from pydantic import BaseModel
from typing import Optional, List

from model.side_menu_card import SideMenuCard
from schemas.modal import ModalSchema

class SideMenuCardSchema(BaseModel):

    """ Define como um SideMenuCard será estruturado
    """

    id: str = "1ksj22kdk234kalwl"
    name: str = "Receitas"
    description: str = "Receitas faceis"

class SideMenuCardSearchSchema(BaseModel):

    id: str = "1ksj22kdk234kalwl"

class SideMenuCardViewSchema(BaseModel):

    name: str = "Receitas"
    description: str = "Receitas faceis"

class SideMenuCardDelSchema(BaseModel):
    id: str = "1ksj22kdk234kalwl"

class listingSideMenuCard(BaseModel):

    sideMenuCards: List[SideMenuCardSchema]

def to_present_sideMenuCard(sideMenuCards: List[SideMenuCard]):

    result=[]
    for card in sideMenuCards:
        result.append({
            "id": card.id,
            "name": card.name,
            "description": card.description
        })

    return {"sideMenuCard": result}


class sideMenuCardViewSchema(BaseModel):

    id: str = "1ksj22kdk234kalwl"
    name: str = "Receitas"
    description: str = "Receitas faceis"
    total_modals: int = 1
    modals: List[ModalSchema]


def apresenta_sideMenuCard(sideMenuCard: SideMenuCard):
    return {
        "id": modal.id,
        "name": modal.name,
        "description":  modal.description
        "total_modals": len(modal.modal_cards)
        "modals": [{"texto": m.texto} for m in modal.modal_cards]
    }