# Secao: 3.2 Principais métodos

s = "  Olá, Mundo!  "

# Cada método RETORNA uma nova string (strings são imutáveis!)
print(repr(s.strip()))            # remove espaços/\n das bordas → 'Olá, Mundo!'
print(s.strip().upper())          # tudo MAIÚSCULO
print(s.strip().lower())          # tudo minúsculo
print(s.strip().title())          # Cada Palavra Começa Com Maiúscula
print(s.strip().replace("Mundo", "Python"))  # substitui substrings

# Verificação de conteúdo
print("\n'Mundo' está em s?", "Mundo" in s)  # True

# split(): divide a string em lista pelos separadores
partes = s.strip().split(", ")    # divide por ", "
print("split:', '  :", partes)    # ['Olá', 'Mundo!']

# Outros métodos úteis:
print("\nstartswith('  Olá'):", s.startswith("  Olá"))  # True
print("endswith('!  ')    :", s.endswith("!  "))          # True
print("count('o')         :", s.lower().count("o"))       # conta ocorrências
