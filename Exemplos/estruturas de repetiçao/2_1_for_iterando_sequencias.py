# Secao: 2.1 `for` — iterando sequências

# Exemplo básico: percorre cada fruta da lista
frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    # A cada volta do loop, 'fruta' recebe o próximo valor da lista
    print(f"  🍎 {fruta}")


# range(início, fim, passo) — gera uma sequência de números
# range(0, 11, 2) → começa em 0, vai até 10 (11 é exclusivo!), de 2 em 2
print("Pares de 0 a 10:")
for i in range(0, 11, 2):
    print(i, end=" ")   # end=" " imprime na mesma linha com espaço
print()                 # quebra de linha no final

# Outros usos do range:
# range(5)      → 0, 1, 2, 3, 4
# range(1, 6)   → 1, 2, 3, 4, 5
# range(10, 0, -1) → 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


# enumerate() retorna índice E valor ao mesmo tempo
# sem enumerate: só temos o valor, sem saber a posição
# com enumerate: temos (índice, valor) como par

print("Índice e valor:")
for idx, fruta in enumerate(frutas, start=1):
    # start=1 faz o contador começar em 1 (padrão é 0)
    print(f"  [{idx}] {fruta}")
