from app.v1.models.user_model import User

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User])