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
from app.scrum.tareas import tareas
app.register_blueprint(tareas)
from app.scrum.cates import cates
app.register_blueprint(cates)

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

# Tabla Pila (Productos):
class Productos(db.Model):
    __tablename__   = 'productos'
    identificador   = db.Column(db.Integer, primary_key = True)
    nombre          = db.Column(db.String(50), nullable = False)
    descripcion     = db.Column(db.String(500), nullable = True)
    escala          = db.Column(db.Integer, nullable = False)
    pilaAcciones    = db.relationship('Acciones', backref = 'pila_acciones', cascade="all, delete, delete-orphan")
    pilaObjetivos   = db.relationship('Objetivos', backref = 'pila_objetivos', cascade="all, delete, delete-orphan")
    pilaActores     = db.relationship('Actores', backref = 'pila_actores', cascade="all, delete, delete-orphan")
    pilaHistoria    = db.relationship('Historias',backref='pila_historia',cascade = "all, delete, delete-orphan")
    pilaEnlaces     = db.relationship('Enlaces', backref = 'pila_enlaces', cascade="all, delete, delete-orphan")
    def __init__(self, identificador, nombre, descripcion, escala):
        self.identificador  = identificador
        self.nombre         = nombre
        self.descripcion    = descripcion
        self.escala         = escala
        

# Tabla Historia:        
class Historias(db.Model):
    __tablename__    = 'historias'
    identificador    = db.Column(db.Integer, unique=True)
    tipo             = db.Column(db.Integer, nullable = True)
    codigo           = db.Column(db.String(10), primary_key=True,)
    idProducto       = db.Column(db.Integer, db.ForeignKey('productos.identificador'))
    idAccion         = db.Column(db.Integer, db.ForeignKey('acciones.identificador'))
    idSuper          = db.Column(db.Integer, nullable = False)
    idEscala         = db.Column(db.Integer, nullable = True)
    listaObjetivos = db.relationship('ObjHistorias',backref='historia',cascade = "all, delete, delete-orphan")
    listaActores = db.relationship('ActoresHistorias',backref='historia',cascade = "all, delete, delete-orphan")
    historiaTarea = db.relationship('Tareas',backref='historia',cascade = "all, delete, delete-orphan")
    historiaPeso = db.relationship('Pesos',backref='historia',cascade = "all, delete, delete-orphan")



    def __init__(self, identificador,codigo,idProducto, tipo,idAccion,idSuper, idEscala):
        self.identificador  = identificador
        self.tipo = tipo
        self.codigo = codigo
        self.idProducto = idProducto
        self.idAccion = idAccion
        self.idSuper = idSuper
        self.idEscala = idEscala

# Tabla Usuario.
class Users(db.Model):
    __tablename__ = 'usuarios'
    nombre = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(16), primary_key = True)
    clave = db.Column(db.String(16), nullable = False)
    correo = db.Column(db.String(30), unique = True)
    actor = db.Column(db.String(10), nullable = False)

    def __init__(self,fullname, username, password, email,actor):
        self.nombre = fullname
        self.username = username
        self.clave = password
        self.correo = email
        self.actor = actor


# Tabla Acciones.
class Acciones(db.Model):
    __tablename__ = 'acciones'
    idProducto = db.Column(db.Integer, db.ForeignKey('productos.identificador'))
    identificador = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(500), nullable = False)
    historiaAsociada = db.relationship('Historias',backref='acciones',cascade = "all, delete, delete-orphan")
    def __init__(self, idProducto, identificador, descripcion):
        self.idProducto = idProducto
        self.identificador  = identificador
        self.descripcion = descripcion

