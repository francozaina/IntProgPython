import math
#Guia 6
#Ejercicio 1
#1.1
def imprimir_hola():
    print ("Hola")    
#1.2
def imprimir_guns():
    print ("She got a smile")
    print ("That it seems to me")
imprimir_guns()
#1.3
def raiz():
    print(math.sqrt(3))
raiz()
#1.5
def perimetro()-> float:
    res: float = 1*2*math.pi
    print (res)
    return (res)

perimetro()

#Ejercicio 2
#2.3
def farenheit_a_celcius(n:int):
    res = (n-32)*5/9
    print (res)
    print(round(res, 4))   
#2.5
def es_multiplo(n:int, m:int)-> bool :
    if (n%m == 0):
        return (True)
    else:
        return (False)

print (es_multiplo(10,5))

#Ejercicio 3
#3.3
def es_nombre_largo (nombre:str)-> bool:
    res:bool = len (nombre) >= 3 and len (nombre) <= 8 
    return res
print (es_nombre_largo("papu"))

#Ejercicio 4

#Ejercicio 5
#5.1
def devolver_el_doble_si_es_par (n:int) -> bool:
    if (n%2==0):
        return (n*2)
    else:
        return (n)
    
#Ejercicio 6
#6.1
def pares ():
    i = 10
    while (i < 41):
        if (i%2 == 0):
            print (i)
            i= i + 1
        else: 
            i= i+1

pares()
#6.2
def cuenta_atras (n:int):
    while (n >=1):
        print (n)
        n = n-1
    print ("despegue")
cuenta_atras(5)

#9
def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print (es_primo(4))

    
