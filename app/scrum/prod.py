# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
from app.scrum.funcProducto import clsProducto
import model

prod = Blueprint('prod', __name__)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    nuevaDescripcionProducto = params['descripcion']

    nuevoProducto = clsProducto()
    resultInsert = nuevoProducto.insert_Producto(nuevaDescripcionProducto)

    nuevoActor = clsActor()
   
    idProductActual = resultInsert[1]

    check1 = nuevoActor.insert_Actor(idProductActual, 'Product Owner','Es el dueño del producto')
    check2 = nuevoActor.insert_Actor(idProductActual, 'Scrum Master','Es el Maestro Scrum del producto')
    check3 = nuevoActor.insert_Actor(idProductActual, 'Developer','Es el desarrollador del producto')    

    if (resultInsert[0] and check1 and check2 and check3):
        res = results[0]
    else:
        res = results[1]    

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, ]
    res = results[0]

    productoActual = model.db.session.query(model.EstadoActual).all()

    idProductoModif = int(productoActual[0].id_producto_actual)
    nuevaDescripcionProducto = params['descripcion']

    productoModif = clsProducto()
    resultsModif = productoModif.modify_Producto(idProductoModif, nuevaDescripcionProducto)

    if (resultsModif):
        res = results[0]
    else:
        res = results[1]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    pagActorActual= request.url
    pagActorActual.split('=')
    productoActual = pagActorActual[-1]

    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/VProducto')
def VProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    pagActorActual= request.url
    pagActorActual.split('=')
    productoActual = pagActorActual[-1]

    if (productoActual == 'undefined' or productoActual == 's'):
        # Se obtiene el ultimo producto visitado.
        productoVisitado = model.db.session.query(model.EstadoActual).all()
        idPila = int(productoVisitado[0].id_producto_actual)
    else:
        idPila = int(productoActual)

    # Se actualiza el producto actual en la tabla de datos.
    model.db.session.query(model.EstadoActual).update({'id_producto_actual':idPila})

    # Carga de los actores, objetivos y acciones a la base de datos.
    actores = model.db.session.query(model.Actores).filter_by(idProducto = idPila).all()
    acciones = model.db.session.query(model.Acciones).filter_by(idProducto = idPila).all()
    objetivos = model.db.session.query(model.Objetivo).filter_by(idProducto = idPila).all()

    res['data3'] = [
        {'idActor':act.id_actores, 'descripcion':act.nombre_actores}
        for act in actores]
    res['data5'] = [
        {'idAccion':acc.idacciones, 'descripcion':acc.descripAcciones}
         for acc in acciones]
    res['data7'] = [
        {'idObjetivo':obj.idObjetivo, 'descripcion':obj.descripObjetivo}
         for obj in objetivos]
    
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    productosListados = model.EstadoActual.query.all()
    if ( len(productosListados) == 0):
        producto1 = model.EstadoActual(1)
        model.db.session.add(producto1)
        model.db.session.commit()

    producto = model.Pila.query.all()

    res['data0'] = [
        {'idPila':product.idPila, 'nombre':product.descripProducto}
        for product in producto ]

    pagActorActual= request.url
    pagActorActual.split('=')
    productoActual = pagActorActual[-1]

    if (productoActual == 'undefined' or productoActual == 's'):
        # Se obtiene el ultimo producto visitado.
        productoVisitado = model.db.session.query(model.EstadoActual).all()
        idPila = int(productoVisitado[0].id_producto_actual)
    else:
        idPila = int(productoActual)

    # Se actualiza el producto actual en la tabla de datos.
    model.db.session.query(model.EstadoActual).update({'id_producto_actual':idPila})

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

