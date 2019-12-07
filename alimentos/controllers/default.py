from alimentos import app
from flask.templating import render_template
from flask import request, redirect, url_for
from alimentos.models.forms import *
from wtforms.fields import DateField
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from alimentos import db




class Alimento(db.Model):
    __tablename__ = "alimentos"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String, unique=True)
    validade = db.Column(db.String, unique=True)
    peso_produto = db.Column(db.Float, unique=True)
    preco = db.Column(db.Float, unique=True)
    quantidade = db.Column(db.Integer, unique=True)
    pais_origem = db.Column(db.String, unique=True)
    fornecedor = db.Column(db.String, unique=True)
  
    def __init__(self, nome_produto, validade, peso_produto, preco, quantidade, pais_origem, fornecedor):
        self.nome_produto = nome_produto
        self.validade = validade
        self.peso_produto = peso_produto
        self.preco = preco
        self.quantidade = quantidade
        self.pais_origem = pais_origem
        self.fornecedor = fornecedor
        

db.create_all()


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/cadastrar/") #rota de cadastro
def cadastrar():
	return render_template("cadastro.html")


@app.route("/cadastro", methods=['GET', 'POST']) 
def cadastro():
    if request.method == "POST":
        nome_produto = request.form.get("nome_produto")
        validade = request.form.get("validade")
        peso_produto = request.form.get("peso_produto")
        preco = request.form.get("preco")
        quantidade = request.form.get("quantidade")
        pais_origem = request.form.get("pais_origem")
        fornecedor = request.form.get("fornecedor")

        if nome_produto and validade and peso_produto and preco and quantidade and pais_origem and fornecedor:
            p = Alimento(nome_produto, validade, peso_produto, preco, quantidade, pais_origem, fornecedor)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("home"))



"""
@app.route("/teste/<info>")
@app.route("/teste", defaults={'info':None})
def teste():
"""