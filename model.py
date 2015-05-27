# -*- coding: utf-8 -*-. 

"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        
"""
#-------------------------------------------------------------------------------

# Librerias a importar.

from flask                  import Flask
from flask.ext.migrate      import Migrate, MigrateCommand
from flask.ext.sqlalchemy   import SQLAlchemy
from flask.ext.script       import Manager
from sqlalchemy             import CheckConstraint,func

#-------------------------------------------------------------------------------

# Construcción de la base de datos.

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/prueba1"
    # Estructura para realizar la conexión con la base de datos:
    # "postgresql://yourusername:yourpassword@localhost/yournewdb"

db_dir = 'postgresql+psycopg2://postgres:1234@localhost/prueba1'
# Estructrua:
# 'postgresql+psycopg2://user:password@localhost/the_database'  

# Instancia de la aplicación a utilizar.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_dir
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# Instancia de la base de datos a usar.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

# Tabla Pila (Productos):
class Pila(db.Model):
    __tablename__   = 'pila'
    idPila          = db.Column(db.Integer, primary_key = True)
    #nombreProducto  = db.Column(db.String(50), unique = True)
    descripProducto = db.Column(db.String(50), nullable = True)
    pilaAcciones    = db.relationship('Acciones', backref = 'pila', cascade="all, delete, delete-orphan")
    pilaObjetivos   = db.relationship('Objetivo', backref = 'pila', cascade="all, delete, delete-orphan")
    pilaActores     = db.relationship('Actores', backref = 'pila', cascade="all, delete, delete-orphan")
    pilaHistoriaUsuario = db.relationship('Historia_Usuario',backref='pila',cascade = "all, delete, delete-orphan")
    
    def __init__(self, idPila, descripProducto):
        self.idPila  = idPila
        self.descripProducto = descripProducto
        

# Tabla Historia:        
class Historia_Usuario(db.Model):
    __tablename__    = 'historia'
    idHistoria_Usuario       = db.Column(db.Integer, unique=True)
    tipoHistoria_Usuario     = db.Column(db.String(13), nullable = True)
    codigoHistoria_Usuario   = db.Column(db.String(10), primary_key=True,)
    id_Pila_Historia_Usuario = db.Column(db.Integer, db.ForeignKey('pila.idPila'))
    def __init__(self, idHistoria,codigoHistoria,historiaIdPila, tipoHistoria_Usuario= None):
        self.idHistoria_Usuario  = idHistoria
        self.tipoHistoria_Usuario = tipoHistoria_Usuario
        self.codigoHistoria_Usuario = codigoHistoria
        self.id_Pila_Historia_Usuario = historiaIdPila

# Tabla Usuario.
class User(db.Model):
    __tablename__ = 'usuario'
    fullname = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(16), primary_key = True)
    password = db.Column(db.String(16), nullable = False)
    email      = db.Column(db.String(30), unique = True)
    #idActores = db.Column(db.Integer, db.ForeignKey('actores.idactores'))

    def __init__(self,fullname, username, password, email):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        #self.idAcciones = idAcciones


# Tabla Acciones.
class Acciones(db.Model):
    __tablename__ = 'acciones'
    idProducto = db.Column(db.Integer, db.ForeignKey('pila.idPila'))
    idacciones      = db.Column(db.Integer, primary_key = True)
    descripAcciones = db.Column(db.String(500), nullable = False)
    
    def __init__(self, idPila, idAcciones, descripAcciones):
        self.idProducto = idPila
        self.idacciones      = idAcciones
        self.descripAcciones = descripAcciones
        

#class Pila(db.Model):

# Tabla Objetivo
class Objetivo(db.Model):
    __tablename__ = 'objetivo'
    idProducto = db.Column(db.Integer, db.ForeignKey('pila.idPila'))
    idObjetivo    = db.Column(db.Integer, primary_key = True)
    descripObjetivo = db.Column(db.String(500), nullable = False)

    def __init__(self, idPila, idObjetivo, descripObjetivo):
        # Constructor del modelo Acciones.
        self.idProducto = idPila
        self.idObjetivo       = idObjetivo
        self.descripObjetivo  = descripObjetivo

# Tabla Actores.
class Actores(db.Model):
    __tablename__  = 'actores'
    idProducto = db.Column(db.Integer, db.ForeignKey('pila.idPila'))
    id_actores     = db.Column(db.Integer, primary_key = True)
    nombre_actores = db.Column(db.String(50), nullable = False)
    descripcion_actores = db.Column(db.String(500), nullable = True)

    def __init__(self, idPila, id_actores, nombre_actores, descripcion_actores):
        # Constructor del modelo Actores.
        self.idProducto = idPila
        self.id_actores          = id_actores
        self.nombre_actores      = nombre_actores
        self.descripcion_actores = descripcion_actores


class EstadoActual(db.Model):
    __tablename__ = 'estados'
    id_producto_actual = db.Column(db.Integer, primary_key = True)
    id_actor_actual = db.Column(db.Integer, nullable = True)
    id_accion_actual = db.Column(db.Integer, nullable = True)
    id_objetivos_actual = db.Column(db.Integer, nullable = True)

    def __init__(self, id_producto_actual, id_actor_actual = None, id_accion_actual = None, id_objetivos_actual = None):
        self.id_producto_actual  = id_producto_actual
        self.id_actor_actual     = id_actor_actual
        self.id_accion_actual    = id_accion_actual
        self.id_objetivos_actual = id_objetivos_actual

#-------------------------------------------------------------------------------

def createDatabase():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    # Se crean las tablas de la base de datos.
    createDatabase()
    manager.run()

#-------------------------------------------------------------------------------