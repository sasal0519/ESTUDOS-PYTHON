class Bicicleta:#Definindo a classe Bicicleta
    def __init__(self, marca, modelo, ano, cor):#Definindo o método construtor da classe, que é chamado automaticamente quando um objeto é criado a partir da classe. Ele recebe os parâmetros marca, modelo, ano e cor, e os atribui aos atributos do objeto usando self.
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):#Definindo o método exibir_informacoes, que exibe as informações da bicicleta. Ele acessa os atributos do objeto usando self e imprime as informações formatadas.
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")  
    def buzinar(self):
        print("Buzinando: Biiiiip!")  

    def parar(self):#Definindo o método parar, que exibe uma mensagem indicando que a bicicleta está parando. Ele é um método de instância, ou seja, é chamado a partir de um objeto específico da classe.
        print("A bicicleta parando.")
        print("A bicicleta parou.")

    def correr(self):    #Definindo o método correr, que exibe uma mensagem indicando que a bicicleta está correndo. Ele é um método de instância, ou seja, é chamado a partir de um objeto específico da classe.
        print("A bicicleta está correndo.")
bicicleta1 = Bicicleta("Caloi", "Elite", 2020, "Vermelha")
bicicleta2 = Bicicleta("Specialized", "Rockhopper", 2021, "Azul")#Criando dois objetos da classe Bicicleta, passando os argumentos para o método construtor. Cada objeto tem suas próprias informações de marca, modelo, ano e cor.
bicicleta3 = Bicicleta("Trek", "Marlin 7", 2022, "Preta")
bicicleta1.buzinar()
bicicleta2.correr()
bicicleta1.exibir_informacoes()
bicicleta2.exibir_informacoes()
Bicicleta.parar(bicicleta3)#Chamando o método parar da classe Bicicleta, passando o objeto bicicleta3 como argumento. Isso é equivalente a chamar bicicleta3.parar(), mas usando a sintaxe da classe.