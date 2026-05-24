# Secao: 🔄 Versão Alternativa com `dict.get()`

# ═══════════════════════════════════════════════════════════
# DESAFIO 5: VERSÃO ALTERNATIVA COM dict.get()
# ═══════════════════════════════════════════════════════════

def contar_caracteres_alt(string):
    contador = {}
    
    for caractere in string:
        # dict.get(chave, padrao) retorna o valor da chave ou o padrão se não existir
        # Assim, eliminamos a necessidade do if/else!
        contador[caractere] = contador.get(caractere, 0) + 1
    
    return contador


# Comparação lado a lado
print("═" * 60)
print("COMPARAÇÃO: Versão Principal vs Versão Alternativa")
print("═" * 60)

palavra = "collections"

print(f"\nEntrada: '{palavra}'\n")
print(f"Versão Principal (if/else):  {contar_caracteres(palavra)}")
print(f"Versão Alternativa (get):    {contar_caracteres_alt(palavra)}")
print("\n✅ Ambas produzem o mesmo resultado!")
