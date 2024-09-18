from database import db


class Candidato(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))    
    partido = db.Column(db.String(100))    
    numero = db.Column(db.Integer)
    votos = db.Column(db.Integer)

    def __init__(self, nome, partido, numero, votos=1):
        self.nome = nome        
        self.partido = partido
        self.numero = numero
        self.votos = votos