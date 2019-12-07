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
    nome_produto = db.Column(db.String)
    validade = db.Column(db.String)
    peso_produto = db.Column(db.Float)
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    pais_origem = db.Column(db.String)
    fornecedor = db.Column(db.String)
  
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
    alimento = Alimento.query.all()
    return render_template("cadastro.html", alimento=alimento)


@app.route("/cadastro", methods=['GET', 'POST']) 
def cadastro():
    alimento = Alimento.query.all()
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

    return redirect(url_for("cadastrar", alimento=alimento))

@app.route("/lista") #lista todos os imovels do db
def lista():
	alimento = Alimento.query.all()
	return render_template("lista.html", alimento=alimento)

@app.route("/pesquisa")
def pesquisa():
	nome = request.args.get('nome_produto')
	all_alimento = Alimento.query.filter(Alimento.name.contains(nome)).order_by(Alimento.nome_produto).all()
	return render_template("lista.html", alimentos = alimentos)	

@app.route("/excluir/<int:id>") 
def excluir(id):
	alimento = Alimento.query.filter_by(_id=id).first()
	db.session.delete(alimento)
	db.session.commit()

	alimentos = Alimento.query.all()
	return render_template("lista.html", alimentos=alimentos)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST']) 
def atualizar(id):
    alimento = Alimento.query.filter_by(_id=id).first()

    if request.method == 'POST' :
       
         nome_produto = request.form.get("nome_produto")
         validade = request.form.get("validade")
         peso_produto = request.form.get("peso_produto")
         preco = request.form.get("preco")
         quantidade = request.form.get("quantidade")
         pais_origem = request.form.get("pais_origem")
         fornecedor = request.form.get("fornecedor")

         if nome_produto and validade and peso_produto and preco and quantidade and pais_origem and fornecedor:
            alimento.nome_produto = nome_produto
            alimento.validade = validade
            alimento.peso_produto = peso_produto
            alimento.preco = preco
            alimento.quantidade = quantidade
            alimento.pais_origem = pais_origem
            alimento.fornecedor = fornecedor


            db.session.commit()

            return redirect(url_for("cadastrar"))
    return render_template("atualizar.html" , alimento = alimento)

"""
@app.route("/teste/<info>")
@app.route("/teste", defaults={'info':None})
def teste():
"""