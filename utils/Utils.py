def soma_um(binario):
    posicao = len(binario) - 1
    while True:
        if binario[posicao] == '0':
            lista = list(binario)
            lista[posicao] = '1'
            binario = ''.join(lista)
            break
        else:
            lista = list(binario)
            lista[posicao] = '0'
            binario = ''.join(lista)
            posicao = posicao - 1
    return binario


def calcula_decimal(binario):
    decimal = 0
    cont = len(binario) - 1
    potencia = 0
    while cont >= 0:
        if binario[cont] == '1':
            decimal = decimal + 2 ** potencia
        cont = cont - 1
        potencia = potencia + 1
    return decimal


def inverte_binario(binario):
    binario_alterado = ''
    for c in range(len(binario)):
        if binario[c] == '1':
            binario_alterado = binario_alterado + '0'
        else:
            binario_alterado = binario_alterado + '1'
    binario_alterado_mais_um = soma_um(binario_alterado)

    return binario_alterado_mais_um


def validacao_binario(binario):
    pode = True
    for c in range(len(binario)):
        if binario[c] != '0' and binario[c] != '1':
            pode = False
    return pode


def calcula_casas_necessarias(numero):
    potencia = 0
    while True:
        if numero + 1 <= 2 ** potencia:
            return potencia - 1
        potencia = potencia + 1


def calcula_resto(numero):
    restos = []
    while numero >= 1:
        resto = numero % 2
        numero = numero // 2
        restos.append(resto)
    return restos
