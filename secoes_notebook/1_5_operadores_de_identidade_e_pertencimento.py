# Secao: 1.5 Operadores de Identidade e Pertencimento

lista = [1, 2, 3, 4, 5]
a = [1, 2, 3]
b = a          # b é um APELIDO para o mesmo objeto que a
c = [1, 2, 3]  # c tem o mesmo conteúdo, mas é um objeto DIFERENTE

# Identidade — mesma posição de memória?
print("b is a     →", b is a)      # True  — b e a são o MESMO objeto
print("c is a     →", c is a)      # False — c é um objeto diferente
print("c == a     →", c == a)      # True  — conteúdo igual!
print("c is not a →", c is not a)  # True  — são objetos distintos

# Pertencimento — elemento está na sequência?
print()
print("3 in lista     →", 3 in lista)       # True
print("9 in lista     →", 9 in lista)       # False
print("9 not in lista →", 9 not in lista)   # True
print("'Py' in 'Python' →", "Py" in "Python")  # True — funciona em strings!
