from funcoes.Binario_decimal import binario_decimal
from funcoes.Binario_decimal_complemento_a_dois import binario_decimal_complemento_a_dois
from funcoes.Decimal_binario import decimal_binario

funs = {'1': binario_decimal,
        '2': binario_decimal_complemento_a_dois,
        '3': decimal_binario}


while True:
    acao = input('Informe a acao que deseja executar:\n'  
                 '(1)Converter binario para decimal\n'
                 '(2)Converter binario complemento a 2\n'
                 '(3)Converter decimal para binario\n'
                 '(4)Sair\n'
                 'Escolha:')
    if acao in funs:
        funcao = funs[acao]
        resultado = funcao()
        print('', '-'*50, '\n', f'Resultado: {resultado}', '\n', '-'*50)
    elif acao == '4':
        print('Encerrando processo...')
        break
    else:
        print('Acao invalida!')
