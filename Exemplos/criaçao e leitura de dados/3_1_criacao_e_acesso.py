# Secao: 3.1 Criação e acesso

texto = "Python é incrível!"

print("Original  :", texto)
print("Tamanho   :", len(texto))       # len() conta os caracteres
print("1º char   :", texto[0])         # índice 0 = primeiro caractere
print("Último    :", texto[-1])        # índice -1 = último caractere

# FATIAMENTO (slicing): texto[início:fim:passo]
# 'fim' é EXCLUSIVO — texto[0:6] pega índices 0,1,2,3,4,5
print("Fatiamento:", texto[0:6])       # 'Python'
print("Reverso   :", texto[::-1])      # passo -1 = lê de trás pra frente

# Experimente:
# texto[7:]   → do índice 7 até o fim
# texto[:6]   → do início até o índice 5
# texto[::2]  → de 2 em 2 caracteres
