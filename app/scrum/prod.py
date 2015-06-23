# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        Módulo que contiene los métodos que permitirán insertar, modificar y
        eliminar productos.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:

from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
from app.scrum.funcProducto import clsProducto
from app.scrum.funcCategoria import clsCategoria
from model import db, Productos, Actores, Acciones, Objetivos, Categorias

prod = Blueprint('prod', __name__)

#.-----------------------------------------------------------------------------.

@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():

    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, 
               {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[1] 

    # Parámetros del producto a crear.
    nombre = params.get('nombre', None)
    descripcion = params.get('descripcion', None)
    escala = params.get('escala', None)

    if (nombre != None and escala != None and descripcion != None):
        producto = clsProducto()

        # creacionCorrecta es de la forma (Booleano, idProducto).
        creacionCorrecta = producto.insertar(nombre, descripcion, escala)
        print("creacionCorrecta", creacionCorrecta[0])
        if (creacionCorrecta[0]):
            actor = clsActor()   
            idProducto= creacionCorrecta[1]

            # Se añaden los tres actores por defecto.
            creacionPO = actor.insertar(idProducto, 'Product Owner',
                                        'Es el dueño del producto')
            creacionSM = actor.insertar(idProducto, 'Scrum Master',
                                        'Es el maestro Scrum del producto')
            creacionD = actor.insertar(idProducto, 'Developer',
                                       'Es el desarrollador del producto')    

            if ( creacionPO and creacionSM and creacionD ):
                res = results[0]
                res['idPila'] = idProducto
                
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
   
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']},
               {'label':'/VProductos', 'msg':['Error al modificar el producto']},]
    # Resultado de la modificación del producto.
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])
    
    # Parámetros del producto a modificar.
    nombre = params.get('nombre', None)
    descripcion = params.get('descripcion', None)
    escala = params.get('escala', None)

    if ((nombre != None) and (descripcion != None) and (escala != None)):
        producto = clsProducto()
        modificacionCorrecta = producto.modificar(idProducto, nombre, descripcion,
                                                  escala)

        if ( modificacionCorrecta ):
            res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}

    # Producto actual.
    idProducto = int(request.args.get('idPila',1))

    # Se almacena la información recibida.
    res['fPila'] = {'idPila': idProducto,
                    'descripcion':request.args.get('descripcion'),
                    'escala':request.args.get('escala',1)}
    res['idPila'] = idProducto
	
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@prod.route('/prod/VProducto')
def VProducto():
    res = {}

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Identificar del producto actual.
    idProducto = int(request.args.get('idPila', 1))

    # Carga de los actores, objetivos y acciones a la base de datos.
    actores = db.session.query(Actores).\
                    filter(Actores.idProducto == idProducto).all()
    acciones = db.session.query(Acciones).\
                    filter(Acciones.idProducto == idProducto).all()
    objetivos = db.session.query(Objetivos).\
                    filter(Objetivos.idProducto == idProducto).all()

    # Carga de la información del producto actual.
    producto = db.session.query(Productos).\
                    filter(Productos.identificador == idProducto).first()

    # Se envía la información del producto.
    res['fPila'] = {'idPila': idProducto, 
                    'nombre': producto.nombre,
                    'descripcion':producto.descripcion,
                    'escala': producto.escala}

    # Se muestran todos los actores asosiados al producto.
    res['data3'] = [
        {'idActor':act.identificador, 
         'nombre':act.nombre, 
         'descripcion':act.descripcion}
        for act in actores]
    
    # Se muestran todos los actores asosiados al producto.
    res['data5'] = [
        {'idAccion':acc.identificador, 'descripcion':acc.descripcion}
         for acc in acciones]

    # Se muestran todos los actores asosiados al producto.
    res['data7'] = [
        {'idObjetivo':obj.identificador, 'descripcion':obj.descripcion}
         for obj in objetivos]   


    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]

    session['idPila'] = idProducto
    res['idPila'] = idProducto

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    categorias = db.session.query(Categorias).all()
    
    if (categorias == []):
        categoria = clsCategoria()
        categoria.insertar('Implementar una acción',2)
        categoria.insertar('Implementar una vista',2)
        categoria.insertar('Implementar una regla de negocio o un método de una clase',2)
        categoria.insertar('Migrar la base de datos',2)
        categoria.insertar('Crear un diagrama UML',1)
        categoria.insertar('Crear datos iniciales',1)
        categoria.insertar('Crear una prueba de aceptación',1)
        categoria.insertar('Actualizar un elemento implementado en otra tarea',2)
        categoria.insertar('Actualizar en elemento implementado en otra tarea',1)
        categoria.insertar('Escribir el manual en línea de unapágina',1)

    # Se muestra la lista de productos.
    producto = Productos.query.all()

    res['usuario'] = session['usuario']
    res['data0'] = [
        {'idPila':product.identificador, 'nombre':product.nombre}
        for product in producto ]

    return json.dumps(res)

#.-----------------------------------------------------------------------------.
