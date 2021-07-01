from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='bia', idade=18)
    print(pessoa)
    pessoa.save()

# Insere dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='jaque').first()
    print(pessoa.nome)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ana').first()
    pessoa.nome = 'Rafael'
    pessoa.save()

# Deleta dados na tabela pessoa
def delete_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ana').first()
    pessoa.delete()



if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoa()
    #delete_pessoa()
