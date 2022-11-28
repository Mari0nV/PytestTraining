
from sqlalchemy.orm import Session
from .models import User


def create_user(db_session: Session, user_email: str, user_name: str, user_age: int):
    user_already_exists = db_session.query(User).filter(
        User.email == user_email).one_or_none()

    if user_already_exists is not None:
        raise Exception(f"User with email {user_email} already exists.")

    new_user = User(
        email=user_email,
        name=user_name,
        age=user_age
    )
    db_session.add(new_user)
    db_session.flush()

    return new_user
