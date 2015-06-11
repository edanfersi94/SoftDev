# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        Equipo SoftDev
    DESCRIPCION: 
        Módulo que contiene las aplicaciones y vistas correspondientes de
        las historias.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from flask import request, session, Blueprint, json, redirect
from app.scrum.funcHistoria import clsHistoria
from app.scrum.funcObjetivo import clsObjetivo
from app.scrum.funcActor    import clsActor
from app.scrum.funcHistObjetivo import clsHistoriaObj
from app.scrum.funcHistActores  import clsHistoriaActores
from app.scrum.funcEnlace import clsEnlace
from model import db,func,Historias,Objetivos,Acciones,Actores
from model import Productos, ActoresHistorias, ObjHistorias, Enlaces, Tareas
from app.scrum.funcTarea import clsTarea

historias = Blueprint('historias', __name__)

#.-----------------------------------------------------------------------------.

@historias.route('/historias/ACambiarPrioridades', methods=['POST'])
def ACambiarPrioridades():

    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Prioridades reasignadas']}, ]
    res     = results[0]

    idProducto = int(session['idPila'])

    # Identificador de la historia actual.
    #identificador = int (request.args.get('idHistoria',1))

    # Nueva prioridad.
    prioridadH = params.get('lista',None)

    if (prioridadH != None):

        for prioridadf in prioridadH:
            identificador  = prioridadf.get('idHistoria',None)
            prioridad    = prioridadf.get('prioridad', None) 

    
            historia = clsHistoria()
            creacionCorrecta = historia.cambiarPrioridad(identificador,prioridad)

    res['label']  = res['label']+'/'+str(idProducto)
    res['idPila'] = idProducto

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():

    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']},
               {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[1]

    # Identificador del producto actual.
    idProducto = int(session['idPila'])

    # Atributos de la historia a crear.
    tipo = params.get('tipo', None)
    codigo = params.get('codigo', None)
    accion = params.get('accion', None) 
    objetivo = params.get('objetivos', None)
    actor = params.get('actores', None)
    idSuper = params.get('super', None)
    prioridad = params.get('prioridad', None)

    if not(( tipo == None ) and ( codigo == None ) and ( accion == None ) and 
           ( objetivos == None ) and ( actor == None) and (idSuper == None) and 
           (prioridad == None)):
        accionBuscada = db.session.query(Historias).\
                            filter(Historias.idAccion == accion).first()

        if (accionBuscada == None):
            # Se verifica si la epica nueva no genera un bucle.
            enlace = clsEnlace()
            creacionEnlace = enlace.insertar(idProducto,idSuper)

            if (creacionEnlace):
                historia = clsHistoria()
                # creacionCorrecta es una tupla de la forma (Booleano, Identificador).
                creacionCorrecta = historia.insertar(idProducto, codigo, tipo, 
                                                     accion, idSuper, prioridad) 

                if ( creacionCorrecta[0] ):
                    histObjetivo = clsHistoriaObj()
                    histActores  = clsHistoriaActores()

                    # Se agregan los objetivos seleccionados en la base de datos.
                    for obj in objetivo:
                        histObjetivo.insertar(creacionCorrecta[1], obj)

                    # Se agregan los actores seleccionados en la base de datos.
                    for act in actor:
                        histActores.insertar(creacionCorrecta[1], act)

                    res = results[0]
                    res['idHistoria'] = creacionCorrecta[1]
                     
    
    res['idPila'] = idProducto 
    # Se actualiza el URL de la pág a donde se va a redigirir.
    res['label'] = res['label'] + '/' + str(idProducto)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)
