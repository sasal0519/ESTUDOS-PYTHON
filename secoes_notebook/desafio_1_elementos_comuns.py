def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))


if __name__ == "__main__":
    lista1 = ['1', '2', '3', '4']
    lista2 = ['3', '4', '5', '6']

    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
        comuns = elementos_comuns(lista1, lista2)
        print(f"Elementos comuns as duas listas: {comuns}")
    else:
        print("Entrada invalida.")

    lista1 = ['9', '8', '7', '6', '5']
    lista2 = ['5', '2', '3', '7']

    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
        comuns = elementos_comuns(lista1, lista2)
        print(f"Elementos comuns as duas listas: {comuns}")
    else:
        print("Entrada invalida.")

    lista1 = ['a', 'b', 'c', 'd']
    lista2 = ['a', 'e', 'i', 'o', 'u']

    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
        comuns = elementos_comuns(lista1, lista2)
        print(f"Elementos comuns as duas listas: {comuns}")
    else:
        print("Entrada invalida.")

    lista1 = ['1', '2', '2', '3', '3', '3']
    lista2 = ['3', '4', '4', '4']

    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
        comuns = elementos_comuns(lista1, lista2)
        print(f"Elementos comuns as duas listas: {comuns}")
    else:
        print("Entrada invalida.")
