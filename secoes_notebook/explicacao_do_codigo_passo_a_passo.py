# Secao: 📖 Explicação do Código – Passo a Passo

# ═══════════════════════════════════════════════════════════
# DESAFIO 3: ELEMENTOS COMUNS
# ═══════════════════════════════════════════════════════════

def elementos_comuns(lista1, lista2):
    # Converte cada string da lista para inteiro usando map,
    # depois transforma em set para eliminar duplicatas
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    
    # Encontra a interseção (elementos presentes em ambos)
    # e converte de volta para lista
    return list(set1.intersection(set2))


# ─────────────────────────────────────────────────────────
# TESTE 1: Entrada válida (exemplo do desafio)
# ─────────────────────────────────────────────────────────
lista1 = ['1', '2', '3', '4']
lista2 = ['3', '4', '5', '6']

# Validação: todos os elementos são dígitos?
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")


# ─────────────────────────────────────────────────────────
# TESTE 2: Outro exemplo válido
# ─────────────────────────────────────────────────────────
lista1 = ['9', '8', '7', '6', '5']
lista2 = ['5', '2', '3', '7']

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")


# ─────────────────────────────────────────────────────────
# TESTE 3: Entrada inválida (contém letras)
# ─────────────────────────────────────────────────────────
lista1 = ['a', 'b', 'c', 'd']
lista2 = ['a', 'e', 'i', 'o', 'u']

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")


# ─────────────────────────────────────────────────────────
# TESTE 4: Com duplicatas na mesma lista
# ─────────────────────────────────────────────────────────
lista1 = ['1', '2', '2', '3', '3', '3']
lista2 = ['3', '4', '4', '4']

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")


# ═══════════════════════════════════════════════════════════
# DESAFIO 5: CONTAR CARACTERES (Versão Principal)
# ═══════════════════════════════════════════════════════════

def contar_caracteres(string):
    # Inicializa um dicionário VAZIO para armazenar as contagens
    contador = {}
    
    # Itera através de CADA CARACTERE na string, um por um
    for caractere in string:
        
        # Verifica se o caractere JÁ ESTÁ no dicionário
        if caractere in contador:
            # Se SIM: incrementa o valor atual em 1
            contador[caractere] += 1
        else:
            # Se NÃO: cria a chave com valor inicial 1
            contador[caractere] = 1
    
    # Retorna o dicionário completo com todas as contagens
    return contador


# ─────────────────────────────────────────────────────────
# TESTES COM OS EXEMPLOS DO DESAFIO
# ─────────────────────────────────────────────────────────

print("═" * 50)
print("TESTES DO DESAFIO")
print("═" * 50)

testes = ["collections", "numpy", "datetime"]

for palavra in testes:
    resultado = contar_caracteres(palavra)
    print(f"\nEntrada:  '{palavra}'")
    print(f"Saída:    {resultado}")


# ─────────────────────────────────────────────────────────
# TESTE EXTRA: string vazia
# ─────────────────────────────────────────────────────────
print("\n" + "═" * 50)
print("TESTE EXTRA: String vazia")
print("═" * 50)
print(f"Entrada:  ''")
print(f"Saída:    {contar_caracteres('')}")


# ─────────────────────────────────────────────────────────
# TESTE EXTRA: caracteres repetidos
# ─────────────────────────────────────────────────────────
print("\n" + "═" * 50)
print("TESTE EXTRA: 'aaaabbbcc'")
print("═" * 50)
print(f"Entrada:  'aaaabbbcc'")
print(f"Saída:    {contar_caracteres('aaaabbbcc')}")
