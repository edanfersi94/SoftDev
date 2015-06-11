# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        Módulo que contiene las aplicaciones y vistas correspondientes a las
        acciones del producto.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, Acciones
from app.scrum.funcAccion import clsAccion
from flask import request, session, Blueprint, json
from app.scrum.controlDeAcceso import clsControlDeAcceso

accion = Blueprint('accion', __name__)

#.-----------------------------------------------------------------------------.

@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():

    params  = request.get_json()
    results = [{'label':'/VProducto',    'msg':['Acción creada']},
               {'label':'/VCrearAccion', 'msg':['Error al crear acción']},]
    # Resultado de la creación de la acción.
    res = results[1]

    # Parámetros de la acción a crear.
    idProducto = int(session['idPila'])
    descripcion = params.get('descripcion', None)
    
    if ( descripcion != None ):
        controlDeAcceso = clsControlDeAcceso()
        descripcionValida = controlDeAcceso.verificarDescripcion( descripcion )

        if ( descripcionValida ):
            accionNueva = clsAccion()
            creacionCorrecta = accionNueva.insertar(idProducto, descripcion)

            if ( creacionCorrecta ):
                res = results[0]
                # Se actualiza el URL de la pág a donde se va a redirigir.
                res['label'] = res['label'] + '/' + str(idProducto)
                
    res['idPila'] = idProducto

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.
@accion.route('/accion/AElimAccion')
def AElimAccion():
    #GET parameter
    identificador = int(session['idAccion'])
    # Identificador del producto al que pertenece la accion.
    idProducto = int(session['idPila'])
    results = [{'label':'/VProducto', 'msg':['Accion eliminada']}, 
               {'label':'/VAccion', 'msg':['No se pudo eliminar esta acción']}, ]
    res = results[1]
    
    accion = clsAccion()
    eliminarCorrecto = accion.eliminar(identificador)

    if(eliminarCorrecto):
        res = results[0]
        res['label'] = res['label'] + '/' + str(idProducto)

    # Se actualiza el URL de la pág a donde se va a redirigir.
    if (res == results[1]):
        res['label'] = res['label'] + '/' + str(identificador) 

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():

    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, 
               {'label':'/VAccion',   'msg':['Error al modificar acción']}, ]
    # Resultado de la creación de la acción.
    res = results[1]
    
    # Identificador del producto al que pertenece el objeto.
    idProducto = int(session['idPila'])

    # Parámetros de la acción a modificar.
    identificador = int(session['idAccion'])
    descripcion   = params.get('descripcion', None)

    if (descripcion != None):
        accionModificar = clsAccion()
        modificacionCorrecta = accionModificar.modificar( identificador, descripcion)

        if ( modificacionCorrecta ):
            res = results[0]
            res['label'] = res['label'] + '/' + str(idProducto)

    # Se actualiza el URL de la pág a donde se va a redirigir.
    if (res == results[1]):
        res['label'] = res['label'] + '/' + str(identificador)
    res['idPila'] = idProducto
    session['idAccion'] = identificador

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    idProducto = int(session['idPila'])
    res = {}

    # Producto actual.
    idProducto = int(session['idPila'])

    # Se almacena la información recibida.
    res['fAccion'] = {'idPila':idProducto,
                      'idAccion':request.args.get('idAccion',1),
                      'descripción':request.args.get('descripcion')}
    res['idPila'] = idProducto
    
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    res['idPila'] = idProducto

    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@accion.route('/accion/VAccion')
def VAccion():
    identificador = int(request.args.get('idAccion',1))
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    idProducto = int(request.args.get('idPila',1))

    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador de la acción actual.
    session['idAccion'] = identificador

    # Se obtiene la información del objetivo a modificar.
    accionBuscada = db.session.query(Acciones).\
                         filter(Acciones.identificador == identificador).first()
    descripcion = accionBuscada.descripcion

    # Se almacena la información a enviar.
    res['fAccion'] = {'idPila': idProducto,
                      'idAccion':identificador,
                      'descripcion':descripcion}

    return json.dumps(res)

#.-----------------------------------------------------------------------------.