#.--------------------------------------------------------------------------------------------------------------
@historias.route('/historias/AElimHistoria')
def AElimHistoria():
    
    idProducto = session['idPila']
    identificador = session['idHistoria']
    results = [{'label':'/VHistorias', 'msg':['Historia eliminada']}, {'label':'/VHistoria', 'msg':['No se pudo eliminar esta historia']}, ]
    res = results[1]
    
    historia = clsHistoria()
    actores = clsHistoriaActores()
    objetivos = clsHistoriaObj()
    listaEliminar = []

    enlacesActuales = db.session.query(Enlaces).all()
    listaEnlace = {}

    for enlace in enlacesActuales:
        if (enlace.idClave in listaEnlace):
            listaEnlace[enlace.idClave] += [enlace.idValor]
        else:
            listaEnlace[enlace.idClave] = [enlace.idValor]

        if not(enlace.idValor in listaEnlace):
            listaEnlace[enlace.idValor] =[]

    print(listaEnlace)
    if (listaEnlace[identificador] == [] ):
        
        historiaBuscada = db.session.query(Historias).\
                           filter(Historias.identificador == identificador).\
                           first()
                    
        eliminarActor = actores.eliminar(identificador)
        listaEliminar.append(eliminarActor)
                 
        #BORRAR OBJETIVOS ASOCIADOS A LA HISTORIA.        
        eliminarObjetivo= objetivos.eliminar(identificador)
        listaEliminar.append(eliminarObjetivo)
                         
        # BORRAR TAREAS.
        listaTareas = db.session.query(Tareas).\
                        filter(Tareas.idHistoria == identificador).\
                        all()   
        tareaEliminar = clsTarea()
        for tarea in listaTareas:
            tareaEliminar.eliminar(tarea.identificador)
                  
        
        # Se elimina el enlace.
        enlaceBuscado = db.session.query(Enlaces).\
                            filter(Enlaces.idValor == identificador).\
                            first()
        if (enlaceBuscado != None):
            db.session.delete(enlaceBuscado)
            db.session.commit()
        
        # BORRAR LA HISTORIA.         
        eliminarHistoria = historia.eliminar(identificador)
        listaEliminar.append(eliminarHistoria)
        print("listaEliminar",listaEliminar)
        if (listaEliminar == [True,True,True]):
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


#.----------------------------------------------------------------------------------------.

