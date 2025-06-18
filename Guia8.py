import math, random
from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import List, Dict, Tuple, Any
#Guia 8
#Auxiliar
pila = Pila()
pila.put(1)
pila.put(2)
pila.put(3)
pila.put(4)
pila.put(5)
pila2 = Pila()
pila2.put("a")
pila2.put("b")
pila2.put("c")
pila2.put("d")
pila2.put("e")

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
#1.5
s = "(1+2)*(2+1)"
def esta_bien_balanceada(s: str) -> bool:
    pila = Pila()
    for caracter in s:
        if caracter == '(':
            pila.put('(')
        elif caracter == ')':
            if pila.empty():
                return False  
            pila.get()     
    return pila.empty()
print(esta_bien_balanceada(s))
#1.7
def intercalar (p1:Pila[Any], p2:Pila[Any]) -> Pila [Any]:
    pila_intercalada = Pila()
    pila_aux = Pila()
    #intercalo la pila
    while not p1.empty():
        elemento = p1.get()
        pila_aux.put(elemento)
        elemento2 = p2.get()        
        pila_aux.put(elemento2)
    #la doy vuelta
    while not pila_aux.empty():
        elemento3= pila_aux.get()
        pila_intercalada.put(elemento3)
    print ("pila intercalada:")
    mostrar_pila(pila_intercalada)
    return pila_intercalada
intercalar(pila,pila2)
#Ejercicio 2 Colas
cola = Cola()
cola.put(1)
cola.put(2)
cola.put(5)
cola.put(4)  
cola.put(1)
def mostrar_cola (cola:Cola[Any]) -> Cola[Any]:
    cola_auxiliar = Cola()
    while not cola.empty():
        elemento = cola.get()
        cola_auxiliar.put(elemento)
    while not cola_auxiliar.empty():
        elemento = cola_auxiliar.get(elemento)
        print(elemento)
        cola.put(elemento)
    return cola
print("La cola es:")
mostrar_cola(cola)
#2.1
def generar_numeros_cola (cantidad:int,desde:int, hasta:int) -> Cola[int]:
    cola = Cola()
    cont = 0
    while cont < cantidad:
        cola.put(random.randint(desde, hasta))
        cont += 1       
    print("La cola de randoms es:")
    mostrar_cola(cola)
    return cola
generar_numeros_cola(5,1,10)
#2.2
def cantidad_elementos (cola:Cola[Any]) -> int:
    cola_aux = Cola()
    cant_elementos = 0
    while not cola.empty():
        elemento = cola.get()
        cant_elementos += 1
        cola_aux.put(elemento)
    while not cola_aux.empty():
        elemento = cola_aux.get()
        cola.put(elemento)
    print ("La cantidad de elementos de la cola es:",cant_elementos)  
    return cant_elementos 
cantidad_elementos(cola)
#2.3
def buscar_maximo (cola:Cola[int]) -> int:
    maximo = 0
    cola_aux = Cola()  
    while not cola.empty ():
        elemento = cola.get()
        if elemento > maximo:
            maximo = elemento
        cola_aux.put(elemento)
    while not cola_aux.empty():
        elemento = cola_aux.get()
        cola.put(elemento)
    print("el elemento mas grande de la cola es:", maximo)
    return maximo
buscar_maximo (cola)
#2.4
notas = Cola()
notas.put(("Carlos", 1))
notas.put(("Julián", 10))
notas.put(("Ricardo", 2))
def buscar_nota_minima (notas : Cola[Tuple[str, int]]) ->  Tuple[str, int] :
    minima = ("", 10)
    cola_aux = Cola()
    while not notas.empty():
        elemento = notas.get()
        if elemento [1] <= minima [1]:
            minima = elemento
        cola_aux.put(elemento)
    while not cola_aux.empty():
        elemento = cola_aux.get()
        notas.put(elemento)
    print("La nota minima es:", minima)
    return minima
buscar_nota_minima(notas)

notas = [
    ("Ana", 9.0),
    ("Luis", 7.5),
    ("Ana", 8.0),
    ("Luis", 6.0),
    ("Sofía", 10.0)
]
def calcular_promedio_por_estudiante(notas: List[Tuple[str, float]]) -> Dict[str, float]:
    acumuladores: Dict[str, float] = {}
    cantidades: Dict[str, int] = {}

    for nombre, nota in notas:
        if nombre in acumuladores:
            acumuladores[nombre] += nota
            cantidades[nombre] += 1
        else:
            acumuladores[nombre] = nota
            cantidades[nombre] = 1

    promedios: Dict[str, float] = {}
    for nombre in acumuladores:
        promedios[nombre] = acumuladores[nombre] / cantidades[nombre]

    return promedios    

    

    

    








          


    
