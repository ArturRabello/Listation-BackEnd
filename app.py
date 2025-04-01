

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, SideMenuCard, Modal, ModalCard

from schemas import *
from flask_cors import CORS
from logger import logger

Info = Info(title ="LisTation", version = "1.0.0")

app = OpenAPI(__name__, info=Info)
CORS(app)

home_tag = Tag(name="documentation", description="Seleção de documentação da api")
side_menu_card_tag = Tag(name="SideMenuCard", description="Oferece operação de criação, remoção e adição de SideMenuCards")
modal_tag = Tag(name="modal", description="fornece operação de criação, remoção e adição de modalS")
modal_card_tag = Tag(name="modal_card", description="fornece operação de criação, remoção e adição de modal_cards")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

# ----------------------------SIDE_MENU_CARD---------------------------
@app.post('/side_menu_card/create', tags=[side_menu_card_tag],
            responses={"200": SideMenuCardViewSchema, "400": ErrorSchema, "409": ErrorSchema})

def add_side_menu_card(form: SideMenuCardSchema):
    """
        Adiciona um novo side_menu_card à base de dados
    
        Retorna uma representação do side_menu_card
    """
    side_menu_card = SideMenuCard(
        id = form.id,
        name = form.name,
        description = form.description
    )
    try:
        session = Session()
        session.add(side_menu_card)
        session.commit()
        return to_present_sideMenuCard(side_menu_card), 200
    
    except IntegrityError as e:
        # tratamento para erro de nome duplicada
        error_msg = f"Card de mesmo id já cadastrado, '{side_menu_card.id}'"
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        error_msg = "Ocorreu um erro"
        return {"mesage": error_msg}, 400
    
    finally:
        session.close()
        
@app.get('/side_menu_cards/getAll', tags=[side_menu_card_tag],
            responses={"200": ListingSideMenuCardSchema, "404": ErrorSchema})

def get_side_menu_cards():
    """ Faz a busca por todos os side_menu_cards cadastrados
        Retorna uma representação da lista de side_menu_card
    """
    try:
        session = Session()
        side_menu_cards = session.query(SideMenuCard).all()

        if not side_menu_cards:
            #sem cards cadastrados
            return {"side_menu_cards": []}, 200
        else:
            print(side_menu_cards)
            return to_present_sideMenuCards(side_menu_cards), 200
    finally:
        session.close()


@app.get('/side_menu_card/get', tags=[side_menu_card_tag],
             responses={"200": SideMenuCardViewSchema, "404": ErrorSchema})
def get_side_menu_card(query: SideMenuCardSearchSchema):
    """ Faz a busca por um side_menu_card a partir de seu id 
        Retorna uma representação do side_menu_card
    """
    try:
        produto_id = query.id
        session = Session()
        side_menu_card = session.query(SideMenuCard).filter(SideMenuCard.id == produto_id).first()
        
        if not side_menu_card:
            error_msg = "Card nao encontrado"
            return {"mesage": error_msg}, 404
        else:
            return to_present_sideMenuCard(side_menu_card), 200
    finally:
        session.close()

@app.delete('/side_menu_card/delete', tags=[side_menu_card_tag],
            responses={"200": SideMenuCardSearchSchema, "404" : ErrorSchema})

def delete_side_menu_card(query: SideMenuCardSearchSchema):
    """ Faz a busca por um side_menu_card e em seguida o remove.
        Retorna uma representação do side_menu_card
    """

    try:
        card_id = unquote(unquote(query.id))
        session = Session()
        side_menu_card = session.query(SideMenuCard).filter(SideMenuCard.id == card_id).delete()
        session.commit()

        if not side_menu_card:
            error_msg = "card nao encontrado"
            logger.debug(f"Erro ao buscar o card ")
            return {"mesage": error_msg}, 404
        else:

            return {"mesage": "Card removido", "id": card_id}, 200
    finally:
        session.close()

# ----------------------------MODAL---------------------------

@app.post('/modal/create', tags=[modal_tag],
          responses={"200":  ModalViewSchema, "400": ErrorSchema, "409": ErrorSchema, "404": ErrorSchema})

