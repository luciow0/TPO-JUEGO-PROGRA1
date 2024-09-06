import random

def inicioDelJuego(listaProvincias,listaHabitantes,matriz):
    costoElec11 = random.randint(10,20)
    costoElec12 = random.randint(5,10)
    iniciarJuego = True
    print("Comienza a propagarse la enfermedad. Se requiere tomar acción rápidamente ¿Qué vas a hacer ahora? \n")
    print("OP1: Cuarentena total de 20 días -> costo: $",costoElec11," millones \n")
    print("OP2: Suspender actividades no escenciales por 1 mes -> costo: $",costoElec12," millones \n") 
    print("OP3: No hacer nada. Aún es muy pronto para tomar medidas -> costo $0\n\n")
    print("Para la OP1 escribe '1', para la OP2 '2' y para la OP3 '3'\n")

    while iniciarJuego: 

        eleccion = int(input(" "))
        while eleccion != 1 and eleccion != 2 and eleccion != 3:
            eleccion = int(input("Por favor ingrese una eleccion valida (1, 2 o 3) "))

        if eleccion == 1:
            if presupuesto >= 20:
                presupuesto -= 20
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(10,15)
                    matriz[i][1] = habitantes - variacionCantHabs #es ampliamenteprobable que el manejo de la matriz sea erroneo
                    matriz[i][0] = habitantes + variacionCantHabs  
                iniciarJuego = False                  

            #solucionar problema entre decisiones y falta de dinero

            else: 
                print("No tienes presupuesto suficiente. Toma otra decisión: \n") 
                print("OP1: Cerrar fronteras -> costo: $",costoElec11," millones \n ")
                print("OP2: No hacer nada -> costo $",costoElec12,"\n\n") 
                print("Para la OP1 escribe '1' y para la OP2 '2'\n")
                eleccion = int(input(" "))
                #aca hay un problema
                while eleccion == 1 and eleccion != 2 and eleccion != 3: 
                    eleccion = int(input("Por favor ingrese una eleccion valida,  "))

        elif eleccion == 2:
            if presupuesto >= 15:
                presupuesto -= 15
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(5,10)
                    matriz[i][1] = habitantes - variacionCantHabs
                    matriz[i][0] = habitantes + variacionCantHabs   
                iniciarJuego = False
                    
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n")
                print("OP1: Cerrar fronteras -> costo: $",costoElec11," millones \n")
                print("OP2: No hacer nada -> costo $",costoElec12,"\n\n ")
                print("Para la OP1 escribe '1' y para la OP2 '2'\n")
                eleccion = int(input(" ")) #revisar while y eso
                while eleccion == 1 and eleccion != 2 and eleccion != 3: 
                    eleccion = int(input("Por favor ingrese una eleccion valida,  "))

        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            for i in range(len(listaProvincias)):
                habitantes = listaHabitantes[i]
                variacionCantHabs = habitantes / random.randint(20,25)
                matriz[i][1] = habitantes + variacionCantHabs
                matriz[i][0] = habitantes - variacionCantHabs
            iniciarJuego = False