# Tabla Objetivo
class Objetivos(db.Model):
    __tablename__ = 'objetivos'
    idProducto = db.Column(db.Integer, db.ForeignKey('productos.identificador'))
    identificador = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(500), nullable = False)
    transversalidad = db.Column(db.Integer, nullable = True)
    historiaAsociada = db.relationship('ObjHistorias',backref='objetivos',cascade = "all, delete, delete-orphan")

    def __init__(self, idProducto, identificador, descripcion,transversalidad):
        self.idProducto = idProducto
        self.identificador = identificador
        self.descripcion = descripcion
        self.transversalidad = transversalidad

# Tabla Actores.
class Actores(db.Model):
    __tablename__  = 'actores'
    idProducto = db.Column(db.Integer, db.ForeignKey('productos.identificador'))
    identificador = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String(500), nullable = True)
    historiaAsociada = db.relationship('ActoresHistorias',backref='actores',cascade = "all, delete, delete-orphan")
    
    def __init__(self, idProducto, identificador, nombre, descripcion):
        # Constructor del modelo Actores.
        self.idProducto = idProducto
        self.identificador       = identificador
        self.nombre      = nombre
        self.descripcion = descripcion


class ObjHistorias(db.Model):
    __tablename__ = 'objHistorias'
    identificador = db.Column(db.Integer, primary_key = True)
    idHistoria = db.Column(db.Integer, db.ForeignKey('historias.identificador'))
    idObjetivo = db.Column(db.Integer, db.ForeignKey('objetivos.identificador'))

    def __init__(self, identificador, idHistoria, idObjetivo):
        self.identificador = identificador
        self.idHistoria = idHistoria
        self.idObjetivo = idObjetivo

class ActoresHistorias(db.Model):
    __tablename__ = 'actHistorias'
    identificador = db.Column(db.Integer, primary_key = True)
    idHistoria = db.Column(db.Integer, db.ForeignKey('historias.identificador'))
    idActores = db.Column(db.Integer, db.ForeignKey('actores.identificador'))

    def __init__(self, identificador, idHistoria, idActor):
        self.identificador = identificador
        self.idHistoria = idHistoria
        self.idActores = idActor

class Enlaces(db.Model):
    __tablename__ = 'enlaces'
    identificador = db.Column(db.Integer, primary_key = True)
    idProducto = db.Column(db.Integer, db.ForeignKey('productos.identificador'))
    idClave = db.Column(db.Integer, nullable = True)
    idValor = db.Column(db.Integer, nullable = True)

    def __init__(self, identificador, idProducto, idClave, idValor = None):
        self.identificador = identificador
        self.idProducto  = idProducto
        self.idClave     = idClave
        self.idValor    = idValor
        
class Categorias(db.Model):
    __tablename__ = 'categorias'
    identificador = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = True)
    peso = db.Column(db.Integer)
    categoriasTareas   = db.relationship('Tareas', backref = 'categoria_Tareas', cascade="all, delete, delete-orphan")

    def __init__(self, identificador,nombre, peso):
        self.identificador = identificador
        self.nombre     = nombre
        self.peso = peso
        

class Tareas(db.Model):
    __tablename__ = 'tareas'
    identificador = db.Column(db.Integer, primary_key = True)
    idHistoria = db.Column(db.Integer, db.ForeignKey('historias.identificador'))
    descripcion = db.Column(db.String(500), nullable = True)
    idCategoria = db.Column(db.Integer, db.ForeignKey ('categorias.identificador'))
    peso = db.Column(db.Integer)

    def __init__(self, identificador, idHistoria, descripcion, idCategoria, peso):
        self.identificador = identificador
        self.idHistoria  = idHistoria
        self.descripcion     = descripcion
        self.idCategoria = idCategoria
        self.peso = peso

class Pesos(db.Model):
    __tablename__ = 'pesos'
    identificador = db.Column(db.Integer, primary_key = True)
    idHistoria = db.Column(db.Integer, db.ForeignKey('historias.identificador'))
    peso = db.Column(db.Integer)
    
    def __init__(self, identificador, idHistoria,peso):
        self.identificador = identificador
        self.idHistoria  = idHistoria
        self.peso = peso

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()
