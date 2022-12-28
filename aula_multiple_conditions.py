
#seguindo a mesma lógica da tributação do vídeo
pais = input('Qual o seu país de origem?')

tax = 0


if pais.lower() == 'brasil':
    estado = input('Em qual estado você realizou a compra?')
#if estado == 'São Paulo' or estado == 'Rio de Janeiro': OUTRA FORMA DE ESCREVER A MESMA COISA, DE FORMA MAIS ELEGANTE 
    if estado.lower() in('são paulo','rio de janeiro','paraná'):
        tax = 0.20
    elif estado.lower() == 'brasília':
        tax = 0.15
    elif estado.lower() == 'minas gerais':
        tax = 0.10
    else:
        tax = 0.05
else: 
    tax = 0.0
print('Você terá que pagar ' + str(tax)) 
