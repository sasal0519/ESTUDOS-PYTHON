# Secao: 5. Tuplas

# ── Criação ──────────────────────────────────────────────────
coordenadas = (10.5, -37.2)      # latitude, longitude
rgb_vermelho = (255, 0, 0)       # valores RGB
singleton    = (42,)             # ⚠️ vírgula OBRIGATÓRIA para 1 elemento
                                 # sem vírgula: (42) é só o número 42!

print("Coordenadas :", coordenadas)
print("RGB vermelho:", rgb_vermelho)
print("Singleton   :", singleton, "→ tipo:", type(singleton))
print("Sem vírgula :", (42),     "→ tipo:", type((42)))  # é int, não tupla!


# ── Acesso e fatiamento (idêntico às listas) ─────────────────
ponto = (3, 7, 15, 22, 8)

print("ponto[0]   :", ponto[0])    # primeiro elemento
print("ponto[-1]  :", ponto[-1])   # último elemento
print("ponto[1:4] :", ponto[1:4])  # fatiamento: índices 1, 2, 3

# Tentativa de modificar → ERRO!
# ponto[0] = 99   # TypeError: 'tuple' object does not support item assignment


# ── Desempacotamento (unpacking) ─────────────────────────────
# Extrai os valores da tupla em variáveis individuais — muito elegante!

coordenadas = (10.5, -37.2)
x, y = coordenadas           # número de variáveis deve bater com a tupla
print(f"Latitude: {x} | Longitude: {y}")

# ── Desempacotamento com * (captura o "resto") ────────────────
ponto = (3, 7, 15, 22, 8)
primeiro, *meio, ultimo = ponto
# primeiro = 3 (primeiro elemento)
# meio     = [7, 15, 22] (tudo do meio, como lista)
# ultimo   = 8 (último elemento)
print(f"Primeiro: {primeiro} | Meio: {meio} | Último: {ultimo}")


# ── Métodos disponíveis nas tuplas ───────────────────────────
# Tuplas têm apenas 2 métodos (ao contrário das listas que têm ~12)
notas = (7, 9, 8, 9, 6, 9, 7)

print("count(9) :", notas.count(9))   # conta quantas vezes 9 aparece → 3
print("index(8) :", notas.index(8))   # índice da PRIMEIRA ocorrência de 8 → 2

# ── Conversão entre tipos ─────────────────────────────────────
lista_conv = list(notas)            # tupla → lista (agora mutável)
tupla_conv = tuple([1, 2, 3])      # lista → tupla (agora imutável)

print("\nlist() :", lista_conv)
print("tuple():", tupla_conv)


# ── Tupla como chave de dicionário ───────────────────────────
# Listas NÃO podem ser chaves de dicionários (não são hashable)
# Tuplas SIM — pois são imutáveis e, portanto, hashable

locais = {
    (-5.79, -35.21): "Natal, RN",        # tupla (lat, lon) como chave
    (-23.55, -46.63): "São Paulo, SP",
}

print("Locais cadastrados:")
for coord, cidade in locais.items():
    print(f"  {coord} → {cidade}")

# Acessando diretamente pela chave-tupla:
print("\nNatal está em:", locais[(-5.79, -35.21)])
