def contar_caracteres(string):
    contador = {}

    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

    return contador


if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DO DESAFIO")
    print("=" * 50)

    testes = ["collections", "numpy", "datetime"]

    for palavra in testes:
        resultado = contar_caracteres(palavra)
        print(f"\nEntrada:  '{palavra}'")
        print(f"Saida:    {resultado}")

    print("\n" + "=" * 50)
    print("TESTE EXTRA: String vazia")
    print("=" * 50)
    print("Entrada:  ''")
    print(f"Saida:    {contar_caracteres('')}")

    print("\n" + "=" * 50)
    print("TESTE EXTRA: 'aaaabbbcc'")
    print("=" * 50)
    print("Entrada:  'aaaabbbcc'")
    print(f"Saida:    {contar_caracteres('aaaabbbcc')}")
