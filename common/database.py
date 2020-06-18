from sqlalchemy import MetaData


def dbconnect():
    from app import db
    SQLALCHEMY_ENGINE_OPTIONS = {
        "max_overflow": 15,
        "pool_pre_ping": True,
        "pool_recycle": 60 * 60,
        "pool_size": 30,
    }
    dbseesion = db.session
    DBase = db.Model
    metadata = MetaData(bind=db.engine)
    return (dbseesion, metadata, DBase)
