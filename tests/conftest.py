import pytest
import os
import shutil

from ..exo3.game_status import GameStatus
from ..exo4.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


TEST_FILE_FOLDER = "test_files"


@pytest.fixture
def game_status():
    status = {
        "place": "forest.north",
        "day": 1,
        "alive": True
    }
    file_path = os.path.join(TEST_FILE_FOLDER, "status.json")
    return GameStatus(status=status, file_path=file_path)


@pytest.fixture(scope="session")
def generated_test_folder():
    if not os.path.exists(TEST_FILE_FOLDER):
        os.mkdir(TEST_FILE_FOLDER)
    yield
    shutil.rmtree(TEST_FILE_FOLDER)


@pytest.fixture(scope="session")
def connection():
    # The URL should be constructed from environment variables
    # Do not store your credentials in conftest.py!
    engine = create_engine(
        "postgresql://<user>:<pwd>@<host>:<port>/<db_name>")
    return engine.connect()


@pytest.fixture(scope="session")
def setup_database(connection):
    Base.metadata.bind = connection
    Base.metadata.create_all()

    yield

    Base.metadata.drop_all()


@pytest.fixture
def db_session(setup_database, connection):
    transaction = connection.begin()

    yield sessionmaker(bind=connection)()

    transaction.rollback()
