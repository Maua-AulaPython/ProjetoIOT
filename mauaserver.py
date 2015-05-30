#!/usr/bin/python

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maua.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from modos import *

@app.route('/')
def index():
	return "trouxa"

if __name__ == '__main__':
	app.run(debug=True)

@app.route('/list/<id_dev>',methods=['GET'])
def measure_list(id_dev=None):
        medidas=[]
        if id_dev:
           for m in Measure.query.find(id_device=id_dev):
                print i.id,i.temperatura,i.data
                medidas.apend({'id':i.id,'temperatura':i.temperatura,'data':i.data})

           return json.dumps(medidas)


@app.route('/new')
def measure_new():
        if not request.json:
                return jsonify({'status':False})
        
        p=request.get_json()
        med=Measure()
        med.id = p['id']
        med.id_devie=p['id_device']
        med.temperatura=p['temperatura']
        med.data=p['data'];
        db.session.add(med);
        db.session.commit()

        return jsonify({'status':True})

