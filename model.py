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
from sqlalchemy             import CheckConstraint

#-------------------------------------------------------------------------------

# Construcción de la base de datos.

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:joel123@localhost/prueba"
    # Estructura para realizar la conexión con la base de datos:
    # "postgresql://yourusername:yourpassword@localhost/yournewdb"

db_dir = 'postgresql+psycopg2://postgres:joel123@localhost/prueba'
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

num_acciones  = 0
num_objetivos = 0
num_actores   = 0

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.


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
    idacciones         = db.Column(db.Integer, primary_key = True)
    descripAcciones = db.Column(db.String(500), nullable = False)
    
    def __init__(self,idAcciones, descripAcciones):
        self.idacciones      = idAcciones
        self.descripAcciones = descripAcciones
        

#class Pila(db.Model):

# Tabla Objetivo
class Objetivo(db.Model):
    __tablename__ = 'objetivo'
    idObjetivo    = db.Column(db.Integer, primary_key = True)
    descripObjetivo = db.Column(db.String(500), nullable = False)
    #pilas = relationship('Pila', backref = 'objetivo', cascade="all, delete, delete-orphan")

    def __init__(self, idObjetivo, descripObjetivo):
        # Constructor del modelo Acciones.
        self.idObjetivo       = idObjetivo
        self.descripObjetivo  = descripObjetivo

# Tabla Actores.
class Actores(db.Model):
    __tablename__  = 'actores'
    id_actores     = db.Column(db.Integer, primary_key = True)
    nombre_actores = db.Column(db.String(50), nullable = False)
    descripcion_actores = db.Column(db.String(500), nullable = False)

    def __init__(self, id_actores, nombre_actores, descripcion_actores):
        # Constructor del modelo Actores.
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