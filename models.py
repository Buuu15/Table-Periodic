from app import db

class Element(db.Model):
    atomic_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    symbol = db.Column(db.String(5))
    atomic_mass = db.Column(db.Float)
    category = db.Column(db.String(50))
    group = db.Column(db.Integer)
    period = db.Column(db.Integer)
