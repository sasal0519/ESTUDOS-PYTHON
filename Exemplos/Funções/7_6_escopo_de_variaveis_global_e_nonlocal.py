# Secao: 7.6 Escopo de variáveis — `global` e `nonlocal`

# Escopo define ONDE uma variável existe e pode ser acessada
# Local: existe apenas dentro da função
# Global: existe fora de qualquer função

contador_global = 0

def incrementar(quantidade=1):
    global contador_global          # declara que usará a variável GLOBAL
    contador_global += quantidade   # sem 'global', criaria variável local!

incrementar()
incrementar(4)
print("Contador global:", contador_global)   # 5

# ── nonlocal: para funções ANINHADAS ──────────────────────────
# nonlocal acessa a variável da função "envolvente" (não a global)
def criar_contador():
    n = 0                    # variável local de criar_contador
    def incrementa():
        nonlocal n           # acessa o 'n' de criar_contador
        n += 1
        return n
    return incrementa        # retorna a função interna (closure!)

c = criar_contador()
print("c():", c(), c(), c())   # cada chamada incrementa o mesmo 'n': 1, 2, 3

# c e o 'n' formam uma CLOSURE: a função "lembra" do ambiente onde foi criada
