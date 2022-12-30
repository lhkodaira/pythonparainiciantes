#criei um novo arquivo para colocar o segundo exemplo da aula 29

#first_name = input('Escreva seu primeiro nome: ')
#first_name_initial = first_name[0:1]
#last_name = input('Escreva seu sobrenome: ')
#last_name_initial = last_name[0:1]

#print('Suas iniciais são ' + first_name_initial + last_name_initial)

#vou criar uma função sozinha para este problema 

#def initials (name):
    #print(name[0:1])
    
#first_name = input('Escreva seu primeiro nome: ')
#last_name = input('Escreva seu sobrenome: ')


#solução da professora 

#def get_initial(name): 
 #   initial = name[0:1].upper() #é possível adicionar modificadores de caracteres 
  #  return initial  #coloca-se return para que o valor obtido seja transferido à variável que estiver no 'name'

#first_name = input('Escreva seu primeiro nome: ')
#first_name_initial = get_initial(first_name) # vai pegar o valor dado para first_name e será colocado na função, 
#o valor que a função retornar será passado para o first_name_initial 
#last_name = input('Escreva seu sobrenome ')
#last_name_initial = get_initial(last_name)

#print('Suas iniciais são ' + first_name_initial + last_name_initial)

# uma segunda maneira de resolver esse problema dado pela professora 

def get_initial(name): 
    initial = name[0:1].upper() #é possível adicionar modificadores de caracteres 
    return initial  #coloca-se return para que o valor obtido seja transferido à variável que estiver no 'name'

first_name = input('Escreva seu primeiro nome: ')
#o valor que a função retornar será passado para o first_name_initial 
last_name = input('Escreva seu sobrenome ')


print('Suas iniciais são ' + get_initial(first_name) + get_initial(last_name))