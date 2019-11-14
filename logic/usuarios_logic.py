from data.usuarios_data import UsuariosData


class UsuarioExistente(Exception):
    pass


class UsuariosLogic(object):
    def __init__(self):
        self.usuario = UsuariosData()

    def get_one(self, id_usuario):
        try:
            return self.usuario.get_one(id_usuario)
        except:
            return None

    def get_one_by_credentials(self, user, password):
        try:
            return self.usuario.get_one_by_credentials(user, password)
        except:
            return None

    def get_one_by_user(self, user):
        try:
            return self.usuario.get_one_by_user(user)
        except:
            return None

    def get_all(self):
        return self.usuario.get_all()

    def insert(self, user):
        if not self.regla_1(user):
            return False
        self.usuario.insert(user)
        return True

    def remove(self, id_usuario):
        usuario = self.get_one(id_usuario)
        if usuario is None:
            return False
        else:
            self.usuario.remove(usuario.id_usuario)
            return True

    def update(self, user):
        self.usuario.update(user)
        return True

    def regla_1(self, user):
        if self.get_one_by_user(user.usuario) is not None:
            raise UsuarioExistente("El usuario ya existe.")
        return True

    def insert(self, user):
        if not self.regla_1(user):
            return False
        self.usuario.insert(user)
        return True

    def remove(self, id_usuario):
        usuario = self.get_one(id_usuario)
        if usuario is None:
            return False
        else:
            self.usuario.remove(usuario.id_usuario)
            return True

    def insert_receta_favorita(self, receta_favorita):
        self.usuario.insert_receta_favorita(receta_favorita)
        return True

    def remove_receta_favorita(self, id_usuario, uri, label):
        receta_favorita = self.usuario.get_one_receta(id_usuario, uri, label)
        if receta_favorita is None:
            return False
        else:
            self.usuario.remove_receta_favorita(id_usuario, uri, label)
            return True
