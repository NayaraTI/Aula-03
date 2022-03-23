## Manipulando arquivos TXT

## Abrindo um arquivo somente leitura ##

arq1 = open('arquivos/arquivo.txt','r')

## Lendo o arquivo

print(arq1.read())

# Fechando um arquivo

arq1.close()


## Abrindo um arquivo para gravação e leitura

arq2 = open('arquivos/arquivo.txt','w+')

arq2.write("Tem novo Conteúdo\n")
arq2.write("Tem novamente uma nova linha\n")

print(arq2.seek(0,0))
print(arq2.read())

arq2.close()


### Gerenciador de Contexto de Arquivo ###

with open('arquivos/arquivo1.txt,w+') as f: