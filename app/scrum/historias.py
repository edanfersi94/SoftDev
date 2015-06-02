# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json, redirect
from app.scrum.funcHistoria import clsHistoria
from app.scrum.funcObjetivo import clsObjetivo
from app.scrum.funcActor    import clsActor
from app.scrum.funcHistObjetivo import clsHistoriaObj
from app.scrum.funcHistActores  import clsHistoriaActores

import model

historias = Blueprint('historias', __name__)

#.----------------------------------------------------------------------------------------.

@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[1]

    # Atributos de la historia a crear.
    tipoAsociar = params['tipo']
    codigoHistoria = params.get('codigo', None)
    accionAsociar = params.get('accion', None) 
    objetivosAsociar = params.get('objetivos', None)
    actoresAsociar = params.get('actores', None)


    idProductoActual = session['idPila']
    if not(( codigoHistoria == None ) or ( accionAsociar == None ) or ( objetivosAsociar == None ) or ( actoresAsociar == None) ):
        accionQuery = model.Historia_Usuario.id_Acciones_Historia_Usuario == accionAsociar
        accionInHistory = model.db.session.query(model.Historia_Usuario).filter(accionQuery).all()

        if (accionInHistory == []):
            nuevaHistoria = clsHistoria()
            resultInsert = nuevaHistoria.insert_Historia(idProductoActual, codigoHistoria, tipoAsociar, accionAsociar) 

            if ( resultInsert[0] ):
                histObjetivo = clsHistoriaObj()
                histActores  = clsHistoriaActores()

                # Se agregan los objetivos seleccionados en la base de datos.
                for obj in objetivosAsociar:
                    histObjetivo.insert_Objetivo(resultInsert[1], obj)

                # Se agregan los actores seleccionados en la base de datos.
                for act in actoresAsociar:
                    print(act)
                    histActores.insert_Actor(resultInsert[1], act)

                res = results[0]
                res['idHistoria'] = resultInsert[1]
    
    res['idPila'] = idProductoActual 
    res['label'] = res['label'] + '/' + str(idProductoActual) 

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idPila = int(session['idPila'])
    idHistoria = int(session['idHistoria'])

    # Nuevos atributos de la historia a modificar.
    tipoAsociar = params.get('tipo', None)
    codigoHistoria = params.get('codigo', None)
    accionAsociar = params.get('accion', None) 
    objetivosAsociar = params.get('objetivos', None)
    actoresAsociar = params.get('actores', None)

    nuevaHistoria = clsHistoria()
    nuevoObjetivo = clsHistoriaObj()
    nuevoActor    = clsHistoriaActores()
    listaModify   = []
    
    #---------------------------------------------------------------------------------------
    # BORRAR ACTORES ASOCIADOS A UNA HISTORIA
    
    findActor = nuevoActor.find_Actores(idHistoria)
    
    resultModifActores = False
    
    if ( findActor != [] ):
            resultModifActores = True
            for find in findActor:
                if ( resultModifActores == True ):
                    resultModifActores = nuevoActor.modify_Actor(idHistoria,find)
            listaModify.append(resultModifActores)
            
    #----------------------------------------------------------------------------------------
    #BORRAR OBJETIVOS ASOCIADOS A UNA HISTORIA        
    
    findObjetivo = nuevoObjetivo.find_Objetivo(idHistoria)
    
    resultModifObjetivo = False
    
    if ( findObjetivo != [] ):    
              
            resultModifObjetivo = True
            for find in findObjetivo:
                 if ( resultModifObjetivo == True ):
                     resultModifObjetivo= nuevoObjetivo.modify_Objetivo(idHistoria,find)
            listaModify.append(resultModifObjetivo)
         
              
    #------------------------------------------------------------------------------------------
    # BORRAR UNA HISTORIA
             
    findHistoria = nuevaHistoria.find_Historia(idHistoria)
    resultModifHistoria = False
        
    if ( findHistoria != [] ):
        
            resultModifHistoria = False
            for find in findHistoria:
                if ( resultModifHistoria == True ):
                    resultModifHistoria = nuevaHistoria.modify_Historia(idHistoria,find)
            listaModify.append(resultModifHistoria)
            
    #------------------------------------------------------------------------------------------
    if ( listaModify == [True,True,True] ):
        res = results[0]
    #----------------------------------------------------------------------------------------------------------------------------------------------
    #INSERTAR NUEVA HISTORIA    
    idProductoActual = session['idPila']
    if not(( codigoHistoria == None ) or ( accionAsociar == None ) or ( objetivosAsociar == None ) or ( actoresAsociar == None) ):
        accionQuery = model.Historia_Usuario.id_Acciones_Historia_Usuario == accionAsociar
        accionInHistory = model.db.session.query(model.Historia_Usuario).filter(accionQuery).all()

        if (accionInHistory == []):
            nuevaHistoria = clsHistoria()
            resultInsert = nuevaHistoria.insert_Historia(idProductoActual, codigoHistoria, tipoAsociar, accionAsociar) 

            if ( resultInsert[0] ):
                histObjetivo = clsHistoriaObj()
                histActores  = clsHistoriaActores()

                # Se agregan los objetivos seleccionados en la base de datos.
                for obj in objetivosAsociar:
                    histObjetivo.insert_Objetivo(resultInsert[1], obj)

                # Se agregan los actores seleccionados en la base de datos.
                for act in actoresAsociar:
                    print(act)
                    histActores.insert_Actor(resultInsert[1], act)

                res = results[0]
                res['idHistoria'] = resultInsert[1]
    #------------------------------------------------------------------------------------------------

    res['idHistoria'] = idHistoria
    # Se actualiza el URL de la pág a donde se va a redirigir.
    res['label'] = res['label'] + '/' + str(idHistoria)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProductoActual = session['idPila']
    accionesEsp = model.Acciones.idProducto == idProductoActual
    acciones = model.db.session.query(model.Acciones).filter(accionesEsp).all()
    
    actoresEsp = model.Actores.idProducto == idProductoActual
    actores = model.db.session.query(model.Actores).filter(actoresEsp).all()

    objetivosEsp = model.Objetivo.idProducto == idProductoActual
    objetivos = model.db.session.query(model.Objetivo).filter(objetivosEsp).all()

    # Se muestra por pantalla los actores que pertenecen al producto.
    res['fHistoria_opcionesActores'] = [
      {'key':act.id_actores,'value':act.descripcion_actores}
        for act in actores]

    # Se muestra por pantalla las acciones que pertenecen al producto.
    res['fHistoria_opcionesAcciones'] = [
      {'key':acc.idacciones,'value':acc.descripAcciones}
        for acc in acciones]

    # Se muestra por pantalla los objetivos que pertenecen al producto.
    res['fHistoria_opcionesObjetivos'] = [
      {'key':obj.idObjetivo,'value':obj.descripObjetivo}
        for obj in objetivos]

    # TEMPORAL.
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'}]

    # Tipos de historias disponibles. 
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]

    # Se almacena la información recibida.  

    res['idPila'] = session['idPila']
    res['idHistoria'] = int(request.args.get('idHistoria',1))

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProducto = int(request.args.get('idPila',1))
    idHistoriaActual = int(request.args.get('idHistoria',1))
    print(idProducto)
    historialActual = model.db.session.query(model.Historia_Usuario).filter(model.Historia_Usuario.idHistoria_Usuario == idHistoriaActual).all()
    historialActual = historialActual[0]
    res['idPila'] = idProducto

    #Action code goes here, res should be a JSON structure
    accionesEsp = model.Acciones.idProducto == idProducto
    acciones = model.db.session.query(model.Acciones).filter(accionesEsp).all()
    
    actoresEsp = model.Actores.idProducto == idProducto
    actores = model.db.session.query(model.Actores).filter(actoresEsp).all()
    
    objetivosEsp = model.Objetivo.idProducto == idProducto
    objetivos = model.db.session.query(model.Objetivo).filter(objetivosEsp).all()
    
    res['fHistoria'] = { 'codigo': historialActual.codigoHistoria_Usuario,
                         'super' : 0}
    
    # Se muestra por pantalla los actores que pertenecen al producto.
    res['fHistoria.actores'] = [
      {'key':act.id_actores,'value':act.descripcion_actores}
        for act in actores]

    # Se muestra por pantalla las acciones que pertenecen al producto.
    res['fHistoria.accion'] = [
      {'key':acc.idacciones,'value':acc.descripAcciones}
        for acc in acciones]

    # Se muestra por pantalla los objetivos que pertenecen al producto.
    res['fHistoria.objetivo'] = [
      {'key':obj.idObjetivo,'value':obj.descripObjetivo}
        for obj in objetivos]

    # TEMPORAL.
    res['fHistoria.super'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'}]

    # Tipos de historias disponibles. 
    res['fHistoria.actores.tipo'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]

    res['idPila'] = idProducto
    session['idHistoria'] = idHistoriaActual

    return json.dumps(res)


#.----------------------------------------------------------------------------------------.

@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    idProductoActual = int(request.args.get('idPila'))
    idProducto = model.Historia_Usuario.id_Pila_Historia_Usuario == idProductoActual
    historia = model.db.session.query(model.Historia_Usuario).filter(idProducto).all()

    res['idPila'] = idProductoActual
    res['data0'] = [
      {'idHistoria':his.idHistoria_Usuario, 'enunciado':his.codigoHistoria_Usuario} 
      for his in historia]
    
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.