def add_modal(form : ModalSchema):  
    """
        Adiciona um modal na base de dados 
        Retorna uma representação do modal
    """

    try:
        session = Session()
        sideMenuCard = session.query(SideMenuCard).filter(SideMenuCard.id == form.side_menu_card_id ).first()

        if not sideMenuCard:
            error_msg = "card não encontrado"
            logger.debug(f"Erro ao buscar o card ")
            return {"mesage": error_msg}, 404
        
        modal = Modal(
            id =  form.id,
            name = form.name,
            description = form.description,
            side_menu_card_id = form.side_menu_card_id


        )

        session.add(modal)
        sideMenuCard.modal.append(modal)
        logger.debug(f"Modal adicionado à sessão")

        session.commit()
        logger.debug(f"Alterações commitadas")

        logger.debug(f"adicioando o modal {modal.name}")
        return to_present_modal(modal), 200
    
    except IntegrityError as e:
        # tratamento para erro de id duplicada
        error_msg = "Modal de mesmo id ja cadastrado, {modal.id}"
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        error_msg = "Ocorreu um erro"
        logger.warning(f"não foi possivel salvar novo item :/")
        return {"mesage":error_msg}, 400
    
    finally:
        session.close()

@app.get ('/modal/getAllMemberSideMenuCard', tags=[modal_tag],
          responses={"200": ListingModalSchema, "404": ErrorSchema})

def get_modals(query: GetAllModalSchema):
    """ Faz a busca por todos os modals cadastrados, contidos no em um determinado side_menu_card
        Retorna uma representação da lista de modals
    """
    try:
        side_menu_card_id = unquote(unquote(query.side_menu_card_id))
        session = Session()

        side_menu_card = session.query(SideMenuCard).filter(SideMenuCard.id == side_menu_card_id).first()
        
        if not side_menu_card:
            error_msg = "Card nao encontrado"
            logger.debug(f"Erro ao buscar o card ")
            return {"mesage": error_msg}, 404
        
        modals = session.query(Modal).filter(Modal.side_menu_card_id == side_menu_card.id).all()
        
        if not modals:
            return {"modals": []}, 200
        else:
            logger.debug(f"{len(modals)} modals coletados")
            return to_present_modals(modals), 200
    finally:
        session.close()

@app.get('/modal/get', tags=[modal_tag],
         responses={"200": ModalViewSchema, "404": ErrorSchema, "400": ErrorSchema})

def get_modal(query: ModalSearchSchema):
    """ Faz a busca por um modal a partir de seu id .
        Retorna uma representação do modal
    """
    try:
        modal_id = query.id
        session = Session()

        modal = session.query(Modal).filter(Modal.id == modal_id ).first()

        if not modal:
            erro_msg = "modal não encontrado"
            logger.debug(f"Erro ao buscar o modal")
            return{"mesage": erro_msg}, 400
        else:
            logger.debug(f"Modal encotrado {modal_id}")
            return to_present_modal(modal), 200
    finally:
        session.close()


@app.delete('/modal/delete', tags=[modal_tag],
            responses={"200": ModalSearchSchema, "404" : ErrorSchema, "400": ErrorSchema})
def delete_modal(query: ModalSearchSchema):
    """
        Faz a busca por um modal e em seguida o remove.
        Retorna uma representação do modal
    """
    try:
        modal_id = unquote(unquote(query.id))
        session = Session()
        
        modal = session.query(Modal).filter(Modal.id == modal_id).first()

        if not modal:
            error_msg = "modal nao encontrado"
            logger.debug(f"Erro ao buscar o modal ")
            return {"mesage": error_msg}, 404
        else:
            logger.debug(f"Modal coletado {modal_id}")
            session.delete(modal)
            session.commit()
            return to_present_modal(modal), 200
    finally:
        session.close()

# ----------------------------MODAL_CARD---------------------------

@app.post('/modal_card/create', tags=[modal_card_tag],
            responses={"200": ModalCardViewSchema, "400": ErrorSchema, "409": ErrorSchema, "404": ErrorSchema})
