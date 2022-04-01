from utils.Utils import validacao_binario, calcula_decimal, inverte_binario


def binario_decimal_complemento_a_dois():
    binario = input('Informe o binario: ')
    valido = validacao_binario(binario)
    if valido:
        if binario[0] == '0':
            decimal = calcula_decimal(binario)
        else:
            binario_invertido = inverte_binario(binario)
            decimal = calcula_decimal(binario_invertido)
            decimal = decimal * (-1)
        return str(decimal)
    else:
        return 'Binario invalido!'
