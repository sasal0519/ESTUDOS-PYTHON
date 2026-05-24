class Conta:
    """
    Representa uma conta bancária com encapsulamento de saldo.
    """

    def __init__(self, nro_agencia: str, saldo: float = 0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo  # atributo protegido

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual da conta."""
        return self._saldo

    def depositar(self, valor: float) -> None:
        """
        Deposita um valor na conta.
        
        Args:
            valor: Quantia a ser depositada (deve ser positiva).
        
        Raises:
            ValueError: Se o valor for negativo ou zero.
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        """
        Saca um valor da conta.
        
        Args:
            valor: Quantia a ser sacada (deve ser positiva).
        
        Raises:
            ValueError: Se o valor for negativo ou zero.
            ValueError: Se houver saldo insuficiente.
        """
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError(f"Saldo insuficiente. Saldo atual: R${self._saldo:.2f}")
        self._saldo -= valor

    def __str__(self) -> str:
        return f"Conta(agência={self.nro_agencia}, saldo=R${self._saldo:.2f})"

    def __repr__(self) -> str:
        return f"Conta(nro_agencia='{self.nro_agencia}', saldo={self._saldo})"


# --- Uso ---
conta = Conta("0001", 100)
conta.depositar(100)

print(conta.nro_agencia)   # 0001
print(conta.saldo)         # 200.0  (agora é uma property, não precisa de ())

# Tentativas inválidas (descomente para testar):
# conta.depositar(-50)     # ValueError
# conta.sacar(999)         # ValueError: Saldo insuficiente