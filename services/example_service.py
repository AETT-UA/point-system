from loguru import logger
from schemas.example_user_schemas import UserCreate
from sqlalchemy.orm import Session
from utils.DBEngine import DBEngine
from models.example import User  # This is your SQLAlchemy model

db = DBEngine()

def insert_user(user_data: UserCreate) -> User:
    with Session(db.engine) as session:
        session.begin()
        try:
            new_user = User(**user_data.dict())
            session.add(new_user)
            session.commit()
            session.refresh(new_user)  
        except Exception as e:
            logger.error(e)
            session.rollback()
            raise
        return new_user

