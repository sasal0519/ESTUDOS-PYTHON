# Secao: 7.5 Funções Lambda

# Lambda: função ANÔNIMA de UMA expressão (sem def, sem nome, sem return explícito)
# Sintaxe: lambda parâmetros: expressão
# Quando usar: quando a função é simples e usada em um único lugar

dobrar   = lambda x: x * 2
potencia = lambda base, exp: base ** exp

print("dobrar(7)       :", dobrar(7))
print("potencia(3, 4)  :", potencia(3, 4))

# ── Uso clássico: como argumento de funções de ordem superior ──

nomes = ["Carlos", "Ana", "Beatriz", "Daniel"]

# sorted com key personalizada: ordena pelo comprimento do nome
print("\nPor tamanho     :", sorted(nomes, key=lambda n: len(n)))

# map(): aplica uma função a CADA elemento
quadrados = list(map(lambda n: n**2, range(1, 6)))
print("map quadrados   :", quadrados)

# filter(): mantém apenas os elementos onde a função retorna True
impares = list(filter(lambda n: n % 2 != 0, range(10)))
print("filter ímpares  :", impares)
