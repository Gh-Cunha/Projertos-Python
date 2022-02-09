def contar_caracteres(s):
    """Função  que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('gabriel')
    {'g': 1, 'a': 1, 'b': 1, 'r': 1, 'i': 1, 'e': 1, 'l': 1}
    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s: string a ser contada

    """

    resultado={}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('Gabriel'))
    print()
    print(contar_caracteres('banana'))