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

db_dir = 'postgresql+psycopg2://BMO:@localhost/newapmwsc'
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
from app.scrum.historias import historias
app.register_blueprint(historias)

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

# Tabla Pila (Productos):
class Pila(db.Model):
    __tablename__   = 'pila'
    idPila          = db.Column(db.Integer, primary_key = True)
    descripProducto = db.Column(db.String(50), nullable = True)
    pilaAcciones    = db.relationship('Acciones', backref = 'pila_acciones', cascade="all, delete, delete-orphan")
    pilaObjetivos   = db.relationship('Objetivo', backref = 'pila_objetivos', cascade="all, delete, delete-orphan")
    pilaActores     = db.relationship('Actores', backref = 'pila_actores', cascade="all, delete, delete-orphan")
    pilaHistoria    = db.relationship('Historia_Usuario',backref='pila_historia',cascade = "all, delete, delete-orphan")
    
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
    id_Acciones_Historia_Usuario = db.Column(db.Integer, db.ForeignKey('acciones.idacciones'))
    listaObjetivos = db.relationship('ObjHistorias',backref='historia',cascade = "all, delete, delete-orphan")
    listaActores = db.relationship('ActoresHistorias',backref='historia',cascade = "all, delete, delete-orphan")

    def __init__(self, idHistoria,codigoHistoria,historiaIdPila, tipoHistoria_Usuario,id_Acciones_Historia_Usuario):
        self.idHistoria_Usuario  = idHistoria
        self.tipoHistoria_Usuario = tipoHistoria_Usuario
        self.codigoHistoria_Usuario = codigoHistoria
        self.id_Pila_Historia_Usuario = historiaIdPila
        self.id_Acciones_Historia_Usuario = id_Acciones_Historia_Usuario

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
    pilaHistoriaUsuario = db.relationship('Historia_Usuario',backref='pila',cascade = "all, delete, delete-orphan")
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
    historiaAsociada = db.relationship('ObjHistorias',backref='objetivo',cascade = "all, delete, delete-orphan")

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
    historiaAsociada = db.relationship('ActoresHistorias',backref='actores',cascade = "all, delete, delete-orphan")
    
    def __init__(self, idPila, id_actores, nombre_actores, descripcion_actores):
        # Constructor del modelo Actores.
        self.idProducto = idPila
        self.id_actores          = id_actores
        self.nombre_actores      = nombre_actores
        self.descripcion_actores = descripcion_actores


class ObjHistorias(db.Model):
    __tablename__ = 'objHistorias'
    idObjetivoHistoria = db.Column(db.Integer, primary_key = True)
    idHistoria = db.Column(db.Integer, db.ForeignKey('historia.idHistoria_Usuario'))
    idObjetivo = db.Column(db.Integer, db.ForeignKey('objetivo.idObjetivo'))

    def __init__(self, idObjetivoHistoria, idHistoria, idObjetivo):
        self.idObjetivoHistoria = idObjetivoHistoria
        self.idHistoria = idHistoria
        self.idObjetivo = idObjetivo

class ActoresHistorias(db.Model):
    __tablename__ = 'actHistorias'
    idActoresHistoria = db.Column(db.Integer, primary_key = True)
    idHistoria = db.Column(db.Integer, db.ForeignKey('historia.idHistoria_Usuario'))
    idActores = db.Column(db.Integer, db.ForeignKey('actores.id_actores'))

    def __init__(self, idActoresHistoria, idHistoria, idActor):
        self.idActoresHistoria = idActoresHistoria
        self.idHistoria = idHistoria
        self.idActores = idActor

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