from sqlmodel import Session, create_engine

engine = create_engine("sqlite:///shipments.db", echo=True, connect_args={"check_same_thread": False})


def get_session():
    with Session(engine) as session:
        yield session