def add_modal_card(form: ModalCardSchema ):

    """
        Adiciona um modal_card na base de dados
        Retorna uma representação do modal
    """
    try:
        session = Session()
        modal= session.query(Modal).filter(Modal.id == form.modal_id).first()

        if not modal:
            error_msg = "modal não encontrado"
            logger.debug(f"Erro ao buscar o card ")
            return {"mesage": error_msg}, 404
            

        modal_card = ModalCard(
            id=form.id,
            name=form.name,
            description=form.description,
            modal_id=form.modal_id
        )

        session.add(modal_card)
        session.commit()
        return to_present_modalCard(modal_card), 200
    
    except IntegrityError as e:
    # tratamento para erro de id duplicada
        error_msg = f"Card de mesmo id já cadastrado, '{modal_card.id}'"
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        error_msg = "Ocorreu um erro"
        return {"mesage": error_msg}, 400

    finally:
        session.close()


@app.put('/modal_card/update', tags=[modal_card_tag],
         responses={"200": ModalCardViewSchema, "404": ErrorSchema, "400": ErrorSchema})

def update_modal_card(form: ModalCardSchema):
    """
        Faz a busca por um modal_card e em seguida o atualiza.
        Retorna uma representação do modal_card
    """
    try:
        session = Session()
        modal_card = session.query(ModalCard).filter(ModalCard.id == form.id).first()

        if not modal_card:
            error_msg = "modal_card nao encontrado"
            logger.debug(f"Erro ao buscar o card ")
            return {"mesage": error_msg}, 404

        modal_card.name = form.name
        modal_card.description = form.description
        session.commit()
        return to_present_modalCard(modal_card), 200
    finally:
        session.close()

@app.get('/modal_card/getAllMembersModal', tags=[modal_card_tag],
         responses={"200": ListingModalCardSchema, "404": ErrorSchema, "400": ErrorSchema})


def get_modal_cards(query: GetAllModalCardSchema):
    """ Faz a busca por todos os modals_cards cadastrados, contidos no em um determinado side_menu_card.
        Retorna uma representação da lista de modals
    """
    try:
        modal_id = unquote(unquote(query.modal_id))
        session = Session()
        modal = session.query(Modal).filter(Modal.id == modal_id).first()

        if not modal:
            error_msg = "modal não encontrado"
            return {"mesage": error_msg}, 404
        
        modal_cards = session.query(ModalCard).filter(ModalCard.modal_id == modal.id).all()

        if not modal_cards:
            error_msg = "nenhum card foi encontrado"
            return {"mesage": error_msg}, 404
        else:
            return to_present_modalCards(modal_cards), 200
        
    finally:
        session.close()

@app.get('/modal_card/get', tags=[modal_card_tag],
        responses={"200": ModalCardViewSchema, "400": ErrorSchema})

def get_modal_card(query: ModalCardSearchSchema):
    """ 
        Faz a busca por um modal_card, contido em um determinado modal.
        Retorna uma representação do modal
    """
    try:
        modal_card_id = unquote(unquote(query.id))
        session = Session()

        modal_card = session.query(ModalCard).filter(ModalCard.id == modal_card_id).first()

        if not modal_card:
            error_msg ="modal não encontrado"
            logger.debug(f"error ao buscar o modal")
            return {"mesage": error_msg}, 400
        else:
            logger.debug(f"Modal encotrado {modal_card.id}")
            return to_present_modalCard(modal_card), 200
        
    finally:
        session.close()


@app.delete('/modal_card/delete', tags=[modal_card_tag],
            responses={"200": ModalCardSearchSchema, "400": ErrorSchema})

def delete_modal_card(query: ModalCardSearchSchema):
    """
        Faz a busca por um modal_card e em seguida o remove.
        Retorna uma representação do modal
    """
    try:
        modal_card_id = unquote(unquote(query.id))
        session = Session()


        modal_card = session.query(ModalCard).filter(ModalCard.id == modal_card_id).first()

        if not modal_card:
            erro_msg = "modal_card nao encontrado"
            logger.debug(f"Erro ao buscar o modal_card")
            return {"mesage": erro_msg}, 404
        else:
            logger.debug("card não encontrado")
            session.delete(modal_card)
            session.commit()
            return to_present_modalCard(modal_card), 200
            
    finally:
        session.close()