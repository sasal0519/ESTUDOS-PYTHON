def contar_caracteres_alt(string):
    contador = {}

    for caractere in string:
        contador[caractere] = contador.get(caractere, 0) + 1

    return contador


def contar_caracteres(string):
    contador = {}

    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

    return contador


if __name__ == "__main__":
    print("=" * 60)
    print("COMPARACAO: Versao Principal vs Versao Alternativa")
    print("=" * 60)

    palavra = "collections"

    print(f"\nEntrada: '{palavra}'\n")
    print(f"Versao Principal (if/else):  {contar_caracteres(palavra)}")
    print(f"Versao Alternativa (get):    {contar_caracteres_alt(palavra)}")
    print("\nAmbas produzem o mesmo resultado!")