@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, 
               {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])
    identificador = int(session['idHistoria'])

     # Atributos de la historia a crear.
    tipo = params.get('tipo', None)
    codigo = params.get('codigo', None)
    accion = params.get('accion', None) 
    objetivo = params.get('objetivos', None)
    actor = params.get('actores', None)
    idSuper = params.get('super', None)
    prioridad = params.get('prioridad', None)

    if ((tipo != None) and (codigo != None) and (accion != None) and 
        (objetivo != None) and (actor != None) and (idSuper != None)
        and (prioridad != None)):

        if (len(codigo) <= 10):

            historia = clsHistoria()
            objetivos = clsHistoriaObj()
            actores    = clsHistoriaActores()
            listaModificar   = []
        
            enlaceBuscado = db.session.query(Enlaces).\
                                filter(Enlaces.idValor == identificador).\
                                first()
    
            viejoSuper = enlaceBuscado.identificador
            #viejoSuper = enlaceEncontrado.idClave
    
            enlace = clsEnlace()
            modificacionCorrecta = enlace.modificar(viejoSuper, idSuper, 
                                                    identificador)
    
            if (modificacionCorrecta):
    
                    accionBuscada = db.session.query(Historias).\
                                        filter(Historias.idAccion == accion).\
                                        first()
            
                    if (accionBuscada == None) or (accionBuscada.identificador == identificador):
                        # BORRAR ACTORES ASOCIADOS A LA HISTORIA. 
                        modificarActor = actores.eliminar(identificador)
                        listaModificar.append(modificarActor)
                     
                        #BORRAR OBJETIVOS ASOCIADOS A LA HISTORIA.        
                        modificarObjetivo= objetivos.eliminar(identificador)
                        listaModificar.append(modificarObjetivo)
                             
                        # BORRAR LA HISTORIA.         
                        modificarHistoria = historia.eliminar(identificador)
                        listaModificar.append(modificarHistoria)
    
                        if (listaModificar == [True,True,True]):
                            historia = clsHistoria()
                            creacionCorrecta = historia.insertar(idProducto, codigo, 
                                                                 tipo, accion, idSuper, 
                                                                 prioridad) 
                
                            if ( creacionCorrecta[0] ):
                                histObjetivo = clsHistoriaObj()
                                histActores  = clsHistoriaActores()
    
                                # Se agregan los objetivos seleccionados en la base 
                                # de datos.
                                for obj in objetivo:
                                    histObjetivo.insertar(creacionCorrecta[1], obj)
                                # Se agregan los actores seleccionados en la base de 
                                # datos.
                                for act in actor:
                                    histActores.insertar(creacionCorrecta[1], act)
                                res = results[0]
                                res['label'] = res['label'] + '/' + str(idProducto)
    

    if (res == results[1]):
        res['idHistoria'] = identificador
        # Se actualiza el URL de la pág a donde se va a redirigir.
        res['label'] = res['label'] + '/' + str(identificador)

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

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    idProducto = int(session['idPila'])

    # Lista de acciones que están asociado al producto actual.
    acciones = db.session.query(Acciones).\
                filter(Acciones.idProducto == idProducto).\
                all()

    # Lista de actores que están asociado al producto actual.
    actores =   db.session.query(Actores).\
                filter(Actores.idProducto == idProducto).\
                all()
    
    objetivos = db.session.query(Objetivos).\
                    filter(Objetivos.idProducto == idProducto,
                           Objetivos.transversalidad == 0).all()

    historias = db.session.query(Historias).\
                filter(Historias.idProducto == idProducto).\
                all()

    prioridad = db.session.query(Productos).\
                filter(Productos.identificador == idProducto).all()

                
    if (prioridad[0].escala == 1):
        escalaP = 1
    elif (prioridad[0].escala == 2):
        escalaP = 2

    # Se muestra por pantalla los actores que pertenecen al producto.
    res['fHistoria_opcionesActores'] = [
      {'key':act.identificador,'value':act.nombre}
        for act in actores]

    # Se muestra por pantalla las acciones que pertenecen al producto.
    res['fHistoria_opcionesAcciones'] = [
      {'key':acc.identificador,'value':acc.descripcion}
        for acc in acciones]

    # Se muestra por pantalla los objetivos que pertenecen al producto.
    res['fHistoria_opcionesObjetivos'] = [
      {'key':obj.identificador,'value':obj.descripcion}
        for obj in objetivos]

    # Se muestra por pantalla las historias creadas.
    res['fHistoria_opcionesHistorias'] = [{'key':0,'value':'Ninguna'}]
    res['fHistoria_opcionesHistorias'] += [
      {'key': hist.identificador,'value':hist.codigo}
      for hist in historias]
    
    # Tipos de historias disponibles. 
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    
    if (escalaP == 1):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':1, 'value':'Alta'},
            {'key':2, 'value':'Media'},
            {'key':3, 'value':'Baja'},]
    elif (escalaP == 2):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':i, 'value':i}
            for i in range(1,21)]        

    res['fHistoria'] = { 'super':0,
                         'idHistoria': request.args.get('idHistoria',1),
                         'idPila': idProducto,
                         'objetivos':request.args.get('idObjetivo',1),
                         'actores': request.args.get('idActores',1),
                         'accion': request.args.get('idAccion',1),
                         'codigo': request.args.get('codigo',None),
                         'tipo': request.args.get('tipo',1),
                         'prioridad':request.args.get('escala',1)}


    # Se almacena la información recibida.  
    res['idPila'] = session['idPila']
    res['idHistoria'] = int(request.args.get('idHistoria',1))
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    idProducto = int(session['idPila'])
    identificador = int(request.args.get('idHistoria',1))
    session['idHistoria'] = identificador
    historiaActual = db.session.query(Historias).\
                        filter(Historias.identificador == identificador).\
                        first()
    print(historiaActual)


    # Se obtiene la información de la historia actual.
    historias = db.session.query(Historias).\
               filter(Historias.idProducto == idProducto).\
                all()

     # Lista de acciones que están asociado al producto actual.
    acciones =  db.session.query(Acciones).\
                filter(Acciones.idProducto == idProducto).\
                all()

    # Lista de actores que están asociado al producto actual.
    actores = db.session.query(Actores).\
                filter(Actores.idProducto == idProducto).\
                all()

    # Lista de objetivos asociados al producto actual.
    objetivos = db.session.query(Objetivos).\
                    filter(Objetivos.idProducto == idProducto,
                           Objetivos.transversalidad ==0).\
                    all()

    # Lista de prioridades asociadas al producto actual.
    prioridad = db.session.query(Productos).\
                filter(Productos.identificador == idProducto).all()
                
    if (prioridad[0].escala == 1):
        escalaP = 1
    elif (prioridad[0].escala == 2):
        escalaP = 2

    # Se muestra por pantalla los actores que pertenecen al producto.
    res['fHistoria_opcionesActores'] = [
      {'key':act.identificador,'value':act.nombre}
        for act in actores]

    # Se muestra por pantalla las acciones que pertenecen al producto.
    res['fHistoria_opcionesAcciones'] = [
      {'key':acc.identificador,'value':acc.descripcion}
        for acc in acciones]

    # Se muestra por pantalla los objetivos que pertenecen al producto.
    res['fHistoria_opcionesObjetivos'] = [
      {'key':obj.identificador,'value':obj.descripcion}
        for obj in objetivos]

     # Se muestra por pantalla las historias creadas.
    res['fHistoria_opcionesHistorias'] = [{'key':0,'value':'Ninguna'}]
    res['fHistoria_opcionesHistorias'] += [
      {'key': hist.identificador,'value':hist.codigo}
      for hist in historias]

    # Tipos de historias disponibles. 
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]

    if (escalaP == 1):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':1, 'value':'Alta'},
            {'key':2, 'value':'Media'},
            {'key':3, 'value':'Baja'},]
    elif (escalaP == 2):
        res['fHistoria_opcionesPrioridad'] = [
            {'key':i, 'value':i}
            for i in range(1,21)]       

    # Lista de actores que fueron elegidos para la historia actual
    # (antes de la modificación).
    actoresHistoria = db.session.query(ActoresHistorias).\
                        filter(ActoresHistorias.idHistoria == identificador).\
                        all()

    idActoresHistoria = [i.idActores for i in actoresHistoria]
 
    # Lista de objetivos que fueron elegidos para la historia actual 
    # (antes de la modifación).
    objetivosHistoria = db.session.query(ObjHistorias).\
                            filter(ObjHistorias.idHistoria == identificador).\
                            all()
    idObjetivosHistoria = [i.idObjetivo for i in objetivosHistoria]
    
    if (historiaActual != None):
        res['fHistoria'] = { 'super':historiaActual.idSuper if historiaActual.idSuper != None else 0,
                             'idHistoria': identificador,
                             'idPila': idProducto,
                             'objetivos':idObjetivosHistoria,
                             'actores': idActoresHistoria,
                             'accion': historiaActual.idAccion,
                             'codigo': historiaActual.codigo,
                             'tipo': int(historiaActual.tipo),
                             'prioridad':historiaActual.idEscala}

    tareas = db.session.query(Tareas).\
                        filter(Tareas.idHistoria == identificador).\
                        all()



    res['data2'] = [ 
      {'idTarea':tarea.identificador, 'descripcion':tarea.descripcion}
      for tarea in tareas
    ]

    res['idPila'] = idProducto
    res['idHistoria'] = identificador
    session['idHistoria'] = identificador
    #res['idHistoria'] = identificador

    return json.dumps(res)


