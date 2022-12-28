#frequentemente necessitamos usar data e hora para registrar erros e logins
#para isso, usaremos a biblioteca datetime 
from datetime import datetime, timedelta
from time import time

current_date = datetime.now()
# a função irá retornar um objeto com a datetime 
print('\nToday is: ' + str(current_date))

#tem funções que podem ser usadas com os objetos do datetime para manipulação de datas. 
#timedelta é usado para definir um periodo de tempo 
#importante, tem que "chamar" esta biblioteca
today = datetime.now()
one_day = timedelta(days=1) #determina a quantidade de dias que quer comparar 
one_week = timedelta(weeks=4)
yesterday = today - one_day
last_week = today - one_week
print('Last week was: ' + str(last_week))
print('Yesterday was: ' + str(yesterday) + '\n')
#não sei pq, mas não funcionou com month 

current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
print('Hour: ' + str(current_date.hour))
print('Minute: ' + str(current_date.minute))
print('Second: ' + str(current_date.second))

#muitas vezes receberemos uma data como string e teremos que converte-la em um objeto do datetime
birthday = input('Qual a sua data de nascimento (dd/mm/yyyy)?: ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Sua data de nascimento foi em ' + str(birthday_date))
birthday_eve = birthday_date - one_day
print('O dia anterior ao seu aniversário foi ' + str(birthday_eve))
#neste caso temos que o usuário terá que colocar a data exatamente no formato, qualquer espaço a mais ou simbolo diferente
#fará com que dê erro 

