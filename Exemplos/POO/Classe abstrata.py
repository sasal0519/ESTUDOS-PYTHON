from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    """
    Classe Abstrata Base (ABC).
    
    NÃO pode ser instanciada diretamente. Serve como 'contrato':
    toda subclasse DEVE implementar os métodos/propriedades marcados
    com @abstractmethod, senão também será abstrata.
    """

    @abstractmethod
    def ligar(self) -> None:
        """Contrato: como ligar o aparelho."""
        pass

    @abstractmethod
    def desligar(self) -> None:
        """Contrato: como desligar o aparelho."""
        pass

    @property
    @abstractmethod
    def marca(self) -> str:
        """
        Propriedade abstrata.
        
        A ordem dos decorators importa: @property por fora, @abstractmethod por dentro.
        Isso define que 'marca' deve ser implementada como @property nas subclasses.
        """
        pass


class ControleTV(ControleRemoto):
    """Implementação concreta para televisão."""

    def ligar(self) -> None:
        print("📺 Ligando a TV...")
        print("   TV Ligada!")

    def desligar(self) -> None:
        print("📺 Desligando a TV...")
        print("   TV Desligada!")

    @property
    def marca(self) -> str:
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    """Implementação concreta para ar condicionado."""

    def ligar(self) -> None:
        print("❄️  Ligando o Ar Condicionado...")
        print("   Ar Ligado!")

    def desligar(self) -> None:
        print("❄️  Desligando o Ar Condicionado...")
        print("   Ar Desligado!")

    @property
    def marca(self) -> str:
        return "LG"


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    
    # Polimorfismo: tratamos objetos diferentes pela mesma interface
    controles: list[ControleRemoto] = [
        ControleTV(),
        ControleArCondicionado(),
    ]

    for controle in controles:
        print(f"\n🔌 Controle {controle.marca}:")
        controle.ligar()
        controle.desligar()

    # Tentativa de instanciar a classe abstrata (erro proposital):
    # c = ControleRemoto()  
    # TypeError: Can't instantiate abstract class ControleRemoto 
    #            with abstract methods desligar, ligar, marca