#.-----------------------------------------------------------------------------.

@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProducto = int(session['idPila'])
    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']

    # Se busca el tipo de escala.
    productoTipoEscala = db.session.query(Productos.escala).\
                            filter(Productos.identificador == idProducto).\
                            first()      
    historias = db.session.query(Historias).\
                    filter(Historias.idProducto == idProducto).\
                    order_by(Historias.idEscala).all() 
    if (productoTipoEscala[0] == 1):
        escala = {1:'Alta', 2:'Media',3:'Baja'}
        res['data0'] = [
            {'idHistoria':historia.identificador, 'enunciado':historia.codigo, 
             'prioridad':escala[historia.idEscala]} 
            for historia in historias]
    else:
        res['data0'] = [
            {'idHistoria':historia.identificador, 'enunciado':historia.codigo, 
             'prioridad':historia.idEscala} 
            for historia in historias]

    res['idPila'] = idProducto
  

    
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@historias.route('/historias/VPrioridades')
def VPrioridades():
    #GET parameter
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']

    idProducto = int(session['idPila'])

    prioridad = db.session.query(Productos).\
                filter(Productos.identificador == idProducto).all()


    #Escala dependiente del proyecto
    if (prioridad[0].escala == 1):
        escalaP = 1
        
    if (prioridad[0].escala == 2):
        escalaP = 2
        
    if (escalaP == 1):
        res['fPrioridades_opcionesPrioridad'] = [
            {'key':1, 'value':'Alta'},
            {'key':2, 'value':'Media'},
            {'key':3, 'value':'Baja'},
        ]
        
    
    if (escalaP == 2):
        res['fPrioridades_opcionesPrioridad'] = [
            {'key':i, 'value':i}
            for i in range(1,21)]      

    historias = db.session.query(Historias).\
                filter(Historias.idProducto == idProducto).\
                order_by(Historias.idEscala.desc()).all()

    

    listHistorias = {}
    dicH = {}
    listH = []
    listH.append(None)
    
    for j in historias:
        idActoresHistoria = []
        idObjetivosHistoria = []
        nombreActoresHistoria = []
        nombreObjetivosHistoria = []
        
        # Lista de actores que fueron elegidos para la historia actual
        # (antes de la modificación).
        actoresHistoria = db.session.query(ActoresHistorias).\
                            filter(ActoresHistorias.idHistoria == j.identificador).\
                            all()

        for i in actoresHistoria:


            idActoresHistoria.append(i.idActores)

        for i in idActoresHistoria:
            actores = db.session.query(Actores).\
                            filter(Actores.identificador == i).\
                            all()

            nombreActoresHistoria.append(actores[0].nombre)
            print(nombreActoresHistoria)


        objetivosHistoria = db.session.query(ObjHistorias).\
                                filter(ObjHistorias.idHistoria == j.identificador).\
                                all()
        for i in objetivosHistoria:
            idObjetivosHistoria.append(i.idObjetivo)

        for i in idObjetivosHistoria:
            objetivos = db.session.query(Objetivos).\
                            filter(Objetivos.identificador == i).\
                            all()

            nombreObjetivosHistoria.append(objetivos[0].descripcion)

        accionesHistoria = db.session.query(Acciones).\
                                filter(Acciones.identificador == j.idAccion).\
                                all()


        dicH = {'id':j.identificador,
                 'actor': nombreActoresHistoria,
                 'objetivo':nombreObjetivosHistoria,
                 'accion': accionesHistoria[0].descripcion}
        listH.append(dicH)


    res['idPila'] = idProducto
    res['fPrioridades'] = {'idPila':idProducto,
      'lista':[
        {'idHistoria':hist.identificador,'prioridad':hist.idEscala, 'enunciado':'En tanto que '+str(listH[hist.identificador].get('actor')) + ' ' + 'pueda'+ ' '+ str(listH[hist.identificador].get('accion')) + ' para '+ str(listH[hist.identificador].get('objetivo')) }
          for hist in historias]}

    #Action code ends here
    return json.dumps(res)
