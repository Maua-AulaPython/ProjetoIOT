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
	return "Hello World! Rotas: [/list/<id_device>]-lista as medidas de todos ou um so device- e [/new]-grava nova medida"
      


@app.route('/list/<id_dev>',methods=['GET'])
def measure_list(id_dev=None):
        medidas=[]
        if id_dev:
           for m in Measure.query.filter(Measure.id_device==id_dev):
                print m.id,m.temperatura,m.data
                medidas.apend({'id':m.id,'temperatura':m.temperatura,'data':m.data})
        else:
           for i in Measure.query.all():
                print i.id,i.temperatura,i.data
                medidas.apend({'id':i.id,'id_device':i.id_device,'temperatura':i.temperatura,'data':i.data})     

        return json.dumps(medidas)


@app.route('/new',methods=['GET'])
def measure_new():
        if not request.json:
                return jsonify({'status':False})
        
        p=request.get_json()
        med=Measure()
        med.id = p['id']
        med.id_device=p['id_device']
        med.temperatura=p['temperatura']
        med.data=p['data'];
        db.session.add(med);
        db.session.commit()

        return jsonify({'status':True})

if __name__ == '__main__':
	app.run(debug=True)
