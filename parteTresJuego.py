import random
def parteTresJuego(listaProvincias, listaHabitantes, matriz):
    costoElec41=random.randint(30,40)
    print("ASÍ AVANZO (MOSTRAR MATRIZ O ALGO NO SÉ) ¿Qué vas a hacer ahora? \n")
    print("OP1: Cerrar fronteras -> costo: $",costoElec41," millones \n") 
    print("OP2: No hacer nada -> costo $0\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
    parteTres = True

    while parteTres: 
        eleccion = int(input(" "))  
        while eleccion != 1 and eleccion != 2 and eleccion != 3:
            eleccion = int(input("Por favor ingrese una eleccion valida (1, 2 o 3) "))
        
        if eleccion == 1:
            if presupuesto >= costoElec41:
                presupuesto -= costoElec41
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(5,15)
                    matriz[i][1] = habitantes - variacionCantHabs
                    matriz[i][0] = habitantes + variacionCantHabs       
                parteTres = False             
                
            else:
                print("No tienes presupuesto suficiente\nNo te queda otra opción que no hacer nada\n")
                print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
                contNoHacerNada += 1
                if contNoHacerNada >= 2:
                    descuento = random.randint(10,15)
                    print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                    presupuesto -= descuento
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(15,25)
                    matriz[i][1] = habitantes + variacionCantHabs
                    matriz[i][0] = habitantes - variacionCantHabs
                      
        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            if contNoHacerNada >= 2:
                descuento = random.randint(10,15)
                print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                presupuesto -= descuento
            for i in range(len(listaProvincias)):
                habitantes = listaHabitantes[i]
                variacionCantHabs = habitantes / random.randint(15,25)
                matriz[i][1] = habitantes + variacionCantHabs
                matriz[i][0] = habitantes - variacionCantHabs