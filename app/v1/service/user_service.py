from collections import UserDict
from fastapi import HTTPException, Path, status

from passlib.context import CryptContext

from app.v1.models.user_model import User as UserModel
from app.v1.schemas import user_schema
from app.v1.service.auth_service import get_password_hash

def create_user(user: user_schema.UserRegister):

    print('user: {}'.format(user))
    get_user = UserModel.filter((UserModel.correo == user.correo) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        correo=user.correo,
        password=get_password_hash(user.password),
        direccion=user.direccion,
        telefono=user.telefono
    )

    db_user.save()
    return build_user_schema(db_user=db_user)


def get_users():
    users = UserModel.select()
    list_user = []
    for user in users:
        list_user.append(build_user_schema(user))
    print("User: {}".format(users))
    return list_user

def get_user(user_id: int):
    get_user = UserModel.filter((UserModel.id == user_id)).first()

    if not get_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return build_user_schema(get_user)

def update_user(user_id: int, user_modify: user_schema.UserRegister):
    get_user = UserModel.filter((UserModel.id == user_id)).first()

    if not get_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    print("user old: {}".format(get_user))
    get_user.username = user_modify.username
    get_user.correo = user_modify.correo
    get_user.password = get_password_hash(user_modify.password)
    get_user.direccion = user_modify.direccion
    get_user.telefono = user_modify.telefono
    print("user new: {}".format(get_user))

    get_user.save()
    return build_user_schema(db_user=get_user)

def delete_user(user_id: int):
    get_user = UserModel.filter((UserModel.id == user_id)).first()
    print("Ejecuto el delete para: {}".format(user_id))

    if not get_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    get_user.delete_instance()
    

def build_user_schema(db_user: UserModel):
    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        correo = db_user.correo,
        direccion = db_user.direccion,
        telefono = db_user.telefono
    )

