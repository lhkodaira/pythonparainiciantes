#handling conditions = lógica condicionais 
#
#price = input('Quanto custou?: ')
#price = float(price) #convertendo para float para que possa fazer a comparação abaixo
#if price >= 1.00:
#    tax = .07
#else: 
#    tax = 0
#print('A taxa que deve ser paga é de ' + str(tax))

##Tomar cuidado ao realizar comparações entre strings, mas são case sensitive. 
##para resolver a gente formata a entrada recebida
print()
country = input('Qual o seu país de origem: ')
if country.lower() == 'canada':
    print('olha, uma canadense : D')
else:
    print('que pena.')