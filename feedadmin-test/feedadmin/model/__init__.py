"""The application's model objects"""
from feedadmin.model.meta import Session, Base, Base2


def init_model(engine, engine2):
    """Call me before using any of the tables or classes in the model"""
    #Session.configure(bind=engine)
    meta.Base.metadata.bind = engine
    meta.Base2.metadata.bind = engine2
