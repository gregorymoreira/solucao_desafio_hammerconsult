from flask import Flask
from flask_restful import Api
from resources.pessoa import Pessoa, Funcionarios, Convidados, GastoTotal, GastoComida, GastoBebida

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Funcionarios, '/ListarFuncionarios') #get
api.add_resource(Pessoa, '/ConfirmarPresenca/<int:cpf>') #post get delete
api.add_resource(Convidados, '/ListarConvidados') #get
api.add_resource(GastoTotal, '/ExibirGastosTotais')
api.add_resource(GastoComida, '/ExibirGastosComida')
api.add_resource(GastoBebida, '/ExibirGastosBebida')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)