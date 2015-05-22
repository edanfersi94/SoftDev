# -*- coding: utf-8 -*-
from flask              import request, session, Blueprint, json
from app.scrum.user     import clsUser

ident = Blueprint('ident', __name__)

#.------------------------------------------------------------------------------------------------.

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño de producto'], "actor":"duenoProducto"}, {'label':'/VMaestroScrum', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"}, {'label':'/VDesarrollador', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"}, {'label':'/VLogin', 'msg':['Datos de identificación incorrectos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    if request.method == 'POST':

        userInput   = clsUser()
        usuarioReq  = params['usuario']
        passwordReq = params['clave']
        lastResult  = len(results) - 1

        checkUsername = userInput.find_username(usuarioReq)
        
        if (checkUsername != []):
            print(str(checkUsername))
            checkPassword = checkUsername[0].password            
            if (checkPassword == passwordReq):
                #userActor = checkUsername.idActor
                userActor = 1

                # Puesto que los id de los actores comienzan desde el 1 entonces se resta una posicion.
                # para obtener el correspondiente.
                res = results[userActor - 1]

            else:
                res = results[lastResult]

        else:
            res = results[lastResult]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


#.------------------------------------------------------------------------------------------------.

@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VLogin', 'msg':['Felicitaciones, Ya estás registrado en la aplicación']}, {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    userInput = clsUser()
    nombreReq   = params['nombre']
    usuarioReq  = params['usuario']
    claveReq    = params['clave']
    clave2Req   = params['clave2']
    correoReq   = params['correo']

    checkUsername = userInput.find_username(usuarioReq)
    checkCorreo   = userInput.find_email(usuarioReq)


    # Falta acomodar el password
    if (checkUsername == [] and checkCorreo == [] and claveReq == clave2Req):
        print(len(usuarioReq))
        # El actor es 1 porque sera un desarrollador.
        # actorUsuario = 1
        resultInsert = userInput.insert_user(nombreReq,usuarioReq,claveReq,correoReq)
        print(resultInsert)
        if (resultInsert):
            res = results[0]
        else:
            res = results[1]

    else:
        res = results[1]


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


#.------------------------------------------------------------------------------------------------.


@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)


#.------------------------------------------------------------------------------------------------.


@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

#.------------------------------------------------------------------------------------------------.