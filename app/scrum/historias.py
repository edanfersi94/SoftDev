# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json, redirect
from app.scrum.funcHistoria import clsHistoria
from app.scrum.funcObjetivo import clsObjetivo
from app.scrum.funcActor import clsActor
import model

historias = Blueprint('historias', __name__)


@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    #if (params =![]):
     #   newTipo = params['tipo']
    print(params)  
    if (params!=[]):
        newTipo   = params['tipo']
        newAccion = params['accion']
        objetivos = params['objetivos']
        actores   = params['actores']
        codigo    = params['codigo']
        obj       = clsObjetivo()
        act       = clsActor()
        idProducto = 1
        
        if (objetivos != []):
            for ob in objetivos:
                print("ob",type(ob),ob)
                print("producto",type(idProducto),idProducto)
                print("codigo",type(codigo),codigo)
                resultObj = obj.modify_Objetivo_Codigo(ob,idProducto,codigo)
                
                
        
    
    
    #resultInsert = nuevaHistoria.insert_Historia(nuevoCodigoHistoria,1, newTipo, nuevoAccionHistoria)
    
    #Datos de prueba
    res['label'] = res['label'] + '/1'
    
    #if(resultInsert):
        #res= results[0]
    #else:
        #res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    #Datos de prueba
    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    accionesEsp = model.Acciones.idProducto == 1
    acciones = model.db.session.query(model.Acciones).filter(accionesEsp).all()
    
    actoresEsp = model.Actores.idProducto == 1
    actores = model.db.session.query(model.Actores).filter(accionesEsp).all()
    
    objetivosEsp = model.Objetivo.idProducto == 1
    objetivos = model.db.session.query(model.Objetivo).filter(objetivosEsp).all()
    
    
    

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':act.id_actores,'value':act.descripcion_actores}
        for act in actores]
    res['fHistoria_opcionesAcciones'] = [
      {'key':acc.idacciones,'value':acc.descripAcciones}
        for acc in acciones]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':obj.idObjetivo,'value':obj.descripObjetivo}
        for obj in objetivos]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0, 
       'actor':1, 'accion':2, 'objetivo':3, 'tipo':1} 
    res['idPila'] = 1


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    accionesEsp = model.Acciones.idProducto == 1
    acciones = model.db.session.query(model.Acciones).filter(accionesEsp).all()
    
    actoresEsp = model.Actores.idProducto == 1
    actores = model.db.session.query(model.Actores).filter(accionesEsp).all()
    
    objetivosEsp = model.Objetivo.idProducto == 1
    objetivos = model.db.session.query(model.Objetivo).filter(objetivosEsp).all()
    
    
    

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':act.id_actores,'value':act.descripcion_actores}
        for act in actores]
    res['fHistoria_opcionesAcciones'] = [
      {'key':acc.idacciones,'value':acc.descripAcciones}
        for acc in acciones]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':obj.idObjetivo,'value':obj.descripObjetivo}
        for obj in objetivos]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0, 
       'actor':1, 'accion':2, 'objetivo':3, 'tipo':1} 
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    historia = model.Historia_Usuario.query.all()
    
    #Datos de prueba
    res['idPila'] = 1
    res['data0'] = [
      {'idHistoria':his.idHistoria_Usuario, 'enunciado':his.codigoHistoria_Usuario} 
      for his in historia]
    

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here