
## Os geradores trabalham com otimização de memória onde não
## é necessário carregar todos os elementos na memória da função ou da
## estrutura de dados

## Criar uma função normal sem ser a geradora

import time
from tkinter.font import nametofont

def funcgerador():
    l = []
    for n in range(100):
        l.append(n)
        time.sleep(0.1)
    return l 

# Jogando a função em memória
gen1 = funcgerador()

#print(gen1)


### Para criar uma função geradora utilizamos o método yield

def funcgerador1():
    for n in range(100):
        yield n
        time.sleep(0.1) 
    
        
gen2 = funcgerador1()

#print(gen2)

#for i in gen2:
    #print(i)
    

## Criando uma lista de geradoras

## Para transformar uma list comprehension em geradora basta
# substituir por parênteses

lc1 = (l for l in range(100)) #geradora

#for i in lc1:
    #print(i)
    
lc2 = [l for l in range(100)] #normal
    
for i in lc2:
    print(i)
    
print(lc2)

## Vamos utilizar o método getsizeof da biblioteca sys

print("Memórias")
import sys

print(sys.getsizeof(lc1))
print(sys.getsizeof(lc2))




    