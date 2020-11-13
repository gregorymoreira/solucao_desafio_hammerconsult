from flask_restful import Resource, reqparse
from models.pessoa import PessoaModel
import sqlite3


pessoas = [
    {
        "cpf": 33333333333,
        "nome": "greg",
        "bebe": 1,
        "convidado": "ana",
        "convidado_bebe": 1
    }
]

class Funcionarios(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        consulta = "SELECT nome FROM QUEM_VAI_NO_CHURRAS"
        res_consulta = cursor.execute(consulta)
        
        funcionarios = []
        for linha in res_consulta:
            funcionarios.append({
                'nome': linha[0]
            })

        return {'funcionarios': funcionarios}

class Convidados(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        consulta = "SELECT convidado FROM QUEM_VAI_NO_CHURRAS"
        res_consulta = cursor.execute(consulta)

        convidados = []
        for linha in res_consulta:
            if linha[0] is not None:
                convidados.append({
                    'nome': linha[0]
                })
        return {'convidados': convidados}

class Pessoa(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('bebe')
    atributos.add_argument('convidado')
    atributos.add_argument('convidado_bebe')
    
    def post(self, cpf):
        if PessoaModel.find_pessoa(cpf):
            return {"message":"Cpf '{}' ja existe.".format(cpf)}, 400

        dados = Pessoa.atributos.parse_args()
        pessoa = PessoaModel(cpf, **dados)
        pessoa.save_pessoa()
        return pessoa.json()
    
    def get(self, cpf):
        pessoa = PessoaModel.find_pessoa(cpf)
        if pessoa:
            return pessoa.json()
        return {'message': 'Not found'}, 404

    def put(self, cpf):
        dados = Pessoa.atributos.parse_args()
        pessoa_encontrada = PessoaModel.find_pessoa(cpf)

        if pessoa_encontrada:
            pessoa_encontrada.update_pessoa(**dados)
            pessoa_encontrada.save_pessoa()
            return pessoa_encontrada.json(), 200
        pessoa = PessoaModel(cpf, **dados)
        pessoa.save_pessoa()
        return pessoa.json(), 201

    def delete(self, cpf):
        pessoa = PessoaModel.find_pessoa(cpf)
        if pessoa:
            pessoa.delete_pessoa()
            return {'message': 'Pessoa deletada!'}
        return {'message': 'Pessoa nao encontrada!'}, 404

class GastoTotal(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        gasto = 0
        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE bebe = 1"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*20)
        

        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE convidado_bebe = 1"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*20)

        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE bebe = 0"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*10)

        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE convidado_bebe = 0"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*10)

        return {'gastoTotal': gasto}

class GastoComida(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        gasto = 0
        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE convidado IS NOT NULL"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*20)
        
        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE convidado IS NULL"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*10)

        return {'gastoComida': gasto}

class GastoBebida(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        gasto = 0
        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE bebe = 1"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*10)

        consulta = "SELECT count(*) FROM QUEM_VAI_NO_CHURRAS WHERE convidado_bebe = 1"
        res_consulta = cursor.execute(consulta)
        for linha in res_consulta:
            gasto += (linha[0]*10)

        return {'gastoBebida': gasto}