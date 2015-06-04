# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json, redirect
from app.scrum.funcHistoria import clsHistoria
from app.scrum.funcObjetivo import clsObjetivo
from app.scrum.funcActor    import clsActor
from app.scrum.funcHistObjetivo import clsHistoriaObj
from app.scrum.funcHistActores  import clsHistoriaActores
from app.scrum.funcEnlace import clsEnlace

import model

historias = Blueprint('historias', __name__)

#.----------------------------------------------------------------------------------------.

@historias.route('/historias/ACambiarPrioridades', methods=['POST'])
def ACambiarPrioridades():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Prioridades reasignadas']}, ]
    res = results[0]

    print(params)
    nuevaPrioridad = params.get('prioridad')
    idHistoria = int(session['idHistoria'])

    historiaModif = clsHistoria()
    resultModif = historiaModif.cambiar_Prioridad( idHistoria, nuevaPrioridad )

    if ( resultModif ):
        res = results[0]


    res['label'] = res['label']+'/' + str(idHistoria)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

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
    superAsociar = params.get('super', None)
    prioridadAsociar = params.get('prioridad', None)

    idProductoActual = session['idPila']
    if not(( codigoHistoria == None ) and ( accionAsociar == None ) and ( objetivosAsociar == None ) and ( actoresAsociar == None) and (superAsociar == None) and (prioridadAsociar == None)):
        accionQuery = model.Historia_Usuario.id_Acciones_Historia_Usuario == accionAsociar
        accionInHistory = model.db.session.query(model.Historia_Usuario).filter(accionQuery).all()

        if (accionInHistory == []):

            nuevoEnlace = clsEnlace()

            result = nuevoEnlace.insert_Enlace(idProductoActual, superAsociar)

            if (result):
                nuevaHistoria = clsHistoria()
                resultInsert = nuevaHistoria.insert_Historia(idProductoActual, codigoHistoria, tipoAsociar, accionAsociar, superAsociar, prioridadAsociar) 

                if ( resultInsert[0] ):
                    histObjetivo = clsHistoriaObj()
                    histActores  = clsHistoriaActores()

                    # Se agregan los objetivos seleccionados en la base de datos.
                    for obj in objetivosAsociar:
                        histObjetivo.insert_Objetivo(resultInsert[1], obj)

                    # Se agregan los actores seleccionados en la base de datos.
                    for act in actoresAsociar:
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
    superAsociar = params.get('super', None)

    #print("tipoAsociar",tipoAsociar,"codigo",codigoHistoria,"accion",accionAsociar,"obj",objetivosAsociar,"act",actoresAsociar,"super",superAsociar)

    nuevaHistoria = clsHistoria()
    nuevoObjetivo = clsHistoriaObj()
    nuevoActor    = clsHistoriaActores()
    listaModify   = []
    
    querySuperHistoriaActual = model.db.session.query(model.Enlaces).\
                                filter(model.Enlaces.id_valor == idHistoria).\
                                all()

    enlaceEncontrado = querySuperHistoriaActual[0]
    viejoSuper = enlaceEncontrado.id_clave

    modifEnlace = clsEnlace()
    result = modifEnlace.modify_Enlace(idPila, viejoSuper, superAsociar, idHistoria)

    if (result):
        # BORRAR ACTORES ASOCIADOS A UNA HISTORIA. 
        findActor = nuevoActor.find_Actores(idHistoria)
        
        resultModifActores = False
        
        if ( findActor != [] ):
                resultModifActores = True
                for find in findActor:
                    if ( resultModifActores == True ):
                        resultModifActores = nuevoActor.modify_Actor(idHistoria,find)
                listaModify.append(resultModifActores)
                
     
        #BORRAR OBJETIVOS ASOCIADOS A UNA HISTORIA.        
        findObjetivo = nuevoObjetivo.find_Objetivo(idHistoria)
        
        resultModifObjetivo = False
        
        if ( findObjetivo != [] ):    
                  
                resultModifObjetivo = True
                for find in findObjetivo:
                     if ( resultModifObjetivo == True ):
                         resultModifObjetivo= nuevoObjetivo.modify_Objetivo(idHistoria,find)
                listaModify.append(resultModifObjetivo)
             

        # BORRAR UNA HISTORIA.         
        findHistoria = nuevaHistoria.find_Historia(idHistoria)
        resultModifHistoria = False
            
        if ( findHistoria != [] ):
            
                resultModifHistoria = True
                for find in findHistoria:
                    if ( resultModifHistoria == True ):
                        resultModifHistoria = nuevaHistoria.modify_Historia(idPila,idHistoria)
                listaModify.append(resultModifHistoria)
                
        #------------------------------------------------------------------------------------------
        idProductoActual = session['idPila']
        if not(( codigoHistoria == None ) or ( accionAsociar == None ) or ( objetivosAsociar == None ) or ( actoresAsociar == None) ):
            accionQuery = model.Historia_Usuario.id_Acciones_Historia_Usuario == accionAsociar
            accionInHistory = model.db.session.query(model.Historia_Usuario).filter(accionQuery).all()

            if (accionInHistory == []):
                nuevaHistoria = clsHistoria()
                resultInsert = nuevaHistoria.insert_Historia(idProductoActual, codigoHistoria, tipoAsociar, accionAsociar, superAsociar, prioridadAsociar) 

                if ( resultInsert[0] ):
                    histObjetivo = clsHistoriaObj()
                    histActores  = clsHistoriaActores()

                    # Se agregan los objetivos seleccionados en la base de datos.
                    for obj in objetivosAsociar:
                        histObjetivo.insert_Objetivo(resultInsert[1], obj)

                    # Se agregan los actores seleccionados en la base de datos.
                    for act in actoresAsociar:
          
                        histActores.insert_Actor(resultInsert[1], act)
                    

                    resu = True
                    res['idHistoria'] = resultInsert[1]
        
       
        if ( listaModify == [True,True,True] and resu ):
            res = results[0]
    #----------------------------------------------------------------------------------------------------------------------------------------------

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

    idProductoActual = int(session['idPila'])

    # Lista de acciones que están asociado al producto actual.
    acciones = model.db.session.query(model.Acciones).\
                filter(model.Acciones.idProducto == idProductoActual).\
                all()

    # Lista de actores que están asociado al producto actual.
    actores = model.db.session.query(model.Actores).\
                filter(model.Actores.idProducto == idProductoActual).\
                all()
    
    objetivos = model.db.session.query(model.Objetivo).filter_by(idProducto = idProductoActual,transversalidad=0).all()

    historias = model.db.session.query(model.Historia_Usuario).\
            filter(model.Historia_Usuario.id_Pila_Historia_Usuario == idProductoActual).\
            all()

    prioridad = model.db.session.query(model.Pila).\
                filter(model.Pila.idPila == idProductoActual).all()
                
    print("hola",prioridad)
                
    if (prioridad[0].escalaProducto == 1):
        escalaP = 1
        
    if (prioridad[0].escalaProducto == 2):
        escalaP = 2

    # Se muestra por pantalla los actores que pertenecen al producto.
    res['fHistoria_opcionesActores'] = [
      {'key':act.id_actores,'value':act.nombre_actores}
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
    res['fHistoria_opcionesHistorias'] = [{'key':0,'value':'Ninguna'}]
    res['fHistoria_opcionesHistorias'] += [
      {'key': hist.idHistoria_Usuario,'value':hist.codigoHistoria_Usuario}
      for hist in historias]
    

    # Tipos de historias disponibles. 
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    
    if (escalaP == 1):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':1, 'value':'Alta'},
            {'key':2, 'value':'Media'},
            {'key':3, 'value':'Baja'},
        ]
        
    if (escalaP == 2):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':i, 'value':i}
            for i in range(1,21)]        


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

    idProducto = int(session['idPila'])
    idHistoriaActual = int(request.args.get('idHistoria',1))

    # Se obtiene la información de la historia actual.
    historiaActual = model.db.session.query(model.Historia_Usuario).\
                        filter(model.Historia_Usuario.idHistoria_Usuario == idHistoriaActual).\
                        all()
    historiaActual = historiaActual[0]


     # Lista de acciones que están asociado al producto actual.
    acciones = model.db.session.query(model.Acciones).\
                filter(model.Acciones.idProducto == idProducto).\
                all()

    # Lista de actores que están asociado al producto actual.
    actores = model.db.session.query(model.Actores).\
                filter(model.Actores.idProducto == idProducto).\
                all()

    objetivos = model.db.session.query(model.Objetivo).\
                    filter_by(idProducto = idProductoActual,transversalidad=0).\
                    all()
    
    historias = model.db.session.query(model.Historia_Usuario).\
                filter(model.Historia_Usuario.id_Pila_Historia_Usuario == idProducto).\
                all()

    prioridad = model.db.session.query(model.Pila).\
                filter(model.Pila.idPila == idProductoActual).all()
                
    if (prioridad[0].escalaProducto == 1):
        escalaP = 1
        
    if (prioridad[0].escalaProducto == 2):
        escalaP = 2

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
      {'key': hist.idHistoria_Usuario,'value':hist.codigoHistoria_Usuario}
      for hist in historias]
    res['fHistoria_opcionesHistorias'] += [{'key':0,'value':'Ninguna'}]

    # Tipos de historias disponibles. 
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]

    if (escalaP == 1):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':1, 'value':'Alta'},
            {'key':2, 'value':'Media'},
            {'key':3, 'value':'Baja'},
        ]
        
    
    if (escalaP == 2):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':i, 'value':i}
            for i in range(1,21)]       

    # Lista de actores que fueron elegidos para la historia actual (antes de la modificación).
    actoresHistoria = model.db.session.query(model.ActoresHistorias.idActores).\
            filter(model.ActoresHistorias.idHistoria == idHistoriaActual).\
            all()
    idActoresHistoria = [int(i[0]) for i in actoresHistoria]
 
    # Lista de objetivos que fueron elegidos para la historia actual (antes de la modifación).
    
    objetivosHistoria = model.db.session.query(model.ObjHistorias.idObjetivo).\
            filter(model.ObjHistorias.idHistoria == idHistoriaActual).\
            all()
    idObjetivosHistoria = [int(i[0]) for i in objetivosHistoria]

    #objetivos = model.db.session.query(model.Objetivo).filter_by(idProducto = idProducto,transversalidad=0).all()

    res['fHistoria'] = { 'super':0,
                         'idHistoria': idHistoriaActual,
                         'idPila': idProducto,
                         'objetivos':idObjetivosHistoria,
                         'actores': idActoresHistoria,
                         'accion': historiaActual.id_Acciones_Historia_Usuario,
                         'codigo': historiaActual.codigoHistoria_Usuario,
                         'tipo': int(historiaActual.tipoHistoria_Usuario),
                         'prioridad':historiaActual.idEscala}

    res['idPila'] = idProducto
    session['idHistoria'] = idHistoriaActual

    return json.dumps(res)


