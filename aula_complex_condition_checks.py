
from statistics import median


media = float(input('Qual a sua média final?: '))
curso_finalizado = float(input('Quanto da graduação você já concluiu?: '))

if media >= 5.0 and curso_finalizado >= 80.0:
    formacao = True 
else:
    formacao = False 

if formacao:
    print('Muito bem, você poderá se formar este ano!')
else:
    print('Sinto muito, mas não poderá se formar ainda.')