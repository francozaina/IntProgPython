import math, random
from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import List, Dict, Tuple, Any
#Guia 8
#Auxiliar
pila = Pila()
pila.put(1)
pila.put(2)
pila.put(5)
pila.put(2)
pila.put(1)
def mostrar_pila (pila :Pila[Any]) -> Pila[Any]:
    pila_auxiliar = Pila()
    while not pila.empty():
        elemento = pila.get()       
        pila_auxiliar.put(elemento)
    while not pila_auxiliar.empty():       
        elemento = pila_auxiliar.get()
        print(elemento)
        pila.put(elemento)
    return pila    
#Ejercicio 1
#1.1
def generar_numeros_al_azar (cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    cont = 0
    while cont < cantidad:
        pila.put(random.randint(desde, hasta))
        cont += 1
    print("Los numeros al azar son:")
    mostrar_pila(pila)        
    return pila    
generar_numeros_al_azar(5,1,10)
#1.2
def cantidad_elementos (pila :Pila[Any]) -> int:
    cont = 0
    pila_auxiliar = Pila()
    while not pila.empty():
        elemento = pila.get()
        cont +=1       
        pila_auxiliar.put(elemento)
    while not pila_auxiliar.empty():       
        elemento = pila_auxiliar.get()
        pila.put(elemento)
    return cont    
print("La cantidad de elementos es :",cantidad_elementos(pila))
#1.3
def buscar_el_maximo (pila :Pila[Any]) -> int:
    maximo = 0
    pila_auxiliar = Pila()
    while not pila.empty():
        elemento = pila.get()
        if elemento > maximo:
            maximo = elemento
        pila_auxiliar.put(elemento)
    while not pila_auxiliar.empty():       
        elemento = pila_auxiliar.get()
        pila.put(elemento)  
    print("El elemento mas grande es:", maximo)
    return maximo
buscar_el_maximo(pila)
#1.4
notas = Pila()
notas.put(("Carlos", 8))
notas.put(("Julián", 10))
notas.put(("Ricardo", 1))
def buscar_nota_maxima (notas : Pila[Tuple[str, int]]) -> Tuple[str, int]:
    pila_auxiliar = Pila()
    nota_maxima = ("", 0)
    while not notas.empty():
        elemento = notas.get()
        if elemento[1] > nota_maxima[1]:
            nota_maxima = elemento
        pila_auxiliar.put(elemento)
    while not pila_auxiliar.empty():       
        elemento = pila_auxiliar.get()
        notas.put(elemento)
    print ("La nota mas alta es", nota_maxima)            
    return nota_maxima
buscar_nota_maxima(notas)    

    

    

    








          


    
