class Estudante:
    """
    Demonstra atributos de CLASSE (compartilhados) vs. atributos de INSTÂNCIA (exclusivos).
    
    RESOLUÇÃO DE NOMES EM PYTHON:
    Quando acessamos 'obj.atributo', Python procura:
        1. No __dict__ da instância
        2. No __dict__ da classe (e nas superclasses)
    
    Por isso, 'self.escola' encontra 'Estudante.escola' se não houver
    um 'self.escola' definido no __init__.
    """

    escola = "DIO"  # Atributo de CLASSE: compartilhado por TODAS as instâncias

    def __init__(self, nome: str, matricula: int):
        self.nome = nome           # Atributo de INSTÂNCIA: exclusivo de cada objeto
        self.matricula = matricula  # Atributo de INSTÂNCIA

    def __str__(self) -> str:
        return f"{self.nome} (matrícula {self.matricula}) — Escola: {self.escola}"

    def __repr__(self) -> str:
        return (
            f"Estudante("
            f"nome={self.nome!r}, "
            f"matricula={self.matricula!r}, "
            f"escola={self.escola!r})"
        )

    @classmethod
    def alterar_escola(cls, nova_escola: str) -> None:
        """
        Altera o atributo de classe de forma controlada.
        
        IMPORTANTE: isso afeta TODAS as instâncias que ainda não
        possuírem um atributo de instância chamado 'escola'.
        """
        print(f"\n🏫 Alterando escola da classe: {cls.escola!r} → {nova_escola!r}")
        cls.escola = nova_escola

    def ingressar_nova_escola(self, nova_escola: str) -> None:
        """
        Cria um atributo de INSTÂNCIA chamado 'escola', que SOBRESCREVE
        (shadowing) o atributo de classe apenas para ESTE objeto.
        
        A partir daqui, self.escola NÃO MAIS reflete Estudante.escola.
        """
        print(f"\n🎓 {self.nome} está mudando de escola individualmente...")
        self.escola = nova_escola  # Agora existe em self.__dict__!


def mostrar_valores(*estudantes: Estudante) -> None:
    """Exibe os dados de cada estudante e seus dicionários internos."""
    print("\n" + "=" * 50)
    for est in estudantes:
        print(f"\n📌 {est}")
        print(f"   __dict__ da instância: {est.__dict__}")
        print(f"   'escola' está em __dict__? {'escola' in est.__dict__}")
        print(f"   'escola' na classe:      {Estudante.escola!r}")


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":

    # --- Fase 1: Instâncias compartilham o atributo de classe ---
    print("=" * 50)
    print("FASE 1: Atributo de classe compartilhado")
    aluno_1 = Estudante("Guilherme", 1)
    aluno_2 = Estudante("Giovanna", 2)
    mostrar_valores(aluno_1, aluno_2)

    # --- Fase 2: Alterar atributo de classe afeta TODOS ---
    # (exceto instâncias que já possuam 'escola' em seu __dict__)
    Estudante.alterar_escola("Python")
    
    aluno_3 = Estudante("Chappie", 3)
    mostrar_valores(aluno_1, aluno_2, aluno_3)

    # --- Fase 3: Shadowing — atributo de instância sobrescreve o de classe ---
    aluno_1.ingressar_nova_escola("DIO Premium")
    mostrar_valores(aluno_1, aluno_2, aluno_3)

    # --- Fase 4: Alterar a classe NOVAMENTE ---
    # Note que aluno_1 NÃO muda, pois agora tem 'escola' em seu __dict__
    Estudante.alterar_escola("Data Science")
    mostrar_valores(aluno_1, aluno_2, aluno_3)