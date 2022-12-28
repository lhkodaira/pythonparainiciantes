#lists são coleções de itens 

#names = ['Laiz', 'Marcos']
#scores = []
#scores.append(98) #append adiciona um item no final
#scores.append(99)
#scores.append(100)

#print(names)
#print(scores)
#print(scores[2])

#Arrays também podem ser coleções de itens 
#from array import array
#scores = array('d')
#scores.append(97)
#scores.append(98)
#print(scores)
#print(scores[1])

#Diferenças entre arrays e lists 
#lists guarda qualquer coisa e qualquer tipo 
#arrays amarzena dados de tipo numéricos e devem ser do mesmo tipo 
 
#operações comuns 
names = ['Laiz', 'Marcos']
print(len(names)) #mostra o número de itens dentro da lista 
print(names)
names.insert(0,'Hiromi') # adiciona na posição zero o nome Hiromi
print(names)
names.sort()
print(names)
names.append('Yuji')
presenca = names[:3] #atenção ao fato de que a última posição não será incluida('Yuji')
print(names)
print(presenca)

#Dictionaries
#Diferenças entre dicionários e listas 
#Dicionários possuem chave e valor, ficam em pares e seu armazenamento pode não ser ordenado 
#Listas possui ordem no armazenamento
person = {'first' : 'Laiz'} #chave = first , valor = Laiz 
person['last'] = 'Kodaira'
print(person)
print(person['first'])
print(len(person))