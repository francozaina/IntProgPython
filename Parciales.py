import math
from typing import List, Dict, Tuple
#veterinaria
def stock_productos (stock_cambios: list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
    despensa:dict[str,tuple[int,int]] = {}
    for nombre, cantidad in stock_cambios:
        if nombre not in despensa:
            despensa[nombre] = (cantidad, cantidad)
        else:
            minimo, maximo = despensa[nombre]
            if cantidad > maximo:
                maximo = cantidad
            elif cantidad < minimo:
                minimo = cantidad
            despensa[nombre] = (minimo,maximo)
    return despensa
stock = [('leche', 10), ('pan', 5), ('arroz', 7), ('leche', 2), ('pan', 2), ('arroz', 10)] 
print(stock_productos(stock))
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
codigos = [100101,111002,333003,123213]
def filtrar_codigos_primos (codigos:list[int])-> int:
    ultimos_digitos = 0
    res = []
    for i in range (len(codigos)):
        ultimos_digitos = codigos[i]
        if es_primo(ultimos_digitos % 1000) == True:
            res.append(ultimos_digitos)
    print(res)
    return res
filtrar_codigos_primos(codigos)        
tipos_pacientes = [
    "perro", "gato", "conejo", "perro", "gato","perro", "perro","loro", "conejo", "perro"
]
def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    indice_de_mayor_secuencia = 0
    cont_actual = 0
    cont_maximo = 0
    for i in range (len(tipos_pacientes_atendidos)):
        actual = tipos_pacientes_atendidos[i]
        if actual == "perro" or actual == "gato":
            cont_actual += 1
        else:
            if cont_actual > cont_maximo:
                cont_maximo = cont_actual
                indice_de_mayor_secuencia = i - cont_actual
                cont_actual = 0
    if cont_actual > cont_maximo:
        indice_de_mayor_secuencia = len(tipos_pacientes_atendidos) - cont_actual
    print ("el indice de la mayor secuencia es:",indice_de_mayor_secuencia)               
subsecuencia_mas_larga(tipos_pacientes)
grilla = [
    ["Ana", "Ana", "Ana", "Ana", "Ana", "Ana", "Ana"],  # 9 hs
    ["Ana", "Ana", "Sofi", "Ana", "Ana", "Ana", "Ana"],  # 10 hs
    ["Ana", "Ana", "Sofi", "Ana", "Ana", "Ana", "Ana"],  # 11 hs
    ["Ana", "Ana", "Sofi", "Ana", "Ana", "Ana", "Ana"],  # 12 hs
    ["Leo", "Leo", "Leo", "Juan", "Leo", "Leo", "Leo"],   
    ["Leo", "Leo", "Leo", "Leo", "Leo", "Leo", "Leo"],  
    ["Leo", "Leo", "Leo", "Leo", "Leo", "Leo", "Leo"],
    ["Leo", "Leo", "Leo", "Leo", "Leo", "Leo", "Leo"],
]

def columna(matriz: List[List[int]], num: int) -> List[int]:
    lista_final = []
    for fila in matriz:
        lista_final.append(fila[num])
    print("La columna", num, "es", lista_final)
    return lista_final

def un_responsable_por_turno (grilla: list[list[str]]) -> list[tuple[bool,bool]]:
    lista_final = []
    for dia in range(len(grilla[0])):
        dia_actual = columna(grilla, dia)
        if dia_actual[0] == dia_actual [1] and dia_actual[0] == dia_actual [2] and dia_actual [0] == dia_actual[3]:
            mañana  = True
        else:
            mañana  = False
        if dia_actual[4] == dia_actual [5] and dia_actual[4] == dia_actual [6] and dia_actual [4] == dia_actual[7]:
            tarde = True
        else:
            tarde = False
        tupla = (mañana, tarde)
        lista_final.append(tupla)
    print(lista_final)
    return lista_final
un_responsable_por_turno(grilla)
#Sala de escape
def promedio_de_salidas(registro: Dict[str, List[int]]) -> Dict[str, Tuple[int, float]]:
    resultado = {}
    for persona in registro:
        tiempos = registro[persona]
        salidas_exitosas = []
        for t in tiempos:
            if 1 <= t <= 60:
                salidas_exitosas.append(t)      
        cantidad = len(salidas_exitosas)
        if cantidad > 0:
            promedio = sum(salidas_exitosas) / cantidad
        else:
            promedio = 0.0
        
        resultado[persona] = (cantidad, promedio)
    
    return resultado       
tiempos = [0, 15, 61, 10, 20]
def tiempo_mas_rapido (tiempos:List[int])-> int:
    mejor_tiempo = 60
    cont = 0
    #busco mejor tiempo
    for i in range (len(tiempos)) :
        if tiempos[i]< mejor_tiempo and tiempos[i]<61 and tiempos[i]>=1:
            mejor_tiempo = tiempos[i]
    #busco el indice
    for j in range (len(tiempos)):
        if tiempos[j] != mejor_tiempo:
            cont+=1
        else:
            print ("el mejor tiempo fue",mejor_tiempo, "y esta en el indice",cont)
            return cont   
tiempo_mas_rapido(tiempos)
tiempos = [0, 15, 20, 25, 61, 5, 6]
# Racha más larga: [15, 20, 25] → índices 1 a 3
# Resultado esperado: (1, 3)
def racha_mas_larga (tiempos:List[int]) -> Tuple[int, int]:
    mejor_racha = 0
    cont = 0
    inicio_racha = 0
    final_racha = 0
    for i in range (len(tiempos)):
        if tiempos[i]<61 and tiempos[i]>=1 :
            cont += 1
        else:
            if cont > mejor_racha:
                mejor_racha = cont
                inicio_racha = i - cont
                final_racha = i-1
                cont = 0     
    res = (inicio_racha, final_racha)
    print("La mejor racha fue", mejor_racha, "y paso entre estos indices", res)
    return res
racha_mas_larga(tiempos)
amigos_por_salas = [
    [0, 0, 20, 0],  # ✅
    [0, 0, 45, 0],  # ✅
    [0, 0, 0, 0],   # ❌ el tercero no fue
    [1, 0, 10, 0],  # ❌ el primero fue
    [0, 0, 30, 1],  # ❌ el cuarto fue
]
def escape_en_solitario (matriz: List[List[int]])->List[int]:
    res = []
    for fila in range(len(matriz)):
        fila_actual = matriz[fila]
        if fila_actual[0] == 0 and fila_actual[1] == 0 and fila_actual[2]!=0 and fila_actual[3] == 0:
            res.append(fila)
    print (res)
    return res
escape_en_solitario(amigos_por_salas)
#gallinas
def torneo_de_gallinas(estrategias: Dict[str, str]) -> Dict[str, int]:
    jugadores = list(estrategias.keys())
    
    # Inicializar puntajes con for convencional
    puntajes = {}
    for jugador in jugadores:
        puntajes[jugador] = 0

    # Comparar todos contra todos una sola vez
    for i in range(len(jugadores)):
        for j in range(i + 1, len(jugadores)):
            j1 = jugadores[i]
            j2 = jugadores[j]
            e1 = estrategias[j1]
            e2 = estrategias[j2]

            if e1 == "me la banco y no me desvío" and e2 == "me la banco y no me desvío":
                puntajes[j1] = puntajes[j1] - 5
                puntajes[j2] = puntajes[j2] - 5
            elif e1 == "me desvío siempre" and e2 == "me desvío siempre":
                puntajes[j1] = puntajes[j1] - 10
                puntajes[j2] = puntajes[j2] - 10
            elif e1 == "me la banco y no me desvío" and e2 == "me desvío siempre":
                puntajes[j1] = puntajes[j1] + 10
                puntajes[j2] = puntajes[j2] - 15
            elif e1 == "me desvío siempre" and e2 == "me la banco y no me desvío":
                puntajes[j1] = puntajes[j1] - 15
                puntajes[j2] = puntajes[j2] + 10

    return puntajes
