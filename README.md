# solucao_desafio_hammerconsult

A implementação da solução para o desafio foi realizada utilizando a linguagem Python com Flask e banco de dados sqlite, com as seguintes dependências necessárias:
* aniso8601==8.0.0
* click==7.1.2
* Flask==1.1.2
* Flask-RESTful==0.3.8
* Flask-SQLAlchemy==2.4.4
* itsdangerous==1.1.0
* Jinja2==2.11.2
* MarkupSafe==1.1.1
* pytz==2020.4
* six==1.15.0
* SQLAlchemy==1.3.20
* Werkzeug==1.0.1

Rodando a aplicação localmente com o comando : 'python app.py', os endpoints podem ser consumidos.
Para o problema, temos:

* Participar do Churrasco                         -> /ConfirmarPresenca/<int:cpf> -> POST
* Cancelar participação do Churrasco              -> /ConfirmarPresenca/<int:cpf> -> DELETE
* Cancelar participação do convidado no Churrasco -> /ConfirmarPresenca/<int:cpf> -> PUT

Os endpoints acima foram desenvolvidos com uma projeção de utilizar o cpf como chave primária informada sempre pela URL, com os outros parâmetros sendo passados por JSON e conseguir operar para qualquer situação. Um convidado não pode ir sem a pessoa que o convidou para a festa, mas um funcionário pode ir ao churras sem um convidado.

Os atributos que podem ser passados são:\\
    {\\
        "nome": "STRING",\\
        "bebe": "INTEGER",\\
        "convidado": "STRING",\\
        "convidado_bebe": "INTEGER"\\
    }\\
    
Os atributos "bebe" e "convdado_bebe" foram desenvolvidos em uma proposta de "SIM" e "NAO" equivalendo a 1 e 0 respectivamente.

* Listar Participantes -> /ListarFuncionarios -> GET
* Listar Convidados    -> /ListarConvidados -> GET

Os nomes dos funcionários que vão ao churras e o nome dos convidados são exibidos, respectivamente.

* Total Arrecadado       -> /ExibirGastosTotais -> GET
* Total Gasto em Comida  -> /ExibirGastosComida -> GET
* Total Gasto em Bebida  -> /ExibirGastosBebida -> GET

Apenas os valores totais são exibidos com os endpoints acima.
