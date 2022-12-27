#se usarmos uma variável que comporte um número e colocarmos para printar 
#o python ficará confuso se a váriavel é um numero ou string e emitirá um erro
#desta forma, se quisermos que o número seja apresentado na string, teremos que realizar uma conversão:

days_in_feb = 28  #comunicado dessa forma, ela é um int 
print(str(days_in_feb) + ' days in February.') #assim o python entende o código 
print()

#mas, números tbm podem se apresentar como strings, vide exemplo: 
first_num = '9'
second_num = '8'
print(first_num + second_num)

#a função input sempre irá retornar uma string 
third_num = input('Coloque o primeiro número: ')
fourth_num = input('Coloque o segundo número: ') 
print(third_num + fourth_num + ' ( print apenas das varíaveis sem conversão)') # neste exemplo fica bem claro que apesar de estarmos somando as variáveis
# o computador apenas printa seus valores. Para que realize a conta matemática é preciso converter: 
print(int(third_num) + int(fourth_num))
print(float(third_num) + float(fourth_num))
