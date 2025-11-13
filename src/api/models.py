from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    uuid_contraseña: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f'{self.email}'
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }

class Perfil(db.Model):
    __tablename__ = 'perfil'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    foto: Mapped[str] = mapped_column(String(255), nullable=True)
    presentacion: Mapped[str] = mapped_column(String(250), nullable=True)
    telefono: Mapped[str] = mapped_column(String(20), nullable=True)
    edad: Mapped[int] = mapped_column(nullable=True)
    ciudad: Mapped[str] = mapped_column(String(80), nullable=True)
    genero: Mapped[str] = mapped_column(String(80), nullable=True)
    twitter: Mapped[str] = mapped_column(String(80), nullable=True)
    facebook: Mapped[str] = mapped_column(String(80), nullable=True)
    instagram: Mapped[str] = mapped_column(String(80), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


    def __repr__(self):
        return f'{self.nombre}'
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "foto": self.foto,
            "presentacion": self.presentacion,
            "telefono": self.telefono,
            "edad": self.edad,
            "ciudad": self.ciudad,
            "genero": self.genero,
            "twitter": self.twitter,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "user_id": self.user_id
        }

class Tareas(db.Model):
    __tablename__ = 'tareas'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(80), nullable=False)
    evento_id: Mapped[int] = mapped_column(ForeignKey('evento.id'))

    fecha: Mapped[str] = mapped_column(DateTime, nullable=True)
    descripcion: Mapped[str] = mapped_column(String(250), nullable=True)
    Prioridad_id: Mapped[int] = mapped_column(ForeignKey('prioridad.id'))

    estado_id: Mapped[int] = mapped_column(ForeignKey('estado.id'))

    imagen: Mapped[str] = mapped_column(String(255), nullable=True)


    def __repr__(self):
        return f'{self.titulo}'
    
    def serialize(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "imagen": self.imagen,
            "descripcion": self.descripcion,
            "fecha": self.fecha,
            "evento_id": self.evento_id,
            "prioridad_id": self.Prioridad_id,
            "estado_id": self.estado_id,
        }
    
class Estado(db.Model):
    __tablename__ = 'estado'
    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(20), nullable=True)

    def __repr__(self):
        return f'{self.tipo}'
    
    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo
        }
    
class Evento(db.Model):
    __tablename__ = 'evento'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(20), nullable=False)
    lugar: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f'{self.titulo}'
    
    def serialize(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "lugar": self.lugar
        }
    
class Prioridad(db.Model):
    __tablename__ = 'prioridad'
    id: Mapped[int] = mapped_column(primary_key=True)
    nivel: Mapped[str] = mapped_column(String(20), nullable=False)

    def __repr__(self):
        return f'{self.nivel}'
    
    def serialize(self):
        return {
            "id": self.id,
            "nivel": self.nivel,
        }    

class Grupo(db.Model):
    __tablename__ = 'grupo'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categoria.id'))

    fecha: Mapped[str] = mapped_column(DateTime, nullable=True)
    codigo: Mapped[str] = mapped_column(Integer, nullable=True)

    def __repr__(self):
        return f'{self.nombre}'
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria_id": self.categoria_id,
            "fecha": self.fecha,
            "codigo": self.codigo
        }
    
class Categoria(db.Model):
    __tablename__ = 'categoria'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)

    def __repr__(self):
        return f'{self.nombre}'
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
    
class Clan(db.Model):
    __tablename__ = 'clan'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    grupo_id: Mapped[int] = mapped_column(ForeignKey('grupo.id'))


    def __repr__(self):
        return f'User = {self.user_id}'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "grupo_id": self.grupo_id
        }
    
class Mision(db.Model):
    __tablename__ = 'mision'
    id: Mapped[int] = mapped_column(primary_key=True)
    tareas_id: Mapped[int] = mapped_column(ForeignKey('tareas.id'))

    grupo_id: Mapped[int] = mapped_column(ForeignKey('grupo.id'))


    def __repr__(self):
        return f'Grupo = {self.grupo_id}'
    
    def serialize(self):
        return {
            "id": self.id,
            "tareas_id": self.tareas_id,
            "grupo_id": self.grupo_id
        }
    
class TareasAsignadas(db.Model):
    __tablename__ = 'tareas_asignadas'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    tareas_id: Mapped[int] = mapped_column(ForeignKey('tareas.id'))


    def __repr__(self):
        return f'User = {self.user_id}'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "tareas_id": self.tareas_id
        }