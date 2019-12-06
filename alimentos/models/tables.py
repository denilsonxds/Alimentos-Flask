from alimentos import db
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class Fornecedor(db.Model):
    __tablename__ = "fornecedores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, unique=True)
    cnpj = db.Column(db.String, unique=True)
    telefone = db.Column(db.String, unique=True)

    def __ini__(self, nome, cnpj, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone

    
    def __repr__(self):
        return "<Fornecedor %r>" % self.nome


class Alimento(db.Model):
    __tablename__ = "alimentos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String, unique=True)
    validade = db.Column(db.DateTime, unique=True)
    peso_produto = db.Column(db.Float, unique=True)
    preco = db.Column(db.Float, unique=True)
    quantidade = db.Column(db.Integer, unique=True)
    pais_origem = db.Column(db.String, unique=True)
    fornecedor_id = db.Column(db.String, db.ForeignKey('fornecedores.id'))

    fornecedor = db.relationship('Fornecedor', foreign_keys=fornecedor_id)

    def __init__(self, nome_produto, validade, quantidade, fornecedor_id, preco):
        self.nome_produto = nome_produto
        self.validade = validade
        self.quantidade = quantidade
        self.fornecedor_id = fornecedor_id
        self.preco = preco
    
    def __repr__(self):
        return "<Alimento %r>" % self.nome_produto



db.create_all()