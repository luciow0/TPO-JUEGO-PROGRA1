import random
def parteDosJuego(listaProvincias, listaHabitantes, matriz): 
    costoElec31 = random.randint(20,30)
    costoElec32 = random.randint(0,5)

    print("Comienza a propagarse la enfermedad. Se requiere tomar acción rápidamente ¿Qué vas a hacer ahora? \n")
    print("OP1: Trabajo y Educación a distancia hasta nuevo aviso -> costo: $",costoElec31," millones \n")
    print("OP2: Emitir un comunicado para concientizar -> costo: $",costoElec32," millones \n")
    print("OP3: No hacer nada. -> costo $0\n\n Para la OP1 escribe '1', para la OP2 '2' y para la OP3 '3'\n")

    parteDos = True

    while parteDos:
        eleccion = int(input(" "))
        while eleccion != 1 and eleccion != 2 and eleccion != 3:
            eleccion = int(input("Por favor ingrese una eleccion valida (1, 2 o 3) "))
            
        if eleccion == 1:
            if presupuesto >= costoElec31:
                presupuesto -= costoElec31
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(10,15)
                    matriz[i][1] = habitantes - variacionCantHabs
                    matriz[i][1] = habitantes + variacionCantHabs                    
                parteDos = False

            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n")
                print("OP1: Cerrar fronteras -> costo: $",costoElec31," millones \n ")
                print("OP2: No hacer nada -> costo $",costoElec32,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")                  
                eleccion = int(input(" "))
                #poner while y resolver
                    
        elif eleccion == 2:
            print("Ups! Tu discurso no sirvió!\n")
            if presupuesto >= costoElec31:        
                presupuesto -= costoElec31
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i][1]
                    variacionCantHabs = habitantes / random.randint(20,30)
                    matriz[i][1] = habitantes + variacionCantHabs
                    matriz[i][0] = habitantes - variacionCantHabs   
                parteDos = False                 
                    
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n")
                print("OP1: Cerrar fronteras -> costo: $",costoElec31," millones \n")
                print("OP2: No hacer nada -> costo $",costoElec32,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                eleccion = int(input(" ")) 
                #poner while 

        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            if contNoHacerNada >= 2:
                descuento = random.randint(10,30)
                print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                presupuesto -= descuento
                presupuesto -= 10
                for i in range(len(listaProvincias)):
                    habitantes = listaHabitantes[i]
                    variacionCantHabs = habitantes / random.randint(15,25)
                    matriz[i][1] = habitantes + variacionCantHabs
                    matriz[i][0] = habitantes - variacionCantHabs
                parteDos = False
                    