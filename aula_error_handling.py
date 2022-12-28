#error handling - tratamento de erro é diferente de Debugging 
#error handling é quando um erro acontece por eventos fora do nosso controle ex:mudança de banco de dados, problemas nas permissões 
#Debugging - depuração é quando existe um erro no código. 

#Error Types:
##Syntax errors : erro na forma da escrita do código na linguagem Python 

##Runtime errors : erro no código escrito. ex: divisão por 0

##Catching runtime errors


##Logic errors: é quando compila corretamente, não dá erros de sintaxe nem de runtime error mas há erro na lógica escrita
##no caso, erro de interpretação do programador 

#aula demonstrativa 

from ast import Try


x = 42 
y = 0

#print(x/y) gera um erro por ser divisão com zero 
## quando gerar esse erro, tentar:
try:
    print(x / y)
except ZeroDivisionError as e:
    print("Não é possível realizar esta divisão")
else: 
    print('Alguma coisa deu errado')
finally: 
    print('Esta é a nossa limpeza de código.')