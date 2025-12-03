from queue import LifoQueue as Pila # importa LifoQueue y le asigna el alias Pila
def es_multiplo (n:int,m:int)->bool:
    res = False
    if n % m == 0 :
        res = True
    return res
es_multiplo(20,2)

def es_par (n:int)-> bool:
    res = False
    if n %2 == 0:
        res = True
    return res
es_par(18)

def alguno_es_0 (n:int,m:int) -> bool:
    res = False
    if n == 0 or m == 0:
        res = True
    return res

def ambos_son_0 (n:int,m:int) -> bool:
    res = False
    if n == 0 and m == 0:
        res = True
    return res

def es_bisiesto (ano:int) -> bool:
    res = False 
    if es_multiplo (ano,400) == True :
        res = True
    elif es_multiplo(ano,4) and not es_multiplo(ano,100) :
        res = True
    return res
es_bisiesto(2020)

def uno_al_diez () :
    n = 0
    while n < 10:
        n += 1
        print (n)

def pares_40 ():
    n = 0 
    while n < 40:
        n +=2
        print (n)

def despegue (n:int):
    while n >= 1:
        print (n)
        n-=1
    print ("despegue")

def pertenece (lista : list, n:int) -> bool:
    res = False
    for elemento in lista:
        if elemento == n :
            res = True
            return res
    return res    

def divide_a_todos (lista:list, n:int)-> bool:
    res = True
    for elemento in lista:
        if elemento % n != 0:
            res = False
            return res
    return res

def suma_total (lista:list)-> int:
    res = 0
    for elemento in lista:
        res = res + elemento
    print(res)    
    return res

def maximo (lista:list)->int:
    actual = lista[0]
    for elemento in lista:
        if elemento > actual:
            actual = elemento
    return actual

def minimo (lista:list) -> int:
    actual = lista[0]
    for elemento in lista:
        if elemento < actual:
            actual = elemento
    return actual

def ordenados (lista:list)-> bool:
    res = True
    longitud = len(lista)   
    for i in range(longitud - 1):        
        if lista[i] > lista[i + 1]:
            res = False
            return res  
    return res

def pos_maximo (lista:list)->int:
    res:int = -1
    if len(lista) == 0:
        return res
    indice:int = 0
    max= maximo(lista)
    for elemento in lista:
        if elemento == max:
            print(indice)
            res = indice
            return res
        else: indice += 1
    return res
pos_maximo([2])

def pos_minimo (lista:list)-> int:
    res:int =-1
    if len(lista) == 0:
        return res    
    min = minimo (lista)
    longitud = len(lista)
    for i in range(longitud):
        if lista[i] == min:
            res = i
    return res
pos_minimo([]) 

def long_mayor_a_7 (lista:list[str]) -> bool:
    res = False
    for palabra in lista:
        if len(palabra) > 7:
            res = True
            return res
    return res

def es_palindromo (palabra:str) -> bool:
    reverso = ""
    for letra in palabra:
        reverso = letra + reverso
    if palabra == reverso:
        return True
    return False
es_palindromo("a")

def iguales_cosecutivos (lista:list[int])->bool:
    res:bool = False
    longitud = len(lista)
    for i in range(longitud-2):
        if lista[i] == lista[i+1] and lista[i+1] == lista [i+2]:
            res = True
    return res
iguales_cosecutivos([2,3,2,4,4,2])

def vocales_distintas(palabra:str)->bool:
    vocales = ['a','e','i','o','u']
    for letra in palabra:
        if letra in vocales :
            vocales.remove(letra)
    if len(vocales) <= 2:
        return True
    else:
        return False
print (vocales_distintas("hola"))

def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    # --- 1. Inicialización del RÉCORD (Mejor caso) ---
    pos_mejor = 0
    long_mejor = 1
    
    # --- 2. Inicialización del ACTUAL (Caso presente) ---
    pos_actual = 0
    long_actual = 1
    
    # Recorremos hasta el anteúltimo para comparar con el siguiente
    for i in range(len(s) - 1):
        
        # ¿El actual es menor o igual al siguiente? (Sigue ordenado)
        if s[i] <= s[i+1]:
            long_actual = long_actual + 1
            
        else:
            # ¡Se rompió la racha!
            
            # A) Chequeamos si la que terminó es un nuevo récord
            if long_actual > long_mejor:
                long_mejor = long_actual
                pos_mejor = pos_actual
            
            # B) Reseteamos para empezar una nueva racha desde el siguiente
            pos_actual = i + 1
            long_actual = 1   
    # --- 3. EL CHEQUEO FINAL ---
    # Si la lista termina ordenada (ej: 1, 2, 3, 4, 5), el 'else' del bucle
    # nunca se ejecuta y no guardaríamos ese récord. Hay que hacerlo acá.
    if long_actual > long_mejor:
        pos_mejor = pos_actual
        # (No hace falta actualizar long_mejor porque ya terminamos)

    return pos_mejor

def cantidad_digitos_impares(lista:list[int])->int:
    contador = 0
    for numero in lista:
        num = str(numero)
        for digito in num:
            num2 = int(digito)
            if num2 % 2 != 0:
                contador += 1
    return contador
print(cantidad_digitos_impares([57, 2383, 812, 246]))

