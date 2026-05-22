# Secao: 7.7 Funções de ordem superior e decoradores básicos

import time

def cronometrar(func):
    """Decorador: função que ENVOLVE outra função para adicionar comportamento.
    
    Um decorador recebe uma função e retorna uma NOVA função (wrapper)
    que executa código antes e/ou depois da função original.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)   # chama a função original
        fim = time.time()
        print(f"  ⏱ {func.__name__}() levou {(fim-inicio)*1000:.3f} ms")
        return resultado
    return wrapper

# ── Sintaxe @: açúcar sintático para func = cronometrar(func) ──
@cronometrar
def soma_grande(n):
    return sum(range(n))

total = soma_grande(1_000_000)
print(f"  Soma 0..999999 = {total:,}")

# Equivalente sem @:
# soma_grande = cronometrar(soma_grande)
