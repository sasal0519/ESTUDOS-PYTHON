# Secao: Desafio 2: Ano Bissexto

# ═══════════════════════════════════════════════════════════
# DESAFIO 2: ANO BISSEXTO
# ═══════════════════════════════════════════════════════════

def verificador_ano_bissexto(ano):
    # Verifica as duas regras do ano bissexto:
    # Regra 1: divisível por 4 E NÃO divisível por 100
    # Regra 2: OU divisível por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")


# ─────────────────────────────────────────────────────────
# TESTES COM OS EXEMPLOS DO DESAFIO
# ─────────────────────────────────────────────────────────

print("═" * 50)
print("TESTES OFICIAIS DO DESAFIO")
print("═" * 50)

print("\nAno 1975:")
verificador_ano_bissexto(1975)   # Esperado: NÃO

print("\nAno 1986:")
verificador_ano_bissexto(1986)   # Esperado: NÃO

print("\nAno 1992:")
verificador_ano_bissexto(1992)   # Esperado: SIM


# ─────────────────────────────────────────────────────────
# TESTES EXTRAS (casos extremos importantes)
# ─────────────────────────────────────────────────────────

print("\n" + "═" * 50)
print("TESTES EXTRAS (CASOS EXTREMOS)")
print("═" * 50)

# 1900: divisível por 4 e 100, MAS NÃO por 400 → NÃO é bissexto
print("\nAno 1900 (divisível por 4 e 100, mas não por 400):")
verificador_ano_bissexto(1900)

# 2000: divisível por 4, 100 E 400 → É bissexto (exceção da exceção)
print("\nAno 2000 (divisível por 4, 100 E 400):")
verificador_ano_bissexto(2000)

# 2024: divisível por 4, não por 100 → É bissexto
print("\nAno 2024 (divisível por 4, não por 100):")
verificador_ano_bissexto(2024)

# 2023: não divisível por 4 → NÃO é bissexto
print("\nAno 2023 (não divisível por 4):")
verificador_ano_bissexto(2023)

# 1600: divisível por 400 → É bissexto
print("\nAno 1600 (divisível por 400):")
verificador_ano_bissexto(1600)

# 1: não divisível por nada → NÃO é bissexto
print("\nAno 1 (ano mínimo):")
verificador_ano_bissexto(1)
