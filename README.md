# gestion_user
CRUD fastapi for user

run:
uvicorn main:app --reload

open the browser and:
-- http://localhost:8000/user
-- http://localhost:8000/docs

Pasos previos:
-- Crear base de datos.
    Connectarse a la base de datos y ejecutar:
    CREATE DATABASE users WITH OWNER = postgres ENCODING = 'UTF8' CONNECTION LIMIT = -1;
-- Crear las tablas
    Desde consola ejecutar py
    dentro del interprete de python ejecutar ==> from app.v1.scripts.create_tables import create_tables
                                                 create_tables()


Docker
-- Crear la imagen:
    docker image build --tag gestion-user-image .
-- Ejecutar contenedor
    docker container run --publish 8010:80 --name gestion-user-container gestion-user-image

Acceso desde el browser
    http://localhost:8010/docs        