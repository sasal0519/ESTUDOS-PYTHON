# Secao: 7.2 Parâmetros padrão e nomeados

def criar_perfil(nome, idade, cidade="Natal", ativo=True):
    """
    nome, idade  → parâmetros OBRIGATÓRIOS (sem valor padrão)
    cidade, ativo → parâmetros OPCIONAIS (têm valor padrão)
    
    ⚠️ Parâmetros com padrão devem vir DEPOIS dos obrigatórios!
    """
    status = "✅ ativo" if ativo else "❌ inativo"
    return f"{nome}, {idade} anos, {cidade} — {status}"

# Chamadas diferentes:
print(criar_perfil("Ana", 25))                          # usa padrões
print(criar_perfil("Carlos", 30, cidade="Fortaleza"))   # sobrescreve cidade
print(criar_perfil("Bia", 22, ativo=False))             # usa padrão de cidade
print(criar_perfil("Diego", 28, "Recife", False))       # posicionais

# Parâmetros nomeados (keyword arguments) tornam o código mais legível
# e permitem passar em qualquer ordem
print(criar_perfil(idade=35, nome="Eva", ativo=True, cidade="Manaus"))
