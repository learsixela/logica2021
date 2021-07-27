# 1.- Básico : imprime todos los enteros del 0 al 150.
for i in range(0,151):
    print (i)

# 2.- Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1000
for i in range(5,1001,5):
    print (i)
# 3.- Contar, Dojo Way - imprime enteros del 1 al 100. 
# Si es divisible por 5, imprima "Coding" en su lugar. 
# Si es divisible por 10, imprima "Coding Dojo".
for i in range (0,101):
    if i % 5 == 0:
        print (i,"Coding")
    elif i % 10 == 0:
        print (i,"Coding Dojo")
    else:
        print (i, "no cumple ninguna de las condiciones")
# 4.- ¡Uf, Eso es bastante grande!: 
# suma enteros impares de 0 a 500000 e imprime la suma final.

#for i in range (1,500001,2):
suma = 0 #variable acumuladora
for i in range (0,500001):
    if i % 2 != 0:#numeros impares, el resto de la division no es cero
        suma = suma + i # acumular suma de numeros impares
print (suma)
"""
0/2=0
0

4 / 2 = 2   
0
16/2 = 8
0

5 / 2 = 2
1

7/2= 3
1
"""
# 5.- Cuenta regresiva por cuatro : 
# imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for i in range (2018,-1,-4):
    print (i)#

# 6.- Contador flexible : 
# establece tres variables: 
# lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. 
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, 
# el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum=2
highNum=100
mult=7 
#for i in range (2,9+1):
for i in range (lowNum,highNum+1):
    if i % mult == 0:
        print (i, "multiplo de ",mult)

#multiplo de numero:
# 3*1=  3
# 3*2=  6
# 3*3=  9
# 3*4=  12
# 3*5=  15  

#3/3=1
#0

#7/3=2
#1