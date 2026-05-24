from abc import ABC, abstractmethod


# ============================================================
# PROBLEMA DO CÓDIGO ORIGINAL
# ============================================================
# Avião herdando de Passaro VIOLA o princípio da Substituição de Liskov.
# Um Avião NÃO É um Passaro biologicamente, apenas "voa" (comportamento).
# Herança deve modelar relação "É UM" (Passaro -> Pardal/Avestruz).
# Comportamentos compartilhados entre classes não-relacionadas
# devem usar interfaces/protocolos ou duck typing.


# ============================================================
# ABORDAGEM 1: Classe Abstrata para a hierarquia biológica
# ============================================================
class Passaro(ABC):
    """
    Classe abstrata que define o contrato base para todos os pássaros.
    Não pode ser instanciada diretamente.
    """
    
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def voar(self) -> None:
        """
        Método abstrato: toda subclasse DEVE implementar seu próprio voo.
        Isso impede que alguém esqueça de definir o comportamento.
        """
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.nome})"


class Pardal(Passaro):
    """Pardal é um pássaro que voa."""
    
    def voar(self) -> None:
        print(f"🐦 {self.nome} está voando alto!")


class Avestruz(Passaro):
    """
    Avestruz é um pássaro que NÃO voa.
    Mesmo assim, deve implementar o método (polimorfismo).
    """
    
    def voar(self) -> None:
        print(f"🦤 {self.nome} não pode voar, mas corre rápido!")


class Pinguim(Passaro):
    """Novo exemplo: também não voa, mas é um pássaro."""
    
    def voar(self) -> None:
        print(f"🐧 {self.nome} nada e anda, mas não voa.")


# ============================================================
# ABORDAG 2: Protocolo/Interface para "coisas que voam"
# ============================================================
class Voador(ABC):
    """
    Interface para qualquer objeto que possa executar a ação de voar.
    Usada para classes que voam mas NÃO SÃO pássaros.
    """
    
    @abstractmethod
    def voar(self) -> None:
        pass


class Aviao(Voador):
    """
    Avião implementa Voador, NÃO Passaro.
    Correto conceitualmente: Avião é uma máquina, não um animal.
    """
    
    def __init__(self, modelo: str):
        self.modelo = modelo

    def voar(self) -> None:
        print(f"✈️  {self.modelo} está decolando...")

    def __str__(self) -> str:
        return f"Avião({self.modelo})"


class Helicoptero(Voador):
    """Outro exemplo de máquina voadora."""
    
    def voar(self) -> None:
        print("🚁 Helicóptero levantando voo verticalmente!")


# ============================================================
# FUNÇÃO POLIMÓRFICA (Duck Typing)
# ============================================================
def plano_voo(obj) -> None:
    """
    Aceita QUALQUER objeto que tenha o método .voar().
    Não verifica tipo explicitamente — funciona por comportamento.
    Isso é o "duck typing" do Python: "se parece com um pato e faz quack...".
    """
    # Verificação opcional (mais robusta, mas menos pythonica):
    # if not hasattr(obj, 'voar') or not callable(getattr(obj, 'voar')):
    #     raise TypeError(f"{type(obj).__name__} não sabe voar!")
    
    print(f"\n▶️  Iniciando plano de voo para: {obj}")
    obj.voar()


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    
    # Pássaros (herança biológica correta)
    pardal = Pardal("Piu-piu")
    avestruz = Avestruz("Zazu")
    pinguim = Pinguim("Skipper")
    
    # Máquinas (interface de comportamento)
    aviao = Aviao("Boeing 747")
    helicoptero = Helicoptero()
    
    # Todos funcionam no plano_voo graças ao polimorfismo!
    entidades = [pardal, avestruz, pinguim, aviao, helicoptero]
    
    for entidade in entidades:
        plano_voo(entidade)

    # Tentativa de instanciar Passaro diretamente (erro proposital):
    # passaro = Passaro("Generico")  
    # TypeError: Can't instantiate abstract class Passaro with abstract method voar