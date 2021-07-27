# JAVASCRIPT
#  for (var i = 0; i < 5; i++) {
#    
# }0.1.2.3.4

#FOR para Rangos
for i in range(0,5): #[0,1,2,3,4]
    print (i)
# 
for i in range(0,10,2):
    print (i)#0,2,4,6,8

for i in range(1,10,2):
    print (i)#1,3,5,7,9

#FOR para Listas
vocales = ['a','e','i','o','u']
len(vocales)# len() tamaño o cantidad de elementos de la lista

#accedemos a los elementos de la lista por su indice o posicion (i)
for i in range(0,len(vocales)):
    print (i, vocales[i])#0, "a"

#for de objeto
#accedemos a los elementos de la lista
for elemento in vocales:
    print (elemento)

alumno = {"nombre": "Cristian", "edad": 25, "curso": "python"}
for key in alumno:
    print (key)#nombre, edad, curso
    print (alumno[key])#Cristian, 25, python
    print (key, alumno[key])#

for key, elemento in alumno.items():
    print(key," = " ,elemento)
