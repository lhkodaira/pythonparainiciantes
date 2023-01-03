#### MÓDULO é um arquivo com funções, classe e outros componentes. 
#usado para quebrar o código em estruturas reutilizáveis 

#aula exemplo, criamos uma função no arquivo helpers.py 

#para importar o modulo, podemos fazer de três formas: 

##import module as namespace 
#import helpers
#helpers.display('not a warning') #dessa jeito teremos que declarar: nome do arquivo.função 

##import all into current namespace 
#from helpers import * # '*' significa 'everything', desta forma, leremos ' do arquivo helpers, importe tudo 
#display('not a warning') #dessa forma, na hora de utilizar a função, só precisaremos chamar a função 

## import specific items into current namespace 
#from helpers import display #parecido com a forma anterior, c a diferença que estamos importando apenas a função que queremos 
#display('testando', True)

### PACKAGES 
# é a coleção de módulos publicada
#encontram-se na internet 'Python Package Index' 

#Install packages 

## install an individual package 
#pip install colorama 

## Install from a list of packages 
#pip install -r requirements.txt 

## requeriments.txt 
#colorama 