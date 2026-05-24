# Secao: 3.4 Operações úteis

palavras = ["Python", "é", "fantástico"]

# ── join(): une itens de uma lista em uma string ──────────────
# " ".join(lista) → usa espaço como separador
frase = " ".join(palavras)
print("join    :", frase)           # "Python é fantástico"

# Outros separadores:
print(", ".join(palavras))          # "Python, é, fantástico"
print("-".join(["a", "b", "c"]))   # "a-b-c"

# ── find(): retorna o ÍNDICE da primeira ocorrência (-1 se não achar)
print("\nfind 'é'    :", frase.find("é"))   # posição do 'é'
print("find 'Java'  :", frase.find("Java")) # -1 → não encontrado

# ── startswith / endswith ────────────────────────────────────
print("startswith 'Py' :", frase.startswith("Py"))   # True
print("endswith 'co'   :", frase.endswith("co"))      # True

# ── count(): quantas vezes aparece ──────────────────────────
print("count 'a'       :", frase.count("a"))  # conta todas as letras 'a'

# ── zfill(): preenche com zeros à esquerda ───────────────────
# Muito usado para IDs, códigos, protocolos
codigo = "42"
print("\nzfill(5)        :", codigo.zfill(5))   # "00042"
