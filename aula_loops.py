#exemplos da aula 27
#exemplo 1 - looping through a list - percorrendo uma lista 
##for name in ['Hiromi', 'Yuji']:
    #print(name)

#exemplo 2 - looping a number of times 

##for index in range(0,3): #uma lista de números é criado
    #print(index) #aqui vai printar apenas os números 0,1 e2 e caímos naquele mesmo caso, em que o último dígito não é impresso. 

#exemplo 3 - while - looping with condition 

##names = ['Laiz' , 'Marcos']
#i = 0 
#while i < len(names):#leia, enquanto i(contador) for menor que o número de itens dentro da lista names, faça tal ação: 
    #print(names[i])
    #i = i + 1 #para acontecer o loop

#aula 28 loops code 

people = ['Yuji', 'Hiromi']

#for name in people:
    #print(name)

i = 0
while i <len(people):
    print(people[i])
    i = i + 1