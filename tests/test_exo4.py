import pytest

from ..exo4.models import User
from ..exo4.user_service import create_user


def test_create_user(db_session):
    create_user(
        db_session=db_session,
        user_email="toto@mail.com",
        user_name="toto",
        user_age=18
    )

    users = db_session.query(User).all()

    assert len(users) == 1
    assert users[0].email == "toto@mail.com"
    assert users[0].name == "toto"
    assert users[0].age == 18


def test_create_user_fail(db_session):
    create_user(
        db_session=db_session,
        user_email="toto@mail.com",
        user_name="toto",
        user_age=18
    )

    with pytest.raises(Exception):
        create_user(
            db_session=db_session,
            user_email="toto@mail.com",
            user_name="tata",
            user_age=23
        )
