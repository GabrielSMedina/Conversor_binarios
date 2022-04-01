from utils.Utils import validacao_binario, calcula_decimal


def binario_decimal():
    binario = input('Informe o binario: ')
    valido = validacao_binario(binario)
    if valido:
        decimal = calcula_decimal(binario)
        return str(decimal)
    else:
        return 'Binario invalido!'
