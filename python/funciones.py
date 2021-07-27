#funciones
#reutilizar codigo
#objetivo unico
#si la funcion no es llamada, esta no HACE NADA.

#sintaxis
#def nombre_de_la_funcion(argumento1,argumento2,argumento3):

def sumar(a,b):#definicion de funcion
    suma = a + b #operatoria
    print ("print en funcion: ",suma)#impresion
    return suma #retorno o devolucion de un valor

#llamada a la funcion
#nombre_de_la_funcion(argumento1,argumento2,argumento3)
respuesta = sumar(15,38)
print("print de respuesta: ",respuesta)

################################################

def restar(a, b):
    x = a - b
    return x

resta1 = restar(4,6) # resta1= -2
resta2 = restar(1,4) # resta2= -3
resta3 = resta1 + resta2 # resta3= -2 + -3 = -5
print(resta3) # -5
valor_final= sumar(resta1,resta2)
