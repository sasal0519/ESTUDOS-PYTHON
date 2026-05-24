# Secao: 🔄 Versão Alternativa: Conta Vogais com `sum()`

# ═══════════════════════════════════════════════════════════
# DESAFIO 3: VERSÃO COMPACTA (PYTHONICA)
# ═══════════════════════════════════════════════════════════

def conta_vogais_compacto(texto):
    vogais = set("aeiouAEIOU")
    # sum(1 for ...) conta quantos elementos satisfazem a condição
    return sum(1 for char in texto if char in vogais)


# Comparação lado a lado
print("═" * 60)
print("COMPARAÇÃO: Versão Didática vs Versão Compacta")
print("═" * 60)

texto = "Programação"

print(f"\nEntrada: '{texto}'\n")
print(f"Versão Didática (for explícito):  {conta_vogais(texto)}")
print(f"Versão Compacta (sum + gen):    {conta_vogais_compacto(texto)}")
print("\n✅ Ambas produzem o mesmo resultado!")
