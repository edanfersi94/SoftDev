# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

dev = Blueprint('dev', __name__)


@dev.route('/dev/VDesarrollador')
def VDesarrollador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here