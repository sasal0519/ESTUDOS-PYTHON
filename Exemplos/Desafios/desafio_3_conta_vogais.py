# Secao: Desafio 3: Conta Vogais

# ═══════════════════════════════════════════════════════════
# DESAFIO 3: CONTA VOGAIS
# ═══════════════════════════════════════════════════════════

def conta_vogais(texto):
    # Passo 1: Define um conjunto (set) com todas as vogais
    # minúsculas e maiúsculas. Usamos set porque a busca é mais rápida!
    vogais = set("aeiouAEIOU")
    
    # Passo 2: Inicializa o contador em zero
    contador = 0
    
    # Passo 3: Itera por cada caractere da string
    for char in texto:
        
        # Passo 4: Verifica se o caractere está no conjunto de vogais
        if char in vogais:
            # Se for vogal, incrementa o contador
            contador += 1
    
    # Passo 5: Retorna o total de vogais encontradas
    return contador


# ─────────────────────────────────────────────────────────
# TESTES COM OS EXEMPLOS DO DESAFIO
# ─────────────────────────────────────────────────────────

print("═" * 60)
print("TESTES OFICIAIS DO DESAFIO")
print("═" * 60)

testes = ["Python", "Programação", "Função"]

for texto in testes:
    resultado = conta_vogais(texto)
    print(f"O número de vogais na string '{texto}' é: {resultado}")


# ─────────────────────────────────────────────────────────
# TESTES EXTRAS
# ─────────────────────────────────────────────────────────

print("\n" + "═" * 60)
print("TESTES EXTRAS")
print("═" * 60)

# String vazia
texto = ""
resultado = conta_vogais(texto)
print(f"\nString vazia: '{texto}' → {resultado} vogais")

# Só vogais maiúsculas
texto = "AEIOU"
resultado = conta_vogais(texto)
print(f"Só vogais maiúsculas: '{texto}' → {resultado} vogais")

# Só consoantes
texto = "bcdfg"
resultado = conta_vogais(texto)
print(f"Só consoantes: '{texto}' → {resultado} vogais")

# Vogais acentuadas (NÃO contam neste desafio!)
texto = "áéíóú"
resultado = conta_vogais(texto)
print(f"Vogais acentuadas: '{texto}' → {resultado} vogais (não contam!)")

# Mistura de tudo
texto = "Hello World 123!"
resultado = conta_vogais(texto)
print(f"Mistura: '{texto}' → {resultado} vogais")

# Texto longo
texto = "Python é uma linguagem de programação poderosa"
resultado = conta_vogais(texto)
print(f"Texto longo: '{texto}' → {resultado} vogais")
