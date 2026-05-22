# Secao: 1.6 Operadores Bit a Bit

x, y = 0b1010, 0b1100   # x=10, y=12 em decimal

print(f"x      = {x:04b}  ({x})")
print(f"y      = {y:04b}  ({y})")
print(f"x & y  = {x & y:04b}  ({x & y})  AND  → 1 apenas onde ambos têm 1")
print(f"x | y  = {x | y:04b}  ({x | y})  OR   → 1 onde ao menos um tem 1")
print(f"x ^ y  = {x ^ y:04b}  ({x ^ y})  XOR  → 1 onde são diferentes")
print(f"~x     = {~x}          NOT  → inverte todos os bits (resultado negativo!)")
print(f"x << 1 = {x << 1:05b}  ({x << 1})  shift esquerda = x * 2")
print(f"x >> 1 = {x >> 1:03b}   ({x >> 1})   shift direita  = x // 2")
