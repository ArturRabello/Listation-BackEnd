from typing import List
from pydantic import BaseModel, ConfigDict

from model.modal import Modal

class ModalSchema(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str = "lflefs21321"
    name: str = "Bolos"
    description: str = "Receitas de bolos"
    side_menu_card_id: str = "dawdk3123ad"


class ModalSearchSchema(BaseModel):
    id: str = "lflefs21321"

class GetAllModalSchema(BaseModel):
    side_menu_card_id: str = "dawdk3123ad"

class ListingModalSchema(BaseModel):
    ModalSchema: List[ModalSchema]

def to_present_modals(modals: List[Modal]):
    result = []
    for modal in modals:
        result.append({
            "id": modal.id,
            "name": modal.name,
            "description": modal.description,
            "side_menu_card_id": modal.side_menu_card_id,
        })
    return {"Modals": result}

class ModalViewSchema(BaseModel):
    id: str
    name: str
    description: str
    

def to_present_modal(modal: Modal):
    return {
        "id": modal.id,
        "name": modal.name,
        "description": modal.description,
        "total_modalCard": len(modal.modal_cards),
        "modalCard": [{"id": modalCard.id, "name": modalCard.name} for modalCard in modal.modal_cards]
    }
