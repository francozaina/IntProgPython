import math
from typing import List, Dict, Tuple
#Guia 7
#Ejercicio 1
#1.1
def pertenece (lista:List[int], num:int) -> bool:
    for i in lista:
        if (num == i):
            res = True
            print(res)
            return res       
    res = False
    print (res)
    return res
pertenece ([1,2,3],4)
#def pertenece2 (lista:List[int], num:int) -> bool:
#1.2
def divide_a_todos (lista:List[int], num:int) -> bool:
    cont = 0
    for i in lista:
        if (i%num==0):
            cont = cont + 1
    if (cont == len(lista)):
        res = True
        print (res)
        return res
    else:
        res = False
        print (False)
        return False 
divide_a_todos ([4,6,8],3)        
def divide_a_todosPACHO (lista:List[int], num:int) -> bool:
    cont = 0
    for i in lista:
        if (i%num!=0):
            return False       
    return True
#1.3
def suma_a_todos (lista:List[int]) -> int:
    total = 0
    for i in lista:
        total = total + i
    print (total)
suma_a_todos ([1,2,3])
#1.4
def maximo (lista:List[int]) -> int:
    max = 0
    for i in lista:
        if (max < i):
            max = i
    print (max)
maximo ([1,2,4,3])
#1.5
def minimo (lista:List[int]) -> int:
    min = 1
    for i in lista:
        if (min > i):
            min = i           
    print (min)
minimo ([5,2,4,1])
#1.6
def ordenados (lista:List[int]) -> bool:
    cont = 0
    anterior = 0
    for i in lista:
        if (i>anterior):
            cont = cont + 1
            anterior = i
    if (cont == len(lista)):
        res = True
        print (res)
    else:
        res = False
        print (res)
ordenados ([1,2,3,4,5])
def columnas_ordenadas (m:List[List[int]]) -> List[bool]:
    
    res : list [bool] = []
    columna : list[int] = []
    for col in range (len(m[0])):
        for row in range (len(m)):
            columna : list [int] = []
        if (ordenados (columna)== True):
            res.append(True)
        else:
            res.append (False)
        columna.clear()
    return res            

m4 =    [[1, 4, 7],
        [5, 2, 8],
        [3, 6, 9]]
print(columnas_ordenadas(m4))






    

    

    








          


    
