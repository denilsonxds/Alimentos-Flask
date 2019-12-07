"""
from alimentos import db
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class Alimento(db.Model):
    __tablename__ = "alimentos"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String, unique=True)
    validade = db.Column(db.DateTime, unique=True)
    peso_produto = db.Column(db.Float, unique=True)
    preco = db.Column(db.Float, unique=True)
    quantidade = db.Column(db.Integer, unique=True)
    pais_origem = db.Column(db.String, unique=True)
    fornecedor = db.Column(db.String, unique=True)
  
    def __init__(self, alimento):
        self.nome_produto.data = alimento.nome_produto
        self.validade.data = alimento.validade
        self.peso_produto.data = alimento.peso_produto
        self.preco.data = alimento.preco
        self.quantidade.data = alimento.quantidade
        self.pais_origem.data = alimento.pais_origem
        self.fornecedor.data = alimento.fornecedor
        

db.create_all()
"""