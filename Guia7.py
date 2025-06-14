import math
from typing import List, Dict, Tuple
#Guia 7
#Ejercicio 1
#1.1
def pertenece (lista:List[int], num:int) -> bool:
    for i in lista:
        if (num == i):
            res = True
            return res       
    res = False
    return res
pertenece ([1,2,3],4)
#1.2
def divide_a_todos (lista:List[int], num:int) -> bool:
    cont = 0
    for i in lista:
        if (i%num==0):
            cont = cont + 1
    if (cont == len(lista)):
        res = True
        print ("El numero",num, "divide a todos en la lista? ",res)
        return res
    else:
        res = False
        print ("El numero",num, "divide a todos en la lista? ",res)
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
    print ("La suma de todos los numeros de la lista es :",total)
suma_a_todos ([1,2,3])
#1.4
def maximo (lista:List[int]) -> int:
    max = 0
    for i in lista:
        if (max < i):
            max = i
    print ("El mayor número es:", max)
    return max
maximo ([1,2,4,3])
#1.5
def minimo (lista:List[int]) -> int:
    min = 1
    for i in lista:
        if (min > i):
            min = i           
    print ("El menor número es:", min)
    return min
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
        return True
    else:
        return False
ordenados ([1,2,3,4,5])
#1.7
def pos_maximo(lista: List[int]) -> int:
    mayor = maximo(lista)
    contador = 0
    for i in lista:
        if i == mayor:
            print("El maximo numero esta en la posicion : ", contador)
            return contador           
        contador += 1  
pos_maximo ([1,2,5,3,4])
#1.8
def pos_minimo (lista: List[int]) -> int:
    menor = minimo(lista)
    contador = 0
    for i in lista:
        if i == menor:
            print ("El menor numero esta en la posicion : ",contador)
            return contador
        contador = contador +1
pos_minimo ([2,5,1,4])  
#1.9
def mayor_a_siete (lista: List[str]) -> bool:
    for i in lista:
        res = False
        if (len(i)>7):
            res = True
    if (res == True):
        print("La lista contiene una palabara con mas de 7 letras?", res)
    else:
        print("La lista contiene una palabara con mas de 7 letras?", res)                  
lista1 = ["termo", "gato", "tener", "Franco"]
mayor_a_siete(lista1)
#1.10
def es_palindromo (palabra:str)-> bool:
    if (palabra == palabra[::-1]):
        res = True
        print("La palabra es palindromo?", res)
    else:
        res = False   
        print("La palabra es palindromo?", res)
es_palindromo("yatay")
#1.11
#1.12
def vocales_distintas (palabra:str) -> bool:
    vocales = []
    contador_iguales = 0
    for i in palabra:
        if i == "a" or i == "e" or i == "i" or i =="u":
            vocales.append(i)
    for j in vocales:
        if vocales[0] == j:
            contador_iguales = contador_iguales + 1
    if contador_iguales == len(vocales):
        res = True
        print("La palabra tiene 3 vocales distintas?", res )
        return res
    else:
        res = False
        print("La palabra tiene 3 vocales distintas?", res )
        return res
vocales_distintas("denado")           
#1.14
def cantidad_digitos_impares(lista: list[int]) -> int:
    contador = 0
    for numero in lista:
        for digito in str(numero):  
            if int(digito) % 2 != 0:  
                contador += 1
    print("En la lista hay", contador, "dígitos impares")
    return contador
cantidad_digitos_impares([15, 7, 9])
#Ejercicio 2
#2.1
def ceros_en_posiciones_pares(lista: list[int]):
    for i in range(len(lista)):  
        if i % 2 == 0:  
            lista[i] = 0
    print("La lista nueva es", lista)
ceros_en_posiciones_pares([1, 2, 3, 4, 5, 6]) 
#2.3
def problema_sin_vocales(frase: str) -> List: 
    frase_sin_vocales = []
    for i in range(len(frase)):
        if (frase[i] != "a" and 
            frase[i] != "e" and 
            frase[i] != "i" and 
            frase[i] != "o" and 
            frase[i] != "u" and
            frase[i] != "A" and 
            frase[i] != "E" and 
            frase[i] != "I" and 
            frase[i] != "O" and 
            frase[i] != "U"):
            frase_sin_vocales.append(frase[i])
    print("La frase sin vocales es:", frase_sin_vocales)            
problema_sin_vocales("Esto es epico")
#2.4
def problema_remplaza_vocales (frase: str) -> str: 
    frase_nueva = []
    for i in range(len(frase)):
        if (frase[i] != "a" and 
            frase[i] != "e" and 
            frase[i] != "i" and 
            frase[i] != "o" and 
            frase[i] != "u" and
            frase[i] != "A" and 
            frase[i] != "E" and 
            frase[i] != "I" and 
            frase[i] != "O" and 
            frase[i] != "U"):
            frase_nueva.append(frase[i])
        else:
            frase_nueva.append('-')
    print("la frase con vocales remplazadas es:",frase_nueva)        
problema_remplaza_vocales("papus de papus")
#2.5
def problema_dar_vuelta_str (frase: str) -> str:
    frase_nueva = []
    for i in range(len(frase),0,-1):
        frase_nueva.append(frase[i-1])
    print("La frase en reversa es:",frase_nueva)
problema_dar_vuelta_str("Hola papus")    
#2.7
def problema_materia(notas: List[int]) -> int:
    total = 0
    for i in range(len(notas)):
        total += notas[i]
    promedio = total / len(notas)
    res = 1
    for i in range(len(notas)):
        if notas[i] < 4:
            res = 3
            break
    if res != 3:
        if promedio < 4:
            res = 3
        elif promedio < 7:
            res = 2
        else:
            res = 1   
    print("El estado de aprobación es :", res)
    return res
