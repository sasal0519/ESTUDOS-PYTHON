class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}"


nome = input()
idade = int(input())
pessoa = Pessoa(nome, idade)
print(pessoa)  # Nome: Mary Silva, Idade: 32