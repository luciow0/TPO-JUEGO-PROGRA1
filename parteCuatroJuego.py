import random
def parteCuatroJuego(listaProvincias, listaHabitantes, matriz): 
    costoElec51 = random.randint(5,15)
    costoElec52 = random.randint(20,30)
    print("ASÍ AVANZO (MOSTRAR MATRIZ O ALGO NO SÉ) ¿Qué vas a hacer ahora? \n")
    print("OP1: Cerrar fronteras -> costo: $",costoElec51," millones \n") 
    print("OP2: No hacer nada -> costo $",costoElec52,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
    parteCuatro = True
    while parteCuatro: 
        
        eleccion = int(input())
        while eleccion != 1 and eleccion != 2:
            eleccion = int(input("Por favor ingrese una eleccion valida (1, 2) "))
        
        if eleccion == 1:
            if presupuesto >= costoElec51:
                presupuesto -= costoElec51
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(5,15)
                    matriz[i][1] = habitantes - variacionCantHabs
                    matriz[i][0] = habitantes + variacionCantHabs    
                parteCuatro = False                
                
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec51," millones \n OP2: No hacer nada -> costo $",costoElec52,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                elec5 = int(input())
                                   
        else:
            if presupuesto >= costoElec51:
                presupuesto -= costoElec51
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i][1]
                    variacionCantHabs = habitantes / random.randint(15,25)
                    matriz[i][1] = habitantes - variacionCantHabs
                    matriz[i][0] = habitantes + variacionCantHabs 
                parteCuatro = False                   
                
            else:
                print("No tienes presupuesto suficiente. Perdiste el juego")
                parteCuatro = False
                # REVISAR ESTO ACA DIRECTAMENTE DEBERÍA SALIR DE LAS OPCIONES