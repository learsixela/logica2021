# solicitar datos al usuario
# nombre, apellido, edad, sexo, estatura, peso, email
# validar el ingreso

edad = input("Ingrese edad: ")
if edad =="":
    print ("Error: Ingrese edad")
else:
    if edad >= "18":
        print ("Puede pasar")
    else:
        print("No puede pasar")