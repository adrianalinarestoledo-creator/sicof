from app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    gerencia = db.Column(db.String(20), nullable=False)  # GAL, GAF, GSMA, GPSOI, GSTS, DG, ADMIN
    rol = db.Column(db.String(20), nullable=False)       # admin, dg, gerencia
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nombre} - {self.gerencia}>"

