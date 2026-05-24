# Secao: 7.4 Retornando múltiplos valores

def estatisticas(numeros):
    """Retorna (mínimo, máximo, média) de uma lista.
    
    Python permite retornar múltiplos valores separados por vírgula.
    Internamente, são empacotados em uma TUPLA.
    """
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

dados = [4, 7, 2, 9, 1, 6, 8, 3]

# Desempacotamento automático:
minimo, maximo, media = estatisticas(dados)
print(f"Mín: {minimo} | Máx: {maximo} | Média: {media:.2f}")

# Ou capturando como tupla:
resultado = estatisticas(dados)
print("Tipo do retorno:", type(resultado))  # tuple
print("Resultado      :", resultado)
