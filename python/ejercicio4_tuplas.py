#tuplas
#conjunto de datos, separados por coma, que no pueden ser modificados, todos parten en la posicion 0

tupla = (1234, 'aeiou', 0.19, 'qwerty')

#  nombre_tupla[posicion_elemento]
print (tupla[0]) #1234
print (tupla[1]) #"aeiou"
print (tupla[2]) #0.19
print (tupla[3]) #'qwerty'
print (tupla[1:3]) #("aeiou",0.19)  #[1,3[
print (tupla[:2]) # (1234,'aeiou')
print (tupla[2:]) # (0.19,'qwerty')

#listas
#conjunto de datos, separados por coma, ordenados segun su ingreso, todos parten en la posicion 0

lista = [1234, 'aeiou', 0.19, 'qwerty',True]

print(lista[2]) # 0.19
print(lista[4]) #
lista[0] = 4321 # reeemplazando en la posicion 0
#lista = [4321, 'aeiou', 0.19, 'qwerty',True]
print(lista[-1])# True recorrer de manera inversa
print(lista[1]) #'aeiou'

lista2 = lista[:] ## copia de datos
print(lista) # se mantiene [1234, 'aeiou', 0.19, 'qwerty',True]
print(lista2) # es copia de lista

lista2[1] = '12345678' #

print(lista) # [1234, 'aeiou', 0.19, 'qwerty',True]
print(lista2) # [1234, '12345678', 0.19, 'qwerty',True]

lista3 = lista ##
lista3[1] = '12345678' #

print(lista) # ? [1234, '12345678', 0.19, 'qwerty',True]
print(lista3) # [1234, '12345678', 0.19, 'qwerty',True]

print(lista)
