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
    res = results[1]

    # Descripción del producto a crear.
    nuevaDescripcionProducto = params['descripcion']

    nuevoProducto = clsProducto()
    resultInsert = nuevoProducto.insert_Producto(nuevaDescripcionProducto)

    nuevoActor = clsActor()   
    idProductActual = resultInsert[1]

    # Se añaden los tres actores por defecto.
    check1 = nuevoActor.insert_Actor(idProductActual, 'Product Owner','Es el dueño del producto')
    check2 = nuevoActor.insert_Actor(idProductActual, 'Scrum Master','Es el maestro Scrum del producto')
    check3 = nuevoActor.insert_Actor(idProductActual, 'Developer','Es el desarrollador del producto')    

    res['idPila'] = idProductActual

    if (resultInsert[0] and check1 and check2 and check3):
        res = results[0]  

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

    # Se obtiene el identificador del producto actual.
    idProductoModif = int(session['idPila'])
    
    # Se obtiene la nueva descripción.
    nuevaDescripcionProducto = params['descripcion']

    productoModif = clsProducto()
    resultsModif = productoModif.modify_Producto(idProductoModif, nuevaDescripcionProducto)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}

    idProducto = int(request.args.get('idPila',1))

    # Se almacena la información recibida.
    res['fPila'] = {'idPila': idProducto,
                    'descripcion':request.args.get('descripcion')}
    res['idPila'] = idProducto

    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]
    
    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/VProducto')
def VProducto():
    res = {}

    idPila = int(request.args.get('idPila', 1))
    zero=0;

    # Carga de los actores, objetivos y acciones a la base de datos.
    actores = model.db.session.query(model.Actores).filter_by(idProducto = idPila).all()
    acciones = model.db.session.query(model.Acciones).filter_by(idProducto = idPila).all()
    objetivos = model.db.session.query(model.Objetivo).filter_by(idProducto = idPila).all()

    productoActual = model.db.session.query(model.Pila).filter_by(idPila = idPila).all()

    # Se envía la información del producto.
    res['fPila'] = {'idPila':idPila, 
                    'descripcion':productoActual[0].descripProducto}

    res['fPila_opcionesEscala'] = [
      {'key':1,'value':'Alta/Media/Baja'},
      {'key':2,'value':'Entre 1 y 20'}]
      
    # Se muestran todos los actores asosiados al producto.
    res['data3'] = [
        {'idActor':act.id_actores, 
         'nombre':act.nombre_actores, 
         'descripcion':act.descripcion_actores}
        for act in actores]
    
    # Se muestran todos los actores asosiados al producto.
    res['data5'] = [
        {'idAccion':acc.idacciones, 'descripcion':acc.descripAcciones}
         for acc in acciones]

    # Se muestran todos los actores asosiados al producto.
    res['data7'] = [
        {'idObjetivo':obj.idObjetivo, 'descripcion':obj.descripObjetivo}
         for obj in objetivos]   

    print(idPila)
    session['idPila'] = idPila
    res['idPila'] = idPila

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    # Se muestra la lista de productos.
    producto = model.Pila.query.all()
    res['data0'] = [
        {'idPila':product.idPila, 'nombre':product.descripProducto}
        for product in producto ]

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.