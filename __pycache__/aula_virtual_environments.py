#por padrão, os pactes são instalados globalmente 
# o que é bom, mas pode ser ruim em alguns casos 

#iremos instalar localmente, apenas para a nossa aplicação 

##criando um ambiente virtual 
#pip install virtualenv 

# Whindows Systems 
## python -m venv <folder_name> # aqui estaremos especificando onde queremos que seja criado o ambiente virtual 

# Usando o ambiente virtual
# se for no cmd.exe
## <folder_name>\Scripts\Activate.bat 

#se for no Powershell 
## <folder_name>\Scripts\Activate.ps1
# 
#se for no bash shell 
# . ./<folder_name>\Scripts\activate 
 
# Para instalar pacotes no ambiente virutal
# para instalar um pacote individual 
##pip install colorama 

# para instalar de uma lista de pacotes 
## pip install -r requieriments.txt

# requeriments.txt
# colorama 

