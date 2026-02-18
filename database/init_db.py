from sqlmodel import create_db_and_tables

from database.models import Shipment
from database.session import engine


def init_db() -> None:
    create_db_and_tables(engine)
