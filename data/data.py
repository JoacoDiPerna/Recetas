from sqlalchemy.ext.declarative import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True,unique=True, autoincrement=True)
    usuario = Column(String(250), nullable=False)
    contrasenia = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    recetas_favoritas = relationship('RecetaFavorita', back_populates='usuario')

class RecetaFavorita(Base):
    __tablename__ = 'recetas_favoritas'
    id_receta_favorita = Column(Integer, primary_key=True,unique=True, autoincrement=True)
    url = Column(String(250), nullable=False)
    descripcion = Column(String(500), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    usuario = relationship('Usuario', back_populates='recetas_favoritas')
    comentario = Column(String(250))
    fecha_hora = Column(DateTime, nullable=False)
