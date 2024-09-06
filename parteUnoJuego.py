import random
def parteUnoJuego(listaProvincias, listaHabitantes,matriz): 
    costoElec21 = random.randint(5,10)
    costoElec22 = random.randint(10,15)

    print("ASÍ AVANZO (MOSTRAR MATRIZ O ALGO NO SÉ) ¿Qué vas a hacer ahora? \n")
    print("OP1: Implementación del barbijo -> costo: $",costoElec21," millones \n") 
    print("OP2: Suspender actividades no escenciales por 1 mes -> costo: $",costoElec22," millones \n")
    print("OP3: No hacer nada. Aún es muy pronto para tomar medidas -> costo $0\n\n ")
    print("Para la OP1 escribe '1', para la OP2 '2' y para la OP2 '3 \n")

    parteUno = True

    while parteUno:
        eleccion = int(input(" "))
        while eleccion != 1 and eleccion != 2 and eleccion != 3:
            eleccion = int(input("Por favor ingrese una eleccion valida (1, 2 o 3) "))
            
        if eleccion == 1:
            if presupuesto >= 15:
                presupuesto -= 5
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i][1]
                    VariacionCantHabs = habitantes / random.randint(10,15)
                    matriz[i][1] = habitantes - VariacionCantHabs
                    matriz[i][0] = habitantes + VariacionCantHabs   
                parteUno = False
                    
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec21," millones \n")
                print("OP2: No hacer nada -> costo $",costoElec22,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                eleccion = int(input(" "))
                #pegar while y ver como hacerlo 
                
        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1

            if contNoHacerNada >= 2:
                descuento = random.randint(10,15)
                print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                presupuesto -= descuento
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    VariacionCantHabs = habitantes / random.randint(20,25)
                    matriz[i][1] = habitantes + VariacionCantHabs
                    matriz[i][0] = habitantes - VariacionCantHabs
                parteUno = False