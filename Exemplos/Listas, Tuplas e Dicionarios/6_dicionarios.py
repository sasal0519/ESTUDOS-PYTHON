# Secao: 6. Dicionários

# ── Criação ──────────────────────────────────────────────────
aluno = {
    "nome"    : "Salomão",
    "curso"   : "ADS",
    "periodo" : 1,
    "notas"   : [8.5, 9.0, 7.5],    # valor pode ser uma lista!
}

print("Dicionário:", aluno)
print("Nome      :", aluno["nome"])   # acesso direto pela chave
print("Notas     :", aluno["notas"])

# ⚠️ Acessar chave inexistente com [] lança KeyError!
# print(aluno["email"])  → KeyError: 'email'


# ── Acesso seguro com .get() ─────────────────────────────────
# .get(chave, padrão) retorna o padrão se a chave não existir (sem erro)
print(aluno.get("email", "não cadastrado"))   # → "não cadastrado"
print(aluno.get("nome", "desconhecido"))      # → "Salomão"

# ── Adição e atualização ──────────────────────────────────────
aluno["email"] = "salomao@email.com"  # adiciona nova chave
aluno["periodo"] = 2                   # atualiza valor existente

print("\nApós update:", aluno)


# ── Remoção ──────────────────────────────────────────────────
email_removido = aluno.pop("email")   # remove E retorna o valor
print("E-mail removido:", email_removido)
print("Chaves restantes:", list(aluno.keys()))

# Outros métodos de remoção:
# del aluno["chave"]    → remove sem retornar
# aluno.clear()         → remove TODOS os pares
# aluno.pop("x", None)  → remove se existir, retorna None se não existir


# ── Iteração sobre dicionários ────────────────────────────────
print("--- Chaves (keys) ---")
for chave in aluno.keys():
    print(" ", chave)

print("\n--- Valores (values) ---")
for valor in aluno.values():
    print(" ", valor)

print("\n--- Pares chave/valor (items) ---")
for chave, valor in aluno.items():
    # .items() retorna tuplas (chave, valor) — desempacotamos na declaração
    print(f"  {chave:10} : {valor}")


# ── Dicionário aninhado ───────────────────────────────────────
# Dicionários dentro de dicionários — muito comum em APIs JSON!
empresa = {
    "nome": "TechBR",
    "filiais": {
        "norte" : {"cidade": "Natal",     "funcionarios": 30},
        "sudeste": {"cidade": "São Paulo", "funcionarios": 120},
    }
}

# Acesso encadeado: empresa["filiais"]["norte"]["cidade"]
print("Filial norte :", empresa["filiais"]["norte"]["cidade"])
print("Funcionários :", empresa["filiais"]["norte"]["funcionarios"])
print("Total filiais:", len(empresa["filiais"]))


# ── Dict Comprehension ───────────────────────────────────────
# Assim como List Comprehension, mas cria dicionários!
# Sintaxe: {chave: valor for variavel in sequencia if condicao}

quadrados = {n: n**2 for n in range(1, 8)}
print("Quadrados:", quadrados)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

# ── Filtro: só pares cujo VALOR é par ────────────────────────
pares = {k: v for k, v in quadrados.items() if v % 2 == 0}
print("Apenas valores pares:", pares)

# ── Inverter chave e valor ────────────────────────────────────
invertido = {v: k for k, v in quadrados.items()}
print("Invertido (valor→chave):", invertido)
