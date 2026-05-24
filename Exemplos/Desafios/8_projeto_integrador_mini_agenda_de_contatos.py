# Secao: 8. Projeto Integrador — Mini Agenda de Contatos

# ── Mini Agenda usando: dicionários, listas, funções, strings, loops ──

agenda = {}   # dicionário global: chave=nome normalizado, valor=dict de detalhes

def adicionar_contato(nome, telefone, cidade="Não informada"):
    """Adiciona ou atualiza contato na agenda.
    
    .strip() remove espaços acidentais nas bordas.
    .title() normaliza o nome: 'BRUNO silva' → 'Bruno Silva'
    """
    chave = nome.strip().title()     # normaliza para busca consistente
    agenda[chave] = {"telefone": telefone, "cidade": cidade}
    print(f"  ✅ Contato '{chave}' salvo.")

def buscar_contato(nome):
    """Busca contato pelo nome (case-insensitive graças ao .title())."""
    chave = nome.strip().title()
    info  = agenda.get(chave)        # .get() evita KeyError se não existir
    if info:
        print(f"  📞 {chave}: {info['telefone']} | {info['cidade']}")
    else:
        print(f"  ❌ '{nome}' não encontrado.")

def listar_contatos():
    """Lista todos os contatos em ordem alfabética com alinhamento."""
    if not agenda:       # lista vazia é falsy em Python
        print("  Agenda vazia.")
        return
    print(f"  {'Nome':<20} {'Telefone':<15} {'Cidade'}")
    print("  " + "-" * 50)
    for nome in sorted(agenda):    # sorted() itera em ordem alfabética
        info = agenda[nome]
        print(f"  {nome:<20} {info['telefone']:<15} {info['cidade']}")

def remover_contato(nome):
    """Remove contato da agenda sem gerar erro se não existir."""
    chave = nome.strip().title()
    if agenda.pop(chave, None):    # pop com default=None evita KeyError
        print(f"  🗑 '{chave}' removido.")
    else:
        print(f"  ❌ '{chave}' não encontrado.")

# ── Testando a agenda ─────────────────────────────────────────
print("=" * 54)
print("          📒 MINI AGENDA DE CONTATOS")
print("=" * 54)

# Adicionando contatos com nomes em diferentes formatos
adicionar_contato("Ana Lima",    "(84) 99111-2222", "Natal")
adicionar_contato("bruno silva", "(11) 98765-4321", "São Paulo")    # minúsculas → normalizado
adicionar_contato("CARLA SOUZA", "(21) 97654-3210", "Rio de Janeiro")  # maiúsculas → normalizado
adicionar_contato("Diego Costa", "(85) 91234-5678", "Fortaleza")

print()
listar_contatos()

print()
buscar_contato("bruno silva")    # busca com minúsculas → funciona!
buscar_contato("Maria")          # não existe

print()
remover_contato("Diego Costa")
listar_contatos()
