# Secao: 2.4 Compreensão de Lista (*List Comprehension*)

# ── Forma tradicional com loop explícito
quadrados_trad = []
for n in range(1, 6):
    quadrados_trad.append(n ** 2)  # 3 linhas para criar a lista

# ── List comprehension — equivalente, mas em 1 linha!
quadrados = [n ** 2 for n in range(1, 6)]
# Leitura: "lista de n² para cada n em range(1, 6)"

# ── Com filtro (if): só inclui pares
pares = [n for n in range(20) if n % 2 == 0]
# Leitura: "lista de n para cada n em range(20), SE n for par"

print("Quadrados:", quadrados)   # [1, 4, 9, 16, 25]
print("Pares    :", pares)       # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print("Trad.    :", quadrados_trad)  # igual à list comprehension

# ── Exemplo avançado: transformar strings
nomes = ["ana", "bruno", "carla"]
nomes_maiusc = [nome.upper() for nome in nomes]
print("Maiúsculas:", nomes_maiusc)
