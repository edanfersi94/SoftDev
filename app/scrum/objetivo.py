# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcObjetivo import clsObjetivo
from app.scrum.mdlaccesscontrol import clsAccessControl
import model

objetivo = Blueprint('objetivo', __name__)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[1]
    
    # Descripción del objetivo a crear.
    nueva_descripcion_objetivo = params.get('descripcion', None)

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])
    nueva_transversalidad = params['transversal']
    
    if (nueva_transversalidad==True):
        nueva_transversalidad=1
    else:
        nueva_transversalidad=0

    if ( nueva_descripcion_objetivo != None ):
        accessControl = clsAccessControl()
        resultCheck = accessControl.check_descripcion( nueva_descripcion_objetivo )

        if ( resultCheck ):
            nuevoObjetivo = clsObjetivo()
            resultInset = nuevoObjetivo.insert_Objetivo( idProducto, nueva_descripcion_objetivo,nueva_transversalidad)

            if ( resultInset ):
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

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[1]
    
    # Se obtiene el identificador del producto actual.
    idPila = int(session['idPila'])

    # Se obtiene los atributos del objetivo a modificar.
    id_objetivo = int(session['idObjetivo'])
    nueva_descripcion_objetivo = params['descripcion']

    objetivoModif = clsObjetivo()
    resultsModif  = objetivoModif.modify_Objetivo(idPila, id_objetivo, nueva_descripcion_objetivo)

    if ( resultsModif ):
        res = results[0]
    
    # Se actualiza el URL de la pág a donde se va a redirigir.
    res['label'] = res['label'] + '/' + str(id_objetivo)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}

    # Producto actual.
    idProducto = session['idPila']

    # Se almacena la información recibida.
    res['fObjetivo'] = {'idPila': idProducto,
                        'idObjetivo':request.args.get('idObjetivo',1),
                        'descripcion':request.args.get('descripcion')}
    res['idPila'] = idProducto
    res['fObjetivo_opcionesTransversalidad'] = [
      {'key':True, 'value':'Si'},{'key':False, 'value':'No'},
    ]

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProducto = int(request.args.get('idPila',1))

    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador del objetivo actual.
    idObjetivoActual = int(request.args.get('idObjetivo',1))
    session['idObjetivo'] = idObjetivoActual

    # Se obtiene la información del objetivo a modificar.
    infoObjActual = model.db.session.query(model.Objetivo).filter_by(idObjetivo = idObjetivoActual)
    descripcionObjetivoActual = infoObjActual[0].descripObjetivo

    # Se almacena la información a enviar.
    res['fObjetivo'] = {'idPila': idProducto,
                        'idObjetivo':idObjetivoActual,
                        'descripcion':descripcionObjetivoActual}
    res['fObjetivo_opcionesTransversalidad'] = [
      {'key':True, 'value':'Si'},{'key':False, 'value':'No'},
    ]

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.