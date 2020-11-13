from sql_alchemy import banco

class PessoaModel(banco.Model):
    __tablename__ = 'QUEM_VAI_NO_CHURRAS'

    cpf = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    bebe = banco.Column(banco.Integer)
    convidado = banco.Column(banco.String(80))
    convidado_bebe = banco.Column(banco.Integer)


    def __init__(self, cpf, nome, bebe, convidado, convidado_bebe):
        self.cpf = cpf
        self.nome = nome
        self.bebe = bebe
        self.convidado = convidado
        self.convidado_bebe = convidado_bebe

    def json(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "bebe": self.bebe,
            "convidado": self.convidado,
            "convidado_bebe": self.convidado_bebe
        }

    @classmethod
    def find_pessoa(cls, cpf):
        pessoa = cls.query.filter_by(cpf=cpf).first() #select * from QUEM_VAI_NO_CHURRAS where cpf = cpf
        if pessoa:
            return pessoa
        return None
    
    def save_pessoa(self):
        banco.session.add(self)
        banco.session.commit()

    @classmethod
    def lista_convidados(cls):
        pessoas = cls.query.all()
        return pessoas
    
    def update_pessoa(self, nome, bebe, convidado, convidado_bebe):
        self.nome = nome
        self.bebe = bebe
        self.convidado = convidado
        self.convidado_bebe = convidado_bebe
    
    def delete_pessoa(self):
        banco.session.delete(self)
        banco.session.commit()