# Secao: 1.3 Operadores Lógicos

p, q = True, False

print("p and q →", p and q)  # False: precisa de AMBOS True
print("p or  q →", p or  q)  # True:  basta UM ser True
print("not p   →", not p)    # False: inverte True → False
print("not q   →", not q)    # True:  inverte False → True

# Exemplo prático: acesso permitido se maior de idade E tem cadastro
idade = 20
tem_cadastro = True
print("\nAcesso permitido?", idade >= 18 and tem_cadastro)
