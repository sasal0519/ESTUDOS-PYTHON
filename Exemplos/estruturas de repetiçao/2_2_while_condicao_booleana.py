# Secao: 2.2 `while` — condição booleana

contador = 0
while contador < 5:
    print(f"  contador = {contador}")
    contador += 1    # IMPORTANTE: sem essa linha, o loop seria infinito!
                     # pois contador nunca chegaria a 5

print("Loop encerrado!")

# O while equivale a:
# "enquanto contador for menor que 5, execute o bloco"
