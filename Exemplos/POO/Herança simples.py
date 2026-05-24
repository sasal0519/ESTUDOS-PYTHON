class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")

    def ligar_motor(self):
        print("O motor do veículo está ligado.")    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, numero_portas):
        super().__init__(marca, modelo, ano, cor)  # Chamando o construtor da classe base (Veiculo) para inicializar os atributos herdados.
        self.numero_portas = numero_portas  # Atributo específico da classe Carro para armazenar o número de portas do carro.

    def exibir_informacoes(self):
        super().exibir_informacoes()  # Chamando o método exibir_informacoes da classe base para exibir as informações comuns do veículo.
        print(f"Número de Portas: {self.numero_portas}")  # Exibindo a informação específica do carro sobre o número de portas.
    
    def abrir_portas(self):
        print("As portas do carro estão abertas.")
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, tipo_moto):
        super().__init__(marca, modelo, ano, cor)  # Chamando o construtor da classe base (Veiculo) para inicializar os atributos herdados.
        self.tipo_moto = tipo_moto  # Atributo específico da classe Moto para armazenar o tipo da moto (ex: esportiva, cruiser, etc.).

    def exibir_informacoes(self):
        super().exibir_informacoes()  # Chamando o método exibir_informacoes da classe base para exibir as informações comuns do veículo.
        print(f"Tipo de Moto: {self.tipo_moto}")  # Exibindo a informação específica da moto sobre o tipo de moto.
    
    def empinar(self):
        print("A moto está empinando.")
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cor, capacidade_carga):
        super().__init__(marca, modelo, ano, cor)  # Chamando o construtor da classe base (Veiculo) para inicializar os atributos herdados.
        self.capacidade_carga = capacidade_carga  # Atributo específico da classe Caminhao para armazenar a capacidade de carga do caminhão.

    def exibir_informacoes(self):
        super().exibir_informacoes()  # Chamando o método exibir_informacoes da classe base para exibir as informações comuns do veículo.
        print(f"Capacidade de Carga: {self.capacidade_carga} kg")  # Exibindo a informação específica do caminhão sobre a capacidade de carga.
    
    def carregar(self):
        print("O caminhão está carregando.")
carro1 = Carro("Toyota", "Corolla", 2020, "Prata", 4)
moto1 = Moto("Honda", "CB500", 2019, "Vermelha", "Esportiva")
caminhao1 = Caminhao("Volvo", "FH16", 2021, "Branco", 20000)
carro1.exibir_informacoes()
carro1.ligar_motor()
carro1.abrir_portas()
print("\n")
moto1.exibir_informacoes()
moto1.ligar_motor() 
moto1.empinar()
print("\n")
caminhao1.exibir_informacoes()
caminhao1.ligar_motor()
caminhao1.carregar()  