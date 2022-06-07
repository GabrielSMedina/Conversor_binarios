from utils.Utils import calcula_casas_necessarias, calcula_resto


def decimal_binario():
    try:
        n_original = int(input('Informe o valor inteiro a ser convertido: '))
    except ValueError:
        return 'Numero invalido!'

    n = n_original
    binario = ''

    casas = calcula_casas_necessarias(n)
    restos = calcula_resto(n)

    for c in range(0, casas + 1):
        binario = binario + '0'

    for c in range(len(restos)):
        if restos[c] == 0:
            lista = list(binario)
            lista[casas] = '0'
            binario = ''.join(lista)
        else:
            lista = list(binario)
            lista[casas] = '1'
            binario = ''.join(lista)
        casas = casas - 1
    if n_original < 0:
        return f'-{binario}'
    else:
        return binario
