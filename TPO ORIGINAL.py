import random

p = ["CHUBUT", "SALTA", "JUJUY", "CATAMARCA", "TUCUMAN"]
e = ["S", "I", "M"]
ch=[]

for i in range(len(p)):
    ch.append([])   #añado filas
    for j in range(len(e)):
        ch[i].append(50)

# RANDOMIZAR COSTOS DE LAS DECISIONES Y PRESUPUESTO !!!


def desarrolloJuego(provincias,estados,cantHabitantes,presupuesto):
    contNoHacerNada = 0
    
    #Elección 1
    decision=0
    costoElec11 = random.randint(10,20)
    costoElec12 = random.randint(5,10)
    
    while decision==0:
        print(("Comienza a propagarse la enfermedad. Se requiere tomar acción rápidamente ¿Qué vas a hacer ahora? \n OP1: Cuarentena total de 20 días -> costo: $",costoElec11," millones \n OP2: Suspender actividades no escenciales por 1 mes -> costo: $",costoElec12," millones \n OP3: No hacer nada. Aún es muy pronto para tomar medidas -> costo $0\n\n Para la OP1 escribe '1', para la OP2 '2' y para la OP3 '3' NADA\n"))
        elec1 = int(input())
      
        """ACÁ DEBE HACERSE LA CONVERSIÓN A MAYUS --> OPERAR CON STRINGS"""
        
        if elec1 == 1:
            if presupuesto >= 20:
                decision=1
                presupuesto -= 20
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(10,15)
                    cantHabitantes[i][1] = habs-VariacionCantHabs
                    cantHabitantes[i][0] = habs+VariacionCantHabs                    
                
            else: #VER ESTO CAPAZ EN LA PRIMERA NUNCA SE QUEDA SIN
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec11," millones \n OP2: No hacer nada -> costo $",costoElec12,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                elec1 = int(input())
                #validar que no vuelva a elegir la opcion 1 

        elif elec1 == 2:
            if presupuesto >= 15:
                decision=1
                presupuesto -= 15
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(5,10)
                    cantHabitantes[i][1] = habs-VariacionCantHabs
                    cantHabitantes[i][0] = habs+VariacionCantHabs                    
                
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec11," millones \n OP2: No hacer nada -> costo $",costoElec12,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                elec1 = int(input())
        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            decision=1
            for i in range(len(provincias)):
                habs = cantHabitantes[i][1]
                VariacionCantHabs = habs/random.randint(20,25)
                cantHabitantes[i][1] = habs+VariacionCantHabs
                cantHabitantes[i][0] = habs-VariacionCantHabs
                
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Elección 2 (separado)
    decision2=0
    
    costoElec21 = random.randint(5,10)
    costoElec22 = random.randint(10,15)
    
    while decision2==0:
        print("ASÍ AVANZO (MOSTRAR MATRIZ O ALGO NO SÉ) ¿Qué vas a hacer ahora? \n OP1: Implementación del barbijo -> costo: $",costoElec21," millones \n OP2: Suspender actividades no escenciales por 1 mes -> costo: $",costoElec22," millones \n OP3: No hacer nada. Aún es muy pronto para tomar medidas -> costo $0\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
        elec2 = int(input())
      
        """VALIDAR QUE elec2 SEA 1 O 2"""
        """ACÁ DEBE HACERSE LA CONVERSIÓN A MAYUS --> OPERAR CON STRINGS"""
        
        if elec2 == 1:
            if presupuesto >= 15:
                decision2=1
                presupuesto -= 5
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(10,15)
                    cantHabitantes[i][1] = habs-VariacionCantHabs
                    cantHabitantes[i][0] = habs+VariacionCantHabs                    
                
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec21," millones \n OP2: No hacer nada -> costo $",costoElec22,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                elec2=int(input())
        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            if contNoHacerNada >= 2:
                descuento = random.randint(10,15)
                print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                presupuesto -= descuento
            decision2=1
            for i in range(len(provincias)):
                habs = cantHabitantes[i][1]
                VariacionCantHabs = habs/random.randint(20,25)
                cantHabitantes[i][1] = habs+VariacionCantHabs
                cantHabitantes[i][0] = habs-VariacionCantHabs
                
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Elección 3 (hecho)
    decision3=0
      
    while decision3==0:
        costoElec31 = random.randint(20,30)
        costoElec32 = random.randint(0,5)
        print("Comienza a propagarse la enfermedad. Se requiere tomar acción rápidamente ¿Qué vas a hacer ahora? \n OP1: Trabajo y Educación a distancia hasta nuevo aviso -> costo: $",costoElec31," millones \n OP2: Emitir un comunicado para concientizar -> costo: $",costoElec32," millones \n OP3: No hacer nada. -> costo $0\n\n Para la OP1 escribe '1', para la OP2 '2' y para la OP3 '3'\n")
        elec3 = int(input())
        """VALIDAR QUE elec3 SEA 1,2,3"""
        
        if elec3 == 1:
            if presupuesto >= costoElec31:
                decision3=1
                presupuesto -= costoElec31
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(10,15)
                    cantHabitantes[i][1] = habs-VariacionCantHabs
                    cantHabitantes[i][0] = habs+VariacionCantHabs                    
                
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec31," millones \n OP2: No hacer nada -> costo $",costoElec32,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")                  
                elec3 = int(input())
                
        elif elec3 == 2:
            print("Ups! Tu discurso no sirvió!\n")
            if presupuesto >= costoElec31:
                decision3=1
                presupuesto -= costoElec31
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(20,30)
                    cantHabitantes[i][1] = habs+VariacionCantHabs
                    cantHabitantes[i][0] = habs-VariacionCantHabs                    
                
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec31," millones \n OP2: No hacer nada -> costo $",costoElec32,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                elec3 = int(input()) 
        else:
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            if contNoHacerNada >= 2:
                descuento = random.randint(10,30)
                print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                presupuesto -= descuento
                
            decision3=1
            presupuesto -= 10
            for i in range(len(provincias)):
                habs = cantHabitantes[i][1]
                VariacionCantHabs = habs/random.randint(15,25)
                cantHabitantes[i][1] = habs+VariacionCantHabs
                cantHabitantes[i][0] = habs-VariacionCantHabs
                

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Elección 4 (hecho)
    costoElec41=random.randint(30,40)
    print("ASÍ AVANZO (MOSTRAR MATRIZ O ALGO NO SÉ) ¿Qué vas a hacer ahora? \n OP1: Cerrar fronteras -> costo: $",costoElec41," millones \n OP2: No hacer nada -> costo $0\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
    elec4 = int(input())  
    """VALIDAR QUE elec4 SEA 1 O 2"""
    
    if elec4 == 1:
        if presupuesto >= costoElec41:
            presupuesto -= costoElec41
            for i in range(len(provincias)):
                habs = cantHabitantes[i][1]
                VariacionCantHabs = habs/random.randint(5,15)
                cantHabitantes[i][1] = habs-VariacionCantHabs
                cantHabitantes[i][0] = habs+VariacionCantHabs                    
            
        else:
            print("No tienes presupuesto suficiente\nNo te queda otra opción que no hacer nada\n")
            print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
            contNoHacerNada += 1
            if contNoHacerNada >= 2:
                descuento = random.randint(10,15)
                print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
                presupuesto -= descuento
            for i in range(len(provincias)):
                habs = cantHabitantes[i][1]
                VariacionCantHabs = habs/random.randint(15,25)
                cantHabitantes[i][1] = habs+VariacionCantHabs
                cantHabitantes[i][0] = habs-VariacionCantHabs
                
    else:
        print("ESTÁS ACABANDO CON EL SISTEMA DE SALUD! SI NO CAMBIAS DE ACTITUD ACABARÁS CON LOS MÉDICOS DE TODO EL PAIS!!\n")
        contNoHacerNada += 1
        if contNoHacerNada >= 2:
            descuento = random.randint(10,15)
            print("ESTAS EXPLOTANDO EL SISTEMA DE SALUD. Esto generó una perdida. Ahora te fueron descontados $",descuento," del presupuesto\n")
            presupuesto -= descuento
        for i in range(len(provincias)):
            habs = cantHabitantes[i][1]
            VariacionCantHabs = habs/random.randint(15,25)
            cantHabitantes[i][1] = habs+VariacionCantHabs
            cantHabitantes[i][0] = habs-VariacionCantHabs
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Elección 5 (he)
    decision5=0
      
    while decision5==0:
        costoElec51=random.randint(5,15)
        costoElec52=random.randint(20,30)
        print("ASÍ AVANZO (MOSTRAR MATRIZ O ALGO NO SÉ) ¿Qué vas a hacer ahora? \n OP1: Cerrar fronteras -> costo: $",costoElec51," millones \n OP2: No hacer nada -> costo $",costoElec52,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
        elec5 = int(input())
        """VALIDAR QUE elec4 SEA 1 O 2"""
        
        if elec5 == 1:
            if presupuesto >= costoElec51:
                decision5=1
                presupuesto -= costoElec51
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(5,15)
                    cantHabitantes[i][1] = habs-VariacionCantHabs
                    cantHabitantes[i][0] = habs+VariacionCantHabs                    
                
            else:
                print("No tienes presupuesto suficiente. Toma otra decisión: \n OP1: Cerrar fronteras -> costo: $",costoElec51," millones \n OP2: No hacer nada -> costo $",costoElec52,"\n\n Para la OP1 escribe '1' y para la OP2 '2'\n")
                elec5 = int(input())
                                   
        else:
            if presupuesto >= costoElec51:
                decision5=1
                presupuesto -= costoElec51
                for i in range(len(provincias)):
                    habs = cantHabitantes[i][1]
                    VariacionCantHabs = habs/random.randint(15,25)
                    cantHabitantes[i][1] = habs-VariacionCantHabs
                    cantHabitantes[i][0] = habs+VariacionCantHabs                    
                
            else:
                print("No tienes presupuesto suficiente. Perdiste el juego")
                # REVISAR ESTO ACA DIRECTAMENTE DEBERÍA SALIR DE LAS OPCIONES
                                
desarrolloJuego(p,e,ch,50)