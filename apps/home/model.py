from database import db


class Candidato(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))    
    partido = db.Column(db.String(100))    
    numero = db.Column(db.String(100))
    votos = db.Column(db.String(128))

    def __init__(self, nome, numero, votos):
        self.nome = nome        
        self.numero = numero
        self.votos = votos