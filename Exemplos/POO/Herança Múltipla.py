from typing import Any


class Animal:
    """
    Classe base da hierarquia. Define o atributo fundamental para todos os animais.
    
    IMPORTANTE: Em herança cooperativa (cooperative multiple inheritance),
    sempre chamamos super().__init__() para garantir que toda a cadeia MRO
    (Method Resolution Order) seja percorrida.
    """

    def __init__(self, nro_patas: int, **kw: Any):
        self.nro_patas = nro_patas
        # Propaga o **kw para cima, permitindo que outras classes na MRO
        # interceptem seus argumentos específicos.
        super().__init__(**kw)

    def __str__(self) -> str:
        # Ordena os atributos para saída previsível (em vez de __dict__ arbitrário)
        atributos = ", ".join(
            f"{chave}={valor}" for chave, valor in sorted(self.__dict__.items())
        )
        return f"{self.__class__.__name__}: {atributos}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nro_patas={self.nro_patas!r})"
        )


class Mamifero(Animal):
    """
    Herda de Animal. No contexto de herança múltipla, super() NÃO significa
    "chamar o pai direto", mas sim "próximo na MRO".
    
    Se Ornitorrinco(Mamifero, Ave) chamar super(), a ordem MRO será:
    Ornitorrinco -> Mamifero -> Ave -> Animal -> object
    Portanto, o super() de Mamifero pode apontar para Ave, não para Animal!
    """

    def __init__(self, cor_pelo: str, **kw: Any):
        self.cor_pelo = cor_pelo
        # **kw deve conter 'nro_patas' (para Animal) e possivelmente
        # 'cor_bico' (para Ave, se estiver na cadeia MRO).
        super().__init__(**kw)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(cor_pelo={self.cor_pelo!r}, nro_patas={self.nro_patas})"


class Ave(Animal):
    """
    Outra ramificação da hierarquia. Mesmo princípio cooperativo.
    """

    def __init__(self, cor_bico: str, **kw: Any):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(cor_bico={self.cor_bico!r}, nro_patas={self.nro_patas})"


class Gato(Mamifero):
    """
    Herança simples. Mamifero já gerencia o encaminhamento para Animal.
    Gato herda tudo e não precisa de atributos extras.
    """
    pass


class Ornitorrinco(Mamifero, Ave):
    """
    HERANÇA MÚLTIPLA (Diamond Problem).
    
    Ornitorrinco é mamífero E ave (biologicamente é um monotremado).
    
    MRO (Method Resolution Order) desta classe:
        Ornitorrinco -> Mamifero -> Ave -> Animal -> object
    
    Por isso, quando Ornitorrinco chama super().__init__():
        1. Vai para Mamifero.__init__ (captura cor_pelo)
        2. Mamifero chama super(), que vai para Ave.__init__ (captura cor_bico)
        3. Ave chama super(), que vai para Animal.__init__ (captura nro_patas)
        4. Animal chama super(), que vai para object (fim da cadeia)
    
    Se Animal não chamasse super(), a cadeia quebraria e Ave não seria inicializada.
    """

    def __init__(self, cor_pelo: str, cor_bico: str, nro_patas: int):
        # Passamos TODOS os argumentos nomeados. Cada classe na MRO
        # "pega" o que é seu e repassa o restante via **kw.
        super().__init__(
            cor_pelo=cor_pelo,
            cor_bico=cor_bico,
            nro_patas=nro_patas,
        )

    def __repr__(self) -> str:
        return (
            f"Ornitorrinco("
            f"cor_pelo={self.cor_pelo!r}, "
            f"cor_bico={self.cor_bico!r}, "
            f"nro_patas={self.nro_patas})"
        )


# ============================================================
# EXECUÇÃO E DEMONSTRAÇÃO
# ============================================================
if __name__ == "__main__":
    
    # --- Gato (herança simples) ---
    gato = Gato(nro_patas=4, cor_pelo="Preto")
    print(gato)
    print(f"Repr: {repr(gato)}\n")

    # --- Ornitorrinco (herança múltipla) ---
    ornitorrinco = Ornitorrinco(
        nro_patas=2,
        cor_pelo="vermelho",
        cor_bico="laranja",
    )
    print(ornitorrinco)
    print(f"Repr: {repr(ornitorrinco)}\n")

    # --- Visualizando o MRO (Method Resolution Order) ---
    print("MRO de Ornitorrinco:")
    for i, cls in enumerate(Ornitorrinco.__mro__, 1):
        print(f"  {i}. {cls.__name__}")