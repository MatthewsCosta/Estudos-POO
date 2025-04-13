class Pessoa:
    def __init__(self, nome="", sexo="", idade=0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def cadastrar_pessoa(self):
        self.nome = input('Digite seu nome: ')
        self.sexo = input('Digite seu sexo: ')
        self.idade = input('Digite sua idade: ')

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}, sou do sexo {self.sexo}, e tenho {self.idade} anos.")


pessoa1 = Pessoa()
pessoa2 = Pessoa()

pessoa1.cadastrar_pessoa()
pessoa2.cadastrar_pessoa()

pessoa1.apresentar()
pessoa2.apresentar()