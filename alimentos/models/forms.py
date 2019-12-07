from flask_wtf import Form
from wtforms import StringField, IntegerField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class AlimentoForm(Form):
    nome_produto = StringField("nome_produto")
    validade = DateField("validade", format='%Y-%m-%d')
    fornecedor = StringField("fornecedor")
    peso = FloatField("peso", default=None)
    preco = FloatField("preco")
    quantidade = IntegerField("quantidade")
    pais_origem = StringField("pais_origem")
    
