# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

historias = Blueprint('historias', __name__)


@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
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

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]
    res['fHistoria'] = {'super':0}
    res['idPila'] = 1


    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Ejemplo de relleno de listas para selectrores
    res['fHistoria_opcionesActores'] = [
      {'key':1,'value':'Actor1'},
      {'key':2,'value':'Actor2'},
      {'key':3,'value':'Actor3'}]
    res['fHistoria_opcionesAcciones'] = [
      {'key':1,'value':'Acccion1'},
      {'key':2,'value':'Acccion2'},
      {'key':3,'value':'Acccion3'}]
    res['fHistoria_opcionesObjetivos'] = [
      {'key':1,'value':'Objetivo1'},
      {'key':2,'value':'Objetivo2'},
      {'key':3,'value':'Objetivo3'}]
    res['fHistoria_opcionesHistorias'] = [
      {'key':0,'value':'Ninguna'},
      {'key':1,'value':'Historia1'},
      {'key':2,'value':'Historia2'},
      {'key':3,'value':'Historia3'}]
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

    #Datos de prueba
    res['idPila'] = 1
    res['data0'] = [
      {'idHistoria':1, 'enunciado':'En tanto que picho podría tomar agua para saciar mi sed'}]
    

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here