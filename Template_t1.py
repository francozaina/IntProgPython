from queue import Queue as Cola
# Ejercicio 1
def maximas_cantidades_consecutivos (v: list[int]) -> dict[int,int]:
    return {}
 
# Ejercicio 2
def columna (A: list[list[int]], num : int) -> list[int]:
    lista_final = []
    for fila in A:
        lista_final.append(fila[num])
    print("La columna",num,"es",lista_final) 
    return lista_final

def es_primo (n:int)->bool:
    div = 1
    cont = 0
    res = True
    while div <= n:
        if n % div == 0:
            cont += 1
        div +=1
    if cont > 2 :
        res = False
    print(res)
    return res

def cantidad_primos(lista:list[int])-> int:
    res = 0
    for i in lista:
        if es_primo(i):
            res += 1
    print(res)
    return res


def maxima_cantidad_primos(A: list[list[int]]) -> int:
    columnas = len(A[0])
    max_primos = 0
    for indice in range(columnas):
        cant = cantidad_primos(columna(A, indice))
        if cant > max_primos:
            max_primos = cant
    return max_primos

A2 = [
    [4, 6, 3],
    [9, 10, 2],
    [14, 15, 1]
]

print(maxima_cantidad_primos(A2))
# Ejercicio 3
c = Cola()
c.put([-1,2])
c.put([1,2])
c.put([1,0])
c.put([-1,4])
c.put([1,3])

def mostrar_cola(c:Cola):
    c_aux = Cola()
    while not c.empty():
        elemento = c.get()
        print (elemento)
    
def tuplas_positivas_y_negativas(c: Cola[tuple[int, int]]) -> None:
    c_postivas = Cola()
    c_negativas = Cola()
    while not c.empty():
        elemento = c.get()
        if elemento [0] * elemento [1] > 0 :
            c_postivas.put(elemento)
        elif elemento [0] * elemento [1] < 0:
            c_negativas.put(elemento)
    while not c_postivas.empty():
        elemento = c_postivas.get()
        c.put(elemento)
    while not c_negativas.empty():
        elemento = c_negativas.get()
        c.put(elemento)    
tuplas_positivas_y_negativas(c)

# Ejercicio 4
def resolver_cuenta(s: str) -> float:
    res = 0.0
    i = 0
    while i< len(s):
        temp :str = s[i]
        j:int = i+1
        while j< len(s) and s[j] not in ['+','-']:
            temp += s[j]
            j+=1
        res += float(temp)
        i=j
    print(res)
    return res
resolver_cuenta("+10-5")