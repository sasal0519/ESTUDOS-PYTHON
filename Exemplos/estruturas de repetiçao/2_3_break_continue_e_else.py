# Secao: 2.3 `break`, `continue` e `else`

frutas = ["maçã", "banana", "laranja", "uva"]

# ── break: para tudo ao encontrar 'banana'
print("break ao encontrar 'banana':")
for fruta in frutas:
    if fruta == "banana":
        print("  -> Encontrei! Parando.")
        break           # sai do loop imediatamente
    print(f"  {fruta}")

print()

# ── continue: pula 'banana', mas continua o loop
print("continue — pula 'banana':")
for fruta in frutas:
    if fruta == "banana":
        continue        # vai direto para a próxima iteração
    print(f"  {fruta}")

print()

# ── else: executa somente se o loop não foi interrompido por break
print("else no for:")
for i in range(3):
    print(f"  i={i}")
else:
    print("  Loop concluído sem break!")  # executa aqui pois não houve break