notas = [2, 3, 2]
problema_materia(notas)  
#2.8
def problema_saldo_actual(movimientos: List[Tuple[str, int]]) -> int:
    saldo_actual = 0
    for i in range(len(movimientos)):
        tipo, monto = movimientos[i]
        if tipo == "I":
            saldo_actual += monto
        elif tipo == "R":
            saldo_actual -= monto
        else:
            print("Comando inválido.")
    print("El saldo actual es :", saldo_actual)
    return saldo_actual
movimientos = [("I", 2000), ("R", 20)] 
problema_saldo_actual(movimientos)
#Ejercicio 3
#3.1
m = [[1, 2, 3],
    [7, 5, 4],
    [8, 1, 5]]
def problema_pertenece_a_matriz (matriz:List[List[int]], num:int) -> bool :
    res : bool
    for col in range (len(matriz[0])):
        for row in range (len(matriz)):
            if pertenece(matriz[row], num) == True:
                res = True
                print ("El numero",num, "pertenece a la matriz?:", res)
                return res                
            else:               
                res = False
    print ("El numero",num, "pertenece a la matriz?:", res)                  
problema_pertenece_a_matriz(m,1)
#3.2
def problema_es_matriz (matriz:List[List[int]])-> bool:
    res: bool
    if len(matriz) == 0:
        print("m es matriz?", res)
        return False
    if len(matriz[0]) == 0:
        print("m es matriz?", res)
        return False 
    num_columnas = len(matriz[0])
    for fila in matriz:
        if len(fila) != num_columnas:
            res = False
            print("m es matriz?", res)
            return False
    res = True
    print("m es matriz?", res)       
    return True
problema_es_matriz(m)
#3.3
def filas_ordenadas (matriz:List[List[int]]) -> List[bool]:
    res = []
    cantidad_filas = 0
    for filas in matriz:
        cantidad_filas += 1
    for fila in range(cantidad_filas):
        fila_actual = matriz[fila]
        if ordenados(fila_actual) == True:
            res.append(True)      
        else:
            res.append(False)           
    print(res)
    return res                        
filas_ordenadas(m)
#3.4
def columna (matriz:List[List[int]], num : int) -> List[int]:
    lista_final = []
    for fila in matriz:
        lista_final.append(fila[num])
    print("La columna",num,"es",lista_final) 
    return lista_final   
columna(m,1)
#3.5
def columnas_ordenadas (matriz:List[List[int]]) -> List[bool]:
    res = []
    cont = 0
    col = []
    for columna in range (len(matriz[0])):
        for fila in matriz:
            col.append(fila[cont])     
        if ordenados(col) == True:
            res.append(True)
            col = []
        else:
            res.append(False)
            col = []
        cont += 1         
    print (res)
    return res                                     
columnas_ordenadas(m)
#3.6
m2 =[[1, 2, 3],
    [4, 5, 6]]
def transponer (matriz:List[List[int]])-> List[List[int]]:
    transpuesta = []
    for columna in range(len(matriz[0])):
        col = []
        for fila in matriz:
            col.append(fila[columna])
        transpuesta.append(col)
    print(transpuesta)
    return transpuesta          
transponer(m2)

#3.7
#Auxiliares
tablero = [['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', 'X']]

def columnaTateti (tateti:List[List[str]], num : int) -> List[str]:
    lista_final = []
    for fila in tateti:
        lista_final.append(fila[num])
    return lista_final

def filaTateti(tateti:List[List[str]], num : int) -> List[str]:
    lista_final = []
    for fila in tateti[num]:
        lista_final.append(fila)
    return lista_final

def diagonalTateti(tateti:List[List[str]]) -> List[str]:
    lista_final = []
    num = 0
    for fila in tateti:
        lista_final.append(fila[num])
        num += 1
    return lista_final
 
def diagonalInversaTateti(tateti:List[List[str]]) -> List[str]:
    lista_final = []
    num = 2
    for fila in tateti:
        lista_final.append(fila[num])
        num -= 1
    return lista_final
diagonalInversaTateti(tablero)

def tateti (tablero:List[List[str]])-> int:
    res = 0
    num = 0
    #Chequeo las X
    for i in range (len(tablero[0])):
        if columnaTateti(tablero,num) == ["X","X","X"]:
            res = 1
            return res
        num += 1
    num = 0
    for j in range(len(tablero[0])):
        if filaTateti(tablero,num) == ["X","X","X"]:
            res = 1
            return res
        num +=1
    if diagonalTateti(tablero) == ["X","X","X"]:
        res = 1
        return res  
    elif diagonalInversaTateti(tablero) == ["X","X","X"]:
        res = 1
        return res
    #Chequeo las O
    num = 0
    for k in range (len(tablero[0])):
        if columnaTateti(tablero,num) == ["O","O","O"]:
            res = 0
            return res
        num += 1
    num = 0
    for m in range(len(tablero[0])):
        if filaTateti(tablero,num) == ["O","O","O"]:
            res = 0
            return res
        num +=1
    if diagonalTateti(tablero) == ["O","O","O"]:
        res = 0
        return res  
    elif diagonalInversaTateti(tablero) == ["O","O","O"]:
        res = 0
        return res
    #Si no entra a nada devuelve empate
    res = 2
    return res
print(tateti(tablero)) 






    

    

    








          


    
