from pydantic import BaseModel
from typing import Optional, List

from model.modal import Modal

class ModalSchema(BaseModel):

    """  Define como um SideMenuCard será estruturado
    """

    id: str = "f3f3sf3221g44fg23"
    name: str = "Bolos"
    description: str = "Receitas de bolos"

class ModalSearchSchema(BaseModel):
    id: str = "f3f3sf3221g44fg23"

class ModalViewSchema(BaseModel):
    name: str = "Bolos"
    description: str = "Receitas de bolos"

class ModalDelSchema(BaseModel):
    id: str = "f3f3sf3221g44fg23"

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
        "id": sideMenuCard.id,
        "name": sideMenuCard.name,
        "description": sideMenuCard.description
        "total_modals": len(sideMenuCard.modal)
        "modals": [{"texto": m.texto} for m in sideMenuCard.modals]
    }