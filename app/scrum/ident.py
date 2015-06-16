# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        Módulo que contiene los métodos que permitirán insertar, modificar y
        eliminar acciones.
"""

#.-----------------------------------------------------------------------------.

from app.scrum.user import clsUser
from flask import request, session, Blueprint, json
from app.scrum.controlDeAcceso import clsControlDeAcceso

ident = Blueprint('ident', __name__)

#.-----------------------------------------------------------------------------.

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():

    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño de producto'], "actor":"duenoProducto"}, 
               {'label':'/VMaestroScrum', 'msg':['Bienvenido Maestro Scrum'],  "actor":"maestroScrum"}, 
               {'label':'/VDesarrollador','msg':['Bienvenido Desarrollador'], "actor":"desarrollador"}, 
               {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    # Resultado de la autenticación del usuario.
    lastResult  = len(results) - 1
    res = results[lastResult]

    # Parámetros para autenticar al usuario.
    usuarioSolicitado  = params.get('usuario', None)
    claveSolicitada = params.get('clave', None)
    
    if ( usuarioSolicitado != None and claveSolicitada != None ):

        usuario = clsUser()
        usuarioExiste = usuario.buscarUsername(usuarioSolicitado)

        if (usuarioExiste != None):
            claveAsociada = usuarioExiste.clave   
            controlDeAcceso = clsControlDeAcceso()
            claveEncriptada = controlDeAcceso.encriptar(claveAsociada)
            resultadoVerificacion = controlDeAcceso.verificarPassword(claveEncriptada, 
                                                                      claveSolicitada)
            if ( resultadoVerificacion ):
                if params['usuario'] == 'yoda':
                    session['usuario'] = usuarioSolicitado
                    res = results[1]
                elif params['usuario'] == 'hans':
                    session['usuario'] = usuarioSolicitado
                    res = results[2]
                    
                else:
                    session['usuario'] = usuarioSolicitado
                    res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():

    params = request.get_json()
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']},
               {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, ]
    res = results[1]

    # Campos correspondiente a la registración del usuario.
    nombreUsuario = params['nombre']
    username = params['usuario']
    clave = params['clave']
    claveRepetida = params['clave2']
    correo = params['correo']

    usuario = clsUser()
    verificarUsuario = usuario.buscarUsername(nombreUsuario)
    verificarCorreo  = usuario.buscarCorreo(correo)

    controlDeAcceso = clsControlDeAcceso()
    claveEncriptada = controlDeAcceso.encriptar(clave)
    resultadoVerificacion = controlDeAcceso.verificarPassword(claveEncriptada, 
                                                            claveRepetida)

    if ( verificarUsuario == None and verificarCorreo == None and resultadoVerificacion):
        resultadoCreacion = usuario.insertar(nombreUsuario, username, 
                                                    clave, correo)
        if ( resultadoCreacion ):
            res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    session.pop('usuario', None)
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.