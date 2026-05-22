# Secao: 7.3 `*args` e `**kwargs`

# ── *args: número VARIÁVEL de argumentos posicionais ──────────
# O * "empacota" todos os argumentos extras em uma TUPLA
def somar(*numeros):
    """Aceita qualquer quantidade de números."""
    total = sum(numeros)
    print(f"Somando {numeros} = {total}")
    return total

somar(1, 2)              # numeros = (1, 2)
somar(3, 5, 7, 9)        # numeros = (3, 5, 7, 9)
somar(*[10, 20, 30])     # desempacota lista → equivale a somar(10, 20, 30)

print()

# ── **kwargs: número VARIÁVEL de argumentos nomeados ──────────
# O ** "empacota" todos os argumentos nomeados extras em um DICIONÁRIO
def ficha(**dados):
    """Aceita qualquer conjunto de campos nomeados."""
    print("=== Ficha ===")
    for campo, valor in dados.items():
        print(f"  {campo:<12}: {valor}")

ficha(nome="Lucas", matricula="2024001", curso="ADS", turno="Noite")
# dados = {"nome": "Lucas", "matricula": "2024001", "curso": "ADS", "turno": "Noite"}
