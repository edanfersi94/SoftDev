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
        tareas de la historia.
"""



#.-----------------------------------------------------------------------------.
from flask import request, session, Blueprint, json
from app.scrum.funcTarea import clsTarea
from model import db,Tareas, Historias, Categorias

tareas = Blueprint('tareas', __name__)


@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VCrearTarea', 'msg':['No se pudo crear tarea.']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idHistoria = int(session['idHistoria'])
    descripcion = params.get('descripcion', None)
    idCategoria = params.get('categoria',None)
    peso = params.get('peso',None)

    if (( descripcion != None ) and ( idCategoria != None ) and ( peso != None )):
        tarea = clsTarea()

        creaccionCorrecta = tarea.insertar(idHistoria,descripcion,idCategoria,peso)
        print("creacionCorrecta",creaccionCorrecta)
        if (creaccionCorrecta[0]):
            res = results[0]
            res['label'] = res['label'] + '/' + repr(idHistoria)

        if (res == results[1]):
            res['label'] = res['label'] + '/' + repr(idHistoria)

    res['idHistoria'] = idHistoria 
    res['idTarea']= creaccionCorrecta[1]
     
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AElimTarea')
def AElimTarea():
    #POST/PUT parameters
    params = request.get_json()
    idHistoria = int(session['idHistoria'])
    identificador = int(session['idTarea'])
    #identificador = int (request.args.get('idTarea',1))
    results = [{'label':'/VHistoria', 'msg':['Tarea borrada']}, {'label':'/VTarea', 'msg':['No se pudo eliminar esta tarea']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    if not(( identificador == None )):
        tarea = clsTarea()
        eliminacionCorrecta = tarea.eliminar(identificador)

        if (eliminacionCorrecta):
            res = results[0]
            res['label'] = res['label'] + '/' + str(idHistoria)

        if (res == results[1]):
            res['label'] = res['label'] + '/' + str(identificador)


    res['idHistoria'] = idHistoria 
    

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AModifTarea', methods=['POST'])
def AModifTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea modificada']}, {'label':'/VCrearTarea', 'msg':['No se pudo modificar esta tarea.']}, ]
    res = results[1]

    idHistoria = int(session['idHistoria'])
    descripcion = params.get('descripcion', None)
    idCategoria = params.get('categoria',None)
    peso = params.get('peso',None)

    identificador = params.get('idTarea',None)

    if not(( descripcion == None ) and ( idCategoria == None ) and ( peso == None )):

        tarea = clsTarea()
        modificacionCorrecta = tarea.modificar(identificador,descripcion,idCategoria,peso)

        if(modificacionCorrecta):
            res = results[0]
            res['label'] = res['label'] + '/' + repr(idHistoria)

        if (res == results[1]):
            res['label'] = res['label'] + '/' + repr(identificador)

    res['idHistoria'] = idHistoria 
        
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/VCrearTarea')
def VCrearTarea():
    #GET parameter

    idHistoria = int(request.args.get('idHistoria'))
    codigoBuscado = db.session.query(Historias).\
                    filter(Historias.identificador == idHistoria).first()

    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = codigoBuscado.codigo
    session['idHistoria'] = idHistoria
    
    categoriasBuscadas = db.session.query(Categorias).all()
    primeraCategoria   = db.session.query(Categorias).first()
    res['fTarea_opcionesCategoria'] = [
      {'key':cat.identificador, 'value':cat.nombre, 'peso':cat.peso}
       for cat in categoriasBuscadas]
    res['fTarea'] = {'idHistoria':idHistoria, 'idTarea': request.args.get('idTarea',1),
                     'descripcion':request.args.get('descripcion',None),
                     'categoria':request.args.get('categoria', primeraCategoria.identificador), 
                     'peso':request.args.get('peso',primeraCategoria.peso)}  
    res['idHistoria'] = idHistoria 
    #Action code ends here
    return json.dumps(res)



@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter
    identificador = int (request.args.get('idTarea',1))
    idHistoria = int(session['idHistoria'])

    descripcionBuscada = db.session.query(Tareas).\
                         filter(Tareas.identificador == identificador).first()
    
    codigoBuscado = db.session.query(Historias).\
                    filter(Historias.identificador == idHistoria).first()
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    res['fTarea'] = {'idTarea': identificador,
                     'descripcion': descripcionBuscada.descripcion}

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = codigoBuscado.codigo
    
    categoriasBuscadas = db.session.query(Categorias).all()
    tareaBuscada = db.session.query(Tareas).\
                        filter(Tareas.identificador == identificador).\
                        first()   
    idCategoria = tareaBuscada.idCategoria
    categorias = db.session.query(Categorias).\
                filter(Categorias.identificador == idCategoria).\
                first()
                        
    print("peso",tareaBuscada.peso)
    
    res['fTarea'] = {'idHistoria':idHistoria, 'idTarea':identificador,
                     'descripcion':tareaBuscada.descripcion,
                    'categoria':idCategoria, 'peso':tareaBuscada.peso}  
  
    res['fTarea_opcionesCategoria'] = [
            {'key':cat.identificador, 'value':cat.nombre, 'peso':tareaBuscada.peso}
            for cat in categoriasBuscadas]
    
    session['idTarea'] = identificador
    res['idTarea'] = identificador
    res['idHistoria'] = idHistoria 
    #Action code ends here
    return json.dumps(res)