# Secao: 3.3 Formatação de strings

nome  = "Salomão"
nota  = 9.75
media = 8.5

# ── f-string (RECOMENDADO — Python 3.6+) ──────────────────────
# Coloque f antes das aspas; use {} para inserir variáveis
# {nota:.1f} → 1 casa decimal; {media:.2f} → 2 casas decimais
print(f"Aluno: {nome} | Nota: {nota:.1f} | Média: {media:.2f}")

# ── .format() (Python 2 e 3) ──────────────────────────────────
# {} é substituído pelos argumentos de .format() na ordem
print("Aluno: {} | Nota: {:.1f}".format(nome, nota))

# ── Alinhamento e preenchimento ───────────────────────────────
# {item:<10} → alinha à esquerda em 10 chars
# {valor:>6.2f} → alinha à direita em 6 chars, 2 decimais
print("\n📋 Lista de preços:")
for item, valor in [("Arroz", 5.90), ("Feijão", 8.50), ("Macarrão", 3.20)]:
    print(f"  {item:<10} R$ {valor:>6.2f}")
