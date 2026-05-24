class Cachorro: #classe é um molde para criar objetos
    def _init_(self,nome, cor, acordado=True): #método construtor, é chamado automaticamente quando um objeto é criado
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def latir(self): #método é uma função definida dentro de uma classe, que descreve o comportamento dos objetos criados a partir da classe
        if self.acordado:
            print("Au au")
        else:
            print("Zzzzz")
cachorro1 = Cachorro("Rex", "Marrom")#criando um objeto da classe Cachorro, passando os argumentos para o método construtor
cachorro2 = Cachorro("Luna", "Preta", acordado=False)
cachorro1.latir()  # Saída: Au au
cachorro2.latir()  # Saída: Zzzzz   