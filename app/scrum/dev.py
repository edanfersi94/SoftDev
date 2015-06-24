# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

dev = Blueprint('dev', __name__)


@dev.route('/dev/VDesarrollador')
def VDesarrollador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
        
    return json.dumps(res)
