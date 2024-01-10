from datetime import datetime
import peewee

from app.v1.utils.db import db

class User(peewee.Model):
    id = peewee.AutoField()
    username = peewee.CharField(max_length=20, unique=True, index=True)
    password = peewee.CharField(max_length=100)
    correo = peewee.CharField(max_length=100, unique=True, index=True)
    direccion = peewee.CharField(max_length=150, null=True)
    telefono = peewee.CharField(max_length=9, null=True)
    createdAt = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db