#.----------------------------------------------------------------------------------------.

@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProductoActual = int(session['idPila'])
    idProducto = model.Historia_Usuario.id_Pila_Historia_Usuario == idProductoActual
    historia = model.db.session.query(model.Historia_Usuario).filter(idProducto).all()

    res['idPila'] = idProductoActual
    res['data0'] = [
      {'idHistoria':his.idHistoria_Usuario, 'enunciado':his.codigoHistoria_Usuario} 
      for his in historia]
    
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@historias.route('/historias/VPrioridades')
def VPrioridades():
    #GET parameter
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProductoActual = session['idPila']

    prioridad = model.db.session.query(model.Pila).\
                filter(model.Pila.idPila == idProductoActual).all()

    #Escala dependiente del proyecto
    if (prioridad[0].escalaProducto == 1):
        escalaP = 1
        
    if (prioridad[0].escalaProducto == 2):
        escalaP = 2
        
    if (escalaP == 1):
        res['Prioridades_opcionesPrioridad'] = [
            {'key':1, 'value':'Alta'},
            {'key':2, 'value':'Media'},
            {'key':3, 'value':'Baja'},
        ]
        
    
    if (escalaP == 2):
        res['Prioridades_opcionesPrioridad'] = [
            {'key':i, 'value':i}
            for i in range(1,21)]      

    historias = model.db.session.query(model.Historia_Usuario).\
            filter(model.Historia_Usuario.id_Pila_Historia_Usuario == idProductoActual).\
            order_by(model.desc(model.Historia_Usuario.idEscala))

    res['idPila'] = idProductoActual
    res['fPrioridades'] = {'idPila':idProductoActual,
      'lista':[
        {'idHistoria':hist.idHistoria_Usuario,'prioridad':hist.idEscala, 'enunciado':'En tanto '+hist.listaActores + ' ' + hist.id_Acciones_Historia_Usuario + ' para '+ hist.listaObjetivos }
          for hist in historias]}

    #Action code ends here
    return json.dumps(res)
