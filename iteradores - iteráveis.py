########## Objetos Iteráveis ###########
# Estruturas de dados, lista, tuplas, dicionários, strings são objetos iteráveis

# Exemplo

lista = ["João",1," Pedro",45]

## Como checar se um elemento é iterável

## Métodos Mágicos ##
# São funções builtins do Python onde são escritas em formato de dunder ou duplo underline
# Método__iter__ - duplo underline__

## Estou abrindo a caixinha do for

# Checar se um elemento é iterável
# hasattr checa o atributo de um elemento

print(hasattr(lista,'__iter__'))

string = 'Florianópolis'

print(hasattr(string,'__iter__'))

##  Executando um iterador a um iterável

for s in string:
    print(s)
    
## Entender o processo dos iteradores

## Função não mágica chamada iter

## A função iter transforma um objeto iterável em iterador

listaiterador = iter(string)

print(type(listaiterador))

## Método mágico '_next_'  itera os elementos de memória

print(hasattr(listaiterador,'_next_'))

## Iterar a Memória

print(next(listaiterador))
print(next(listaiterador))
print(next(listaiterador))
print(next(listaiterador))
print("Separador de texto")

for i in listaiterador:
    print(i)
    

print(next(listaiterador))
    
    
