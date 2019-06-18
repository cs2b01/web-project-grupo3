from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector


class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    username = Column(String(12))


class Producto(connector.Manager.Base):
    __tablename__ = 'producto'
    id = Column(Integer, Sequence('producto_id_seq'), primary_key=True)
    codigo = Column(Integer)
    nombre = Column(String(50))
    marca = Column(String(50))
    cantidad  =  Column(Integer)
    precio = Column(Integer)


class Compras(connector.Manager.Base):
    __tablename__ = 'compras'
    id = Column(Integer, Sequence('compras_id_seq'), primary_key=True)
    usercomprador_id = Column(Integer, ForeignKey('users.id'))
    producto_id = Column(Integer, ForeignKey('producto.id'))
    usercomprador = relationship(User, foreign_keys=[usercomprador_id])
    producto = relationship(Producto, foreign_keys=[producto_id])
    satisfaccion = Column(Integer)
class Mensaje(connector.Manager.Base):
    __tablename__ = 'mensaje'
    id = Column(Integer, Sequence('mensaje_id_seq'), primary_key=True)
    nombre = Column(String(50))
    email = Column(String(50))
    phone = Column(Integer)
    message = Column(String(200))
