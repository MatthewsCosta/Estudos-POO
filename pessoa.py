class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá eu sou{self.nome} e tenho {self.idade}')
