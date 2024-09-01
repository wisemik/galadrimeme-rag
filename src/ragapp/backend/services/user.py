from sqlmodel import Session, select

from backend.database import DB
from backend.models.orm.chat_request import UserChatRequest
from backend.models.user_info import UserInfo


def get_user(id: str, db):
    return db.query(UserInfo).filter(UserInfo.user_id == id).first()


def update(data: UserInfo, db: Session, id: str):
    user = db.query(UserInfo).filter(UserInfo.user_id == id).first()
    user.roles = data.roles

    db.add(user)
    db.commi()
    db.refresh(user)

    return user
