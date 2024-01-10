from typing import List
from fastapi import APIRouter, Path
from fastapi import Depends
from fastapi import status
from fastapi import Body
from app.v1.models.user_model import User

from app.v1.schemas import user_schema
from app.v1.service import user_service

from fastapi.security import OAuth2PasswordRequestForm
from app.v1.service import auth_service
from app.v1.schemas.token_schema import Token

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1", tags=["users"])

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Create a new user in the app

    ### Args
    The app can recive next fields into a JSON
    - correo: A valid email
    - username: Unique username
    - password: Strong password for authentication
    - direccion: dirección postal del usuario
    - telefono: telefono del usuario

    ### Returns
    - user: User info
    """
    return user_service.create_user(user)

@router.post(
    "/login",
    tags=["users"],
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login for access token

    ### Args
    The app can receive next fields by form data
    - username: Your username or email
    - password: Your password

    ### Returns
    - access token and token type
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")

@router.get(
    "/",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=List[user_schema.User],
    dependencies=[Depends(get_db)],
    summary="Get all users"
)
async def read_all_user():
    """
    ## Get all users in the app

    ### Returns
    - user: List User info
    """
    return user_service.get_users()

@router.get(
    "/{user_id}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Get a user"
)
async def read_user(user_id:int):
    """
    ## Get user by id in the app

    ### Args
    The app can receive next fields
    - user_id: id for the primary key user

    ### Returns
    - user: user information
    """
    return user_service.get_user(user_id=user_id)

@router.put(
    "/{user_id}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Update a user by id"
)
async def update_user(user_id: int, user: user_schema.UserRegister = Body(...)):
    """
    ## Update a user register in the app

    ### Args
    - user_id: id for the primary key user
    - The app must recive next fields into a JSON
        - correo: A valid email
        - username: Unique username
        - password: Strong password for authentication
        - direccion: dirección postal del usuario
        - telefono: telefono del usuario

    ### Returns
    - user: User modify info
    """
    return user_service.update_user(user_id=user_id, user_modify=user)

@router.delete(
    "/{user_id}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete a user by id"
)
async def delete_user(user_id: int):
    """
    ## Delete a user register in the app

    ### Args
    - user_id: id for the primary key user

    ### Returns
    - msg: successfully
    """
    user_service.delete_user(user_id=user_id)

    return { 'msg': 'Task has been deleted successfully' }