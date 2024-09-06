import random

# Declaracion del menu inicial.

def menuInicial():
    print("Bienvenido al simulador de epidemia.\n")
    opcion = int(input("Seleccione una opcion:\n (1)-INICIAR\n (2)-SALIR\n"))
    while opcion < 1 or opcion > 2:
        opcion = int(input("Por favor seleccione una opción correcta:\n (1)-INICIAR\n (2)-SALIR\n"))
    return opcion

def llamarLogin():

    if login() == 1:
        iniciar = menuInicial()
        if iniciar == 1:
            print("Estas en el simulador de epidemia, tu objetivo es contrarrestar el avance de infectados en Argentina, para eso, debes tomar decisiones en base a tu presupuesto y su consecuencia. ¡Éxitos!\n")
            print("Tu estado inicial de las provincias es el siguiente:\n")
            # INSERTAR MATRIZ DE SANOS,INFECTADOS,MUERTOS INICIAL
            print(f"Tu sueldo inicial es el siguiente: {'PRESUPUESTO_INICIAL'}")

        else:
            print("\n¡Gracias por jugar al simulador de epidemia!")

def login():
    listaUsuarios = ["usuario", "usuario2","usuario3"]
    listaContraseñas = ["contraseña", "1234", "hola1234"]
    userFound = 0
    while userFound  == 0:
        user = input("Ingrese un usuario: ")
        userLower = user.lower()
        if userLower in listaUsuarios:
            userFound = 1
            posIndexU = listaUsuarios.index(userLower)
            
    if userFound == 1:
        passFound = 0
        while passFound == 0:
            password = input("Ingrese la contraseña: ")
            passLower = password.lower()
            if passLower in listaContraseñas:
                posIndexP = listaContraseñas.index(passLower)
                if posIndexU == posIndexP:
                    passFound = 1
                    ingreso = 1
    return ingreso

    

