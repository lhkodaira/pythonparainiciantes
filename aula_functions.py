#as vezes copiamos e colocamos nossos códigos, para que não fique muito longo e repepetivo, podemos usar as funções. 
#exemplo da aula 29

from datetime import datetime #desta forma não precisa declarar duas vezes o datetime.datetime.now
#printando timestamps para ver quanto tempo dura para que as secções do código sejam rodadas 

#first_name = 'Hiromi'
#print('task completed')
#print(datetime.datetime.now())
#print()

#for x in range(0,10):
    #print(x)
#print('task completed')
#print(datetime.datetime.now())
#print()

#vamos criar uma função para printar o tempo : 

def print_time():
    print('task completed')
    print(datetime.now())#declarando o segundo datetime no topo, no código fica mais limpo
    print()

first_name = 'Laiz'
print_time()

for x in range(0,3):
    print(x)
print_time()

#caso a gente queira usar a msm função mas com algumas modificações em um dos itens: 

def print_time(task_name, msg):#adicionamos o(s) parametro(s) dentro dos parenteses da função 
    print(task_name)#e o colocamos novamente no item que queremos modificar ao nosso gosto 
    print(datetime.now())
    print(msg)

first_name = 'Laiz'
print_time('first name assigned', 'teste')

for x in range(0,3):
    print(x)
print_time('loop completed', 'teste')

