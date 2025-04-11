from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from model.side_menu_card import SideMenuCard



class SideMenuCardSchema(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str = "dawdk3123ad"
    name: str = "Receitas"
    description: str = "Doces"

class SideMenuCardSearchSchema(BaseModel):
    id: str = "dawdk3123ad"

class ListingSideMenuCardSchema(BaseModel):
    sideMenuCards: List[SideMenuCardSchema]

def to_present_sideMenuCards(sideMenuCards: List[SideMenuCard]):
    result = []
    for card in sideMenuCards:
        result.append({
            "id": card.id,
            "name": card.name,
            "description": card.description
        })
    return {"SideMenuCard": result}

class SideMenuCardViewSchema(BaseModel):
    id: str
    name: str
    description: str
    

def to_present_sideMenuCard(sideMenuCard: SideMenuCard):
    return {
        "id": sideMenuCard.id,
        "name": sideMenuCard.name,
        "description": sideMenuCard.description,
        "total_modal" : len(sideMenuCard.modals),
        "modal": [{"id": modal.id, "name": modal.name} for modal in sideMenuCard.modals]
    }
