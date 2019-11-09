from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.usuario import Base, Usuario
from getpass import getuser


class UsuariosData(object):
    def __init__(self):
        engine = create_engine('sqlite:///C:\\Users\\' +
                               getuser() + '\\Desktop\\RecetasDB.db', echo=True)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def get_one(self, id_usuario):
        try:
            return self.session.query(Usuario).filter_by(id_usuario=id_usuario).first()
        except:
            return None

    def get_one_by_credentials(self, user, password):
        try:
            return self.session.query(Usuario).filter_by(usuario=user, contrasenia=password).first()
        except:
            return None

    def get_one_by_user(self, user):
        try:
            return self.session.query(Usuario).filter_by(usuario=user).first()
        except:
            return None

    def get_all(self):
        return self.session.query(Usuario).all()        

    def remove_all(self):
        try:
            self.session.query(Usuario).delete()
            return True
        except:
            return False

    def insert(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def remove(self, id_usuario):
        user = self.get_one(id_usuario)
        if user is None:
            return False
        else:
            self.session.delete(user)
            self.session.commit()
            return True

    def update(self, user):
        user_enc = self.get_one(user.id_usuario)
        user_enc.usuario = user.usuario
        user_enc.contrasenia = user.contrasenia
        user_enc.email = user.email
        user_enc.recetas_favoritas = user.recetas_favoritas
        self.session.commit()
        return user_enc
