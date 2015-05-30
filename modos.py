from mauaserver import db

class Device(db.Model):
    id= db.Column(db.Integer,primary_key = True)
    nome=db.Column(db.String(20))


class Measure(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    id_device=db.Column(db.Integer,db.ForeignKey('Device.id'))
    temperatura=db.Column(db.Float)
    data=db.Column(db.DateTime)
    
