#first_name = input('Qual o seu primeiro nome?')
#last_name = input('Qual o seu sobrenome?')
#print(first_name+last_name)
#print('Hello, ' + first_name + ' ' + last_name)

#modificando strings 
#sentence = 'The dog is named Sammy'
#print(sentence.upper())
#print(sentence.lower())
#print(sentence.capitalize())
#print(sentence.count('a'))

#essas funções ajudam a formatar strings e salvá-las nos arquivos e banco de dados de forma correta e uniforme, exemplo: 
from functools import update_wrapper


first_name = input('Qual o seu primeiro nome?: ')
last_name = input('Qual o seu sobrenome?: ')
#print('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize())

#customizando e formatando a string - Diferentes formas de escrever e ter o mesmo resultado 
#formas mais eficazes e simples de escrever


#output = 'Hello, ' + first_name + ' ' + last_name
#output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {0} {1}'.format(first_name, last_name)
#output = f'Hello, {first_name} {last_name}' #disponível apenas Python 3

print(output)