import math
#Guia 6
#1.1
def imprimir_hola():
    print ("Hola")

imprimir_hola()
#1.2
def raiz():
    print(math.sqrt(3))

raiz()
#1.5
def perimetro()-> float:
    res: float = 1*2*math.pi
    print (res)
    return (res)

perimetro()
#2.5
def es_multiplo(n:int, m:int)-> bool :
    if (n%m == 0):
        return (True)
    else:
        return (False)

print (es_multiplo(10,5))
#3.3
def es_nombre_largo (nombre:str)-> bool:
    res:bool = len (nombre) >= 3 and len (nombre) <= 8 
    return res
print (es_nombre_largo("papu"))
#5.1
def devolver_el_doble_si_es_par (n:int) -> bool:
    if (n%2==0):
        return (n*2)
    else:
        return (n)


    
