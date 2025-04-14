from pessoa import Pessoa

def main():
    pessoas = []
    qtd = int(input('quantas pessoas quer cadastrar: '))

    for i in range(qtd):
        nome = input("Nome: ")
        idade = input("Idade: ")
        pessoa = Pessoa(nome, idade)
        pessoas.append(pessoa)

    print ('Apresentando pessoas:')
    for p in pessoas:
        p.apresentar()

if __name__ == "__main__":
    main()
