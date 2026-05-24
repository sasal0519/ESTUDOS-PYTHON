# Secao: 7.1 Definição básica e `return`

def saudacao(nome):
    """Retorna uma saudação personalizada.
    
    Docstring: documentação da função, acessível via help(saudacao).
    A primeira string de uma função é a docstring — boa prática sempre incluir!
    """
    return f"Olá, {nome}! Bem-vindo ao Python."
    # return encerra a função e devolve o valor para quem chamou

msg = saudacao("Salomão")   # chama a função e armazena o retorno
print(msg)

# Funções sem return retornam None implicitamente
def imprime_separador():
    print("-" * 40)
    # sem return → retorna None

resultado = imprime_separador()
print("Retorno sem return:", resultado)  # None
