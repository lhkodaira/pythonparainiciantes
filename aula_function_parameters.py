#Podemos usar como parametros a lógica booleana (True ou False)

from pickle import TRUE


def get_initial(name, force_uppercase=True):#definindo o valor do force_uppercase, haverá um padrão,mas ainda poderemos declarar como False
#conforme a nossa necessidade, podemos pedir para que esta função force a mudança do caractere, para maiúsculo
#o force_uppercase será definido como false ou true para que aconteça, ex: 
    if force_uppercase: #caso o force_uppercase seja true, ele fará a seguinte ação
        initial = name[0:1].upper()#irá pegar a letra inicial e torná-la maiúscula 
    else: 
        initial = name[0:1]#caso false, irá apenas pegar a letra inicial
    return initial 

first_name = input('Escreva seu primeiro nome: ')
first_name_initial = get_initial(first_name)#Detalhe: como o padrão do force foi definido como true, não precisamos declara-lo quando for true. 
#o primeiro parametro é a variável que iremos utilizar e o segundo parametro é declarado caso seja de nosso interesse que seja maiusculo

middle_name = input('Escreva seu nome do meio: ')
middle_name_initial = get_initial(middle_name, False)#mesmo o force tendo um padrão, ainda podemos declara-lo como false caso necessitemos 

last_name = input('Escreva seu sobrenome: ')
last_name_initial = get_initial(force_uppercase=False, name=last_name)#mesmo o force tendo um default, ainda podemos declará-lo como true sem que heja algum problema 
#na declaração dos parametros do last_name_initial, não seguimos a ordem dada, mas declaramos o que cada parametro é, então não há 
# necessidade de seguir a ordem, está uma boa forma de escrever para que o código se torne mais fácil de ser entendido. 



print('Suas iniciais são : ', first_name_initial, middle_name_initial, last_name_initial)