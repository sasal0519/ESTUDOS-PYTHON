# Secao: 4. Listas

# ── Criação e funções básicas ────────────────────────────────
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
misto   = [42, "texto", 3.14, True, None]  # tipos mistos: OK em Python!

print("Lista      :", numeros)
print("Comprimento:", len(numeros))   # quantos elementos
print("Mínimo     :", min(numeros))   # menor valor
print("Máximo     :", max(numeros))   # maior valor
print("Soma       :", sum(numeros))   # soma de todos

# Verificar se um elemento existe
print("\n5 in numeros?", 5 in numeros)
print("7 in numeros?", 7 in numeros)


# ── Adição de elementos ──────────────────────────────────────
cores = ["vermelho", "verde"]

cores.append("azul")              # ADICIONA no FINAL — mais comum
cores.insert(1, "amarelo")        # INSERE na posição 1 (desloca os demais)
cores.extend(["laranja", "roxo"]) # CONCATENA outra lista no final

# Diferença entre append e extend:
# append([1,2]) → adiciona A LISTA como um elemento: [..., [1, 2]]
# extend([1,2]) → adiciona OS ELEMENTOS:             [...,  1,  2]

print("Após adições:", cores)
print("Total de cores:", len(cores))


# ── Remoção de elementos ────────────────────────────────────
# cores atual: ['vermelho', 'amarelo', 'verde', 'azul', 'laranja', 'roxo']

cores.remove("amarelo")     # remove pela VALOR (primeira ocorrência)
removido = cores.pop(0)     # remove pelo ÍNDICE e RETORNA o valor
del cores[-1]               # deleta diretamente pelo índice (sem retornar)

print("Removido (pop) :", removido)
print("Lista resultante:", cores)

# Resumo dos métodos de remoção:
# remove(valor)  → busca pelo valor, erro se não existir
# pop(índice)    → remove pelo índice, retorna o elemento (padrão: último)
# del lista[i]   → remove pelo índice, não retorna nada
# lista.clear()  → remove TODOS os elementos


# ── Ordenação e reversão ─────────────────────────────────────
numeros = [3, 1, 4, 1, 5, 9, 2, 6]  # resetando a lista

numeros.sort()                   # ordena IN-PLACE (modifica a lista original)
print("Ordenado    :", numeros)

numeros.sort(reverse=True)       # ordena em ordem DECRESCENTE
print("Decrescente :", numeros)

copia_ordenada = sorted(numeros) # sorted() retorna NOVA lista, não altera a original
print("sorted()    :", copia_ordenada)
print("Original    :", numeros)  # permanece inalterada

numeros.reverse()                # inverte a ordem in-place
print("Invertido   :", numeros)


# ── Fatiamento (slicing): lista[início:fim:passo] ───────────
# Mesmo conceito das strings! 'fim' é exclusivo.
lst = list(range(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original  :", lst)
print("lst[2:7]  :", lst[2:7])   # índices 2,3,4,5,6 → [2, 3, 4, 5, 6]
print("lst[::2]  :", lst[::2])   # de 2 em 2 → [0, 2, 4, 6, 8]
print("lst[::-1] :", lst[::-1])  # passo -1 = reverso → [9, 8, ..., 0]
print("lst[-3:]  :", lst[-3:])   # últimos 3 → [7, 8, 9]
print("lst[:4]   :", lst[:4])    # primeiros 4 → [0, 1, 2, 3]

# IMPORTANTE: slicing cria uma CÓPIA, não modifica o original


# ── Listas aninhadas (matriz 2D) ──────────────────────────────
# Uma lista pode conter outras listas — formando uma "grade" ou "tabela"
matriz = [
    [1, 2, 3],   # linha 0
    [4, 5, 6],   # linha 1
    [7, 8, 9]    # linha 2
]

print("Matriz 3x3:")
for linha in matriz:
    print(" ", linha)

# Acesso: matriz[linha][coluna]
print("\nmatriz[0][0] =", matriz[0][0])  # 1  (linha 0, coluna 0)
print("matriz[1][2] =", matriz[1][2])    # 6  (linha 1, coluna 2)
print("matriz[2][1] =", matriz[2][1])    # 8  (linha 2, coluna 1)
