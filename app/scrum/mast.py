# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

mast = Blueprint('mast', __name__)


@mast.route('/mast/VMaestroScrum')
def VMaestroScrum():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here