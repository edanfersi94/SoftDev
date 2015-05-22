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
#.-------------------------------------------------------------------------------.

# Librerias a importar:

from flask                  import Flask, request, session, Blueprint, json
from flask.ext.migrate      import Migrate, MigrateCommand
from flask.ext.sqlalchemy   import SQLAlchemy
from flask.ext.script       import Manager, Server
from sqlalchemy             import CheckConstraint
from random                 import SystemRandom
from datetime               import timedelta

#.-------------------------------------------------------------------------------.

app = Flask(__name__, static_url_path='')

# Construcción de la base de datos.

SQLALCHEMY_DATABASE_URI = "postgresql://BMO:@localhost/newapmwsc"
    # Estructura para realizar la conexión con la base de datos:
    # "postgresql://yourusername:yourpassword@localhost/yournewdb"

db_dir = 'postgresql+psycopg2://postgres:BMO:@localhost/newapmwsc'
# Estructrua:
# 'postgresql+psycopg2://user:password@localhost/the_database'  

# Instancia de la aplicación a utilizar.
#app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_dir
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# Instancia de la base de datos a usar.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)
#manager = Manager(app)
manager.add_command('db', MigrateCommand)



@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

from app.scrum.ident import ident
app.register_blueprint(ident)
from app.scrum.prod import prod
app.register_blueprint(prod)
from app.scrum.mast import mast
app.register_blueprint(mast)
from app.scrum.dev import dev
app.register_blueprint(dev)
from app.scrum.actor import actor
app.register_blueprint(actor)
from app.scrum.objetivo import objetivo
app.register_blueprint(objetivo)
from app.scrum.accion import accion
app.register_blueprint(accion)

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

num_pila = 0
num_acciones = 0
num_actores = 0
num_objetivos = 0

# Tabla Pila (Productos):
class Pila(db.Model):
    __tablename__   = 'pila'
    idPila          = db.Column(db.Integer, primary_key = True)
    nomProducto     = db.Column(db.String(30), nullable = True)
    idActor         = db.Column(db.Integer, nullable = True)
    nomActor        = db.Column(db.String(500), nullable = True)
    idObjetivo      = db.Column(db.Integer, nullable = True)
    descripObjetivo = db.Column(db.String(500), nullable = True)
    idAccion        = db.Column(db.Integer, nullable = True)
    descripAccion   = db.Column(db.String(500), nullable = True)

    def __init__(self,nomProducto,idActor,nomActor, idObjetivo, descripObjetivo, idAccion, descripAccion):
        num_pila     = num_pila + 1
        self.idPila  = num_pila
        self.nomProducto = nomProducto
        self.idActor = idActor
        self.nomActor = nomActor
        self.idObjetivo = idObjetivo
        self.descripObjetivo = descripObjetivo
        self.idAccion = idAccion
        self.descripAccion = descripAccion

# Tabla Usuario.
class User(db.Model):
    __tablename__ = 'usuario'
    fullname = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(16), primary_key = True)
    password = db.Column(db.String(16), nullable = False)
    email    = db.Column(db.String(30), unique = True)
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
    idacciones      = db.Column(db.Integer, primary_key = True)
    descripAcciones = db.Column(db.String(500), nullable = False)
    #usuarios       = db.relationship('User', backref = 'acciones', cascade="all, delete, delete-orphan")
    #pilas = relationship('Pila', backref = 'acciones', cascade="all, delete, delete-orphan")

    def __init__(self, idacciones, descripAcciones):
        # Constructor del modelo Acciones.
        num_acciones         = num_acciones + 1
        self.idacciones      = num_acciones
        self.descripAcciones = descripAcciones


# Tabla Actores.
class Actores(db.Model):
    __tablename__ = 'actores'
    id_actores     = db.Column(db.Integer, primary_key = True)
    nombre_actores = db.Column(db.String(50), nullable = False)
    #pilas = relationship('Pila', backref = 'acciones', cascade="all, delete, delete-orphan")

    def __init__(self, nombre_actores):
        # Constructor del modelo Acciones.
        num_actores          = num_actores + 1
        self.id_actores      = num_actores
        self.nombre_actores  = nombre_actores
        
class Objetivos(db.Model):
    __tablename__ = 'objetivos'
    id_objetivos   = db.Column(db.Integer, primary_key = True)
    descripObjetivos = db.Column(db.String(500), nullable = False)
    
    def __init__(self,descripObjetivos):
        num_objetivos          = num_objetivos + 1
        self.id_objetivos      = num_objetivos
        self.descripObjetivos  = descripObjetivos


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

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()