def sin_vocales (frase:str)->str:
    vocales =['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    frase_nueva =""
    for letra in frase:
        if letra not in vocales:
            frase_nueva = frase_nueva + letra
    print(frase_nueva)
    return frase_nueva

def dar_vuelta_str (frase:str) -> str:
    reverso = ""
    for caracter in frase:
        reverso = caracter + reverso
    print (reverso)
    return reverso
dar_vuelta_str("hola papu")


#MATRICES PAPU ESTO ES EPICO PAPUS
def es_matriz(m:list[list])->bool:
    if len(m) == 0:
        return False
    if len(m[0]) == 0:
        return False
    res = True
    longitud_fila = len(m[0])
    for fila in m:
        if len(fila) != longitud_fila:
            res = False
            return res
    return res 

def filas_ordenadas (m:list[list])->bool:
    res:bool=True
    for fila in m:
        if ordenados(fila) == False:
            res = False
            return res
    return res

m = [[5,2,3],[4,5,6],[7,8,9]]

def columna(m:list[list],n:int)->list:
    col:list = []
    for fila in m:
        col.append(fila[n])
    return col

print(columna(m,1))

def columnas_ordenadas(m:list[list])->bool:
    longitud = len(m[0])
    for i in range(longitud):
        if ordenados(columna(m,i)) == False:
            return False
    return True
print(columnas_ordenadas(m))

#GUIA 8, DICCIONARIOS, PILAS Y COLAS
# Un diccionario vacío
mi_diccionario = {}

# Un diccionario con datos (Clave: Valor)
# Clave: Nombre del alumno (String) -> Valor: Nota (Int)
notas = {
    "Ana": 10,
    "Juan": 4,
    "Lara": 8,
    
}
print(notas["Ana"]) # Imprime 10

#Verificar si existe la clave
if "Pedro" in notas:
    print(notas["Pedro"])
else:
    print("Pedro no tiene nota")

for estudiante in notas:
    print(estudiante)

for nombre, nota in notas.items():
    print("El alumno " + nombre + " se sacó un " + str(nota))

def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    sumas={}
    cantidades={}
    for nombre, nota in notas:
        if nombre in sumas:
            sumas[nombre] = sumas[nombre]+ nota
            cantidades[nombre] = cantidades[nombre] + 1
        else:
            sumas[nombre] = nota
            cantidades[nombre] = 1
    promedios = {}
    for nombre, suma_total in sumas.items():
        cantidad_de_examenes = cantidades[nombre]
        promedio = suma_total / cantidad_de_examenes
        promedios[nombre] = promedio
    return promedios

notas_ejemplo = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
print(calcular_promedio_por_estudiante(notas_ejemplo))

def mantuvieron_voto (eleccion1:dict[str,str], eleccion2:dict[str,str])->dict[str,int]:
    res = {}
    for nombre, voto in eleccion2.items():
        if voto == eleccion1[nombre]:
            if voto not in res:
                res[voto] = 1
            else: 
                res[voto] = res[voto] +1
    return res
        
def ultima_subsecuencia_que_suma(s: list[int], n: int) -> list[int]:
    mejor_inicio = 0
    mejor_fin = 0  
    longitud = len(s)  
    for i in range(longitud):       
        suma_actual = 0          
        for j in range(i, longitud):
            suma_actual = suma_actual + s[j]
            if suma_actual == n:
                mejor_inicio = i
                mejor_fin = j                   
    res = []
    for k in range(mejor_inicio, mejor_fin + 1):
        res.append(s[k])
    return res

#Ejercicio 18
inventario = {'papu': {'precio': 9.9, 'cantidad': 12}}
def agregar_producto (inventario:dict, nombre:str,precio:float,cantidad:int)-> dict:
    info = {}
    info ["precio"] = precio
    info ["cantidad"]= cantidad
    inventario[nombre]= info
    print (inventario)
    return inventario

def actualizar_stock (inventario:dict, nombre:str, cant:int)->dict:
    temp = {}
    temp = inventario[nombre]
    temp["cantidad"] = cant
    inventario[nombre]=temp 
    return inventario
actualizar_stock(inventario,"papu",1)

def actualizar_precio (inventario:dict, nombre:str, valor:float)->dict:
    inventario[nombre]["precio"]=valor
    print(inventario)
    return inventario
actualizar_precio(inventario, "papu", 10.0)


inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantal´on", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)


def calcular_valor_inventario (inventario:dict) -> float:
    acumulador:float = 0.0
    for nombre in inventario:
        actual = inventario[nombre]["precio"] * inventario[nombre]["cantidad"]
        acumulador = acumulador + actual
    print (acumulador)
    return acumulador
valor_total = calcular_valor_inventario(inventario)

print("Valor total del inventario:", valor_total)

#Pilas y colas
pila = Pila()
pila.put(1)
pila.put(15)
pila.put(3)

def mostrar_pila (pila:Pila)-> Pila:
    pila_aux = Pila()
    while not pila.empty():
        elemento = pila.get()
        pila_aux.put(elemento)
    while not pila_aux.empty():
        elemento=pila_aux.get()
        print(elemento)
        pila.put(elemento)
    return pila
mostrar_pila(pila)

def buscar_maximo (pila:Pila)->int:
    maximo = 0
    pila_aux = Pila()
    while not pila.empty():
        elemento = pila.get()
        if elemento > maximo:
            maximo = elemento
        pila_aux.put(elemento)
    while not pila_aux.empty():
        elemento = pila_aux.get()
        pila.put(elemento)
    print(maximo)
    return maximo
buscar_maximo(pila)
