import random

# la siguiente funcion, toma como argumentos la lista de provincias, la lista de habitanbtes y la matriz
# da una imagen de la situacion actual del pais, con datos como: los habitantes, sanos, infectados y muertos de cada provincia, corresponidentemente
# no posee valores de retorno ya que solo se encarga de mostrar datos por pantalla 
# Funcion para imprimir Matriz
def mostrarMatriz(listaProvincias, listaHabitantes, matriz): 
    print("------------------------------------------------------------------------------------------")
    print("\t\t\tESTADO INICIAL DE LAS PROVINCIAS")
    print("------------------------------------------------------------------------------------------")
    print(f"{'PROVINCIA':<20}{'HABITANTES':>12}\t{'SANOS':>12}\t{'INFECTADOS':>12}\t{'MUERTOS':>12}")

    for i in range(len(listaProvincias)):
        print(f"{listaProvincias[i]:<20}{listaHabitantes[i]:>12}\t{matriz[i][0]:>12}\t{matriz[i][1]:>12}\t{matriz[i][2]:>12}")



# la siguiente funcion inicializa la lista de provincias y de forma random, dos listas que trabajaran de manera paralela con esta
# la lista de la cantidad de habitantes por provincia y la de infectados (iniciales) por provincia. A partir de estas podrá definirse la cantidad de sanos/infectados en la matriz
# las 3 listas son retornadas 
# Funcion para inicializar listas
def inicializarListas():
    listaProvincias = ['Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Cordoba', 'Corrientes', 'Entre Rios', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquen', 'Rio Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucuman']
    listaHabitantes = [random.randint(1000000, 1500000) for _ in range(23)]
    infectados = [random.randint(100000, 550000) for _ in range(23)]

    return listaProvincias, listaHabitantes, infectados



# la siguiente funcion, recibe como parametros la lista de habitantes e infectados
# se inicializa la matriz por comprension, asignando solamente ceros para luego ser remplazados
# se asumen un numero definido de columnas y filas y se recorre la matriz asignando los valores de 
# sanos en la columna 0, infectados en la 1
# se omite agregar muertos, ya que esta columna esta preinicilizada en 0 y al comienzo del juego asi sera
# la funcion retorna la matriz
# Funcion para inicializar matriz
def inicializarMatriz(listaHabitantes,infectados): 
    filas = 23
    columnas	 = 3
    matriz = [[0] * columnas for i in range(filas)] 
    for f in range(filas):
        matriz[f][0] = (listaHabitantes[f] - infectados[f]) #sanos 
        matriz[f][1] = infectados[f] #infectados 

    return matriz



# la siguiente funcion, recibe como parametros, la matriz y la variacion que se le dara a la cantidad de habitantes
# de manera positiva ya que sera invocada cuando el usuario tome "una buena decisión"
# verifica que la cantidad de (sanos + la variacion) no sea mayor al total de habitantes y que (infectados - la variacion) sea mayor a 0
# de ser asi, suma y resta las cantidades correspondientes, en caso contrario, la cantidad de sanos se establece en el limite (cantidad de habitantes) y los infectados en 0 
# se actualiza y se retorna la matriz 
# Funcion de alteraciones positivas de infectados/sanos.
def alteracionPositivaMatriz (matriz, variacionCantHabs):
    for i in range(0,23):

        totalHabitantes = matriz[i][0] + matriz[i][1]  # Total de habitantes en la provincia
        sanos = matriz[i][0]
        infectados = matriz[i][1]
        
        # Ajustar sanos e infectados con límite de totalHabitantes
        if sanos + variacionCantHabs <= totalHabitantes and infectados - variacionCantHabs >= 0:
            sanos += variacionCantHabs
            infectados -= variacionCantHabs
        else:
            sanos = totalHabitantes
            infectados = 0

        # Asignamos nuevamente los valores a la matriz
        matriz[i][0] = sanos  # SANOS
        matriz[i][1] = infectados  # INFECTADOS
        
    return matriz



# la siguiente funcion recibe como parametros, la matriz y la variacion que se le dara a la cantidad de habitantes
# de manera negativa, ya que sera invocada cuando el usuario tome "una mala decision"
# verifica que la cantidad de (infectados + la variacion) no sea mayor al total de habitantes y que (sanos - la variacion) sea mayor a 0
# de ser asi, suma las cantidades correspondientes, en caso contrario, la cantidad de infectados se establece en en el total de habitantes 
# y la de sanos en 0 
# se actualiza y se retorna la matriz
# Funcion de alteraciones negativas de infectados/sanos.
def alteracionNegativaMatriz (matriz, variacionCantHabs):
    for i in range(0,23):

        totalHabitantes = matriz[i][0] + matriz[i][1]  # Total de habitantes en la provincia
        sanos = matriz[i][0]
        infectados = matriz[i][1]
        
        # Ajustar sanos e infectados con límite de totalHabitantes
        if infectados + variacionCantHabs <= totalHabitantes and sanos - variacionCantHabs >= 0:
            infectados += variacionCantHabs
            sanos -= variacionCantHabs
        else:
            infectados = totalHabitantes
            sanos = 0

        # Asignamos nuevamente los valores a la matriz
        matriz[i][0] = sanos  # SANOS
        matriz[i][1] = infectados  # INFECTADOS
        
        return matriz



# la siguiente funcion, no recibe parametros, despliega un menu inicial simple, para que el jugador elija si desea jugar o no, retorna la decision del usuario 
# Declaracion del menu inicial.
def menuInicial():
    print("Bienvenido al menú principal:")
    opcion = int(input("Seleccione una opcion:\n (1) - Iniciar Juego\n (2) - Salir\n"))
    while opcion != 1 and opcion != 2:
        opcion = int(input("Por favor seleccione una opción correcta:\n (1) - Iniciar Juego\n (2) - Salir\n"))
    return opcion



# la siguiente funcion, no recibe parametros, invoca a la fucion de login y si esta retorna 1 (si el usuario pudo acceder con usuario y contraseña)
# entonces invoca la funcion que despliega el menu de inicio
# Declaracion del login.
def llamarLogin():
    log = 0
    if login() == 1:
        iniciar = menuInicial()
        if iniciar == 1:
            print("\nBienvenido al simulador de epidemia: \nA lo largo del juego deberas ir tomando decisiones para mitigar la propagación de la enfermedad, minimizar el número de muertes y gestionar el presupuesto del estado para frenar el contagio y/o desarrollar curas \nCada decisión que tomes tendrá implicaciones financieras y efectos sobre el estado de la población \nBuena suerte!!")
            log = 1
        else:
            print("\nPartida cancelada")
    return log
            
            

# la siguiente funcion, no recibe parametros, inicializa dos listas, una con posibles usuarios y otra con contraseñas para iniciar sesion en el juego
# se utiliza una bandera booleana para determinar si el usuario ingresa un nombre de usuario valido, en caso de ser asi solicita contraseña
# y de manera similar, utiliza una bandera booleana para determinar si el usuario ingreso correctamente la contraseña y verifica que sea correspondiente al usuario ingresado
# en caso de ser ambas afirmativas, coloca a la variable 'ingreso' en 1 y se retorna, es la que se utilizara luego para seguir con el resto del juego
def login():
    listaUsuarios = ["usuario", "usuario2","usuario3","1"]
    listaContraseñas = ["contraseña", "1234", "hola1234","1"]
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



# la siguiente funcion, se utilizara para validar las elecciones del usuario durante el desarrollo del juego
# recibe un minimo y un maximo, correspondientes a los numeros que los usuarios podran utilizar para tomar las elecciones
def validacion(min,max):
    eleccion = int(input(""))
    while eleccion < min or eleccion > max:
        eleccion = int(input("Por favor ingrese una opcion valida:\n"))
    
    return eleccion



# la siguiente funcion, da inicio al juego.
# recibe como parametros la lista de provincias y de habitantes para invocar a la funcion mostrarmatriz 
# y la matriz para invocar a la funciones de alternacion
# se inicializan de manera random, el presupuesto inicial del jugador, el costo de las primeras elecciones y una bandera booleana (iniciarJuego)
# que se utiliza para salir del bucle de la primera ronda y avanzar con la siguiente
# retorna la matriz y el presupuesto que seran utilizados por las funciones siguientes del desarrollo del juego 
# Funcion de inicio del juego (ronda 1)
def inicioDelJuego(listaProvincias,listaHabitantes,matriz):
    costoElec11 = random.randint(10,20)
    costoElec12 = random.randint(5,10)
    presupuesto = random.randint(30,50)

    iniciarJuego = True

    print("\nTu estado inicial de las provincias es el siguiente:\n")
    mostrarMatriz(listaProvincias,listaHabitantes,matriz)
    print(f"\nTu presupuesto inicial es el siguiente: $ {presupuesto} millones\n")
    print("Comienza a propagarse la enfermedad. Se requiere tomar acciones rápidamente ¿Qué opcion vas a elegir?: \n")  
    print(" --> OP1: Cuarentena total de 20 días -> costo: $",costoElec11," millones \n")
    print(" --> OP2: Suspender actividades no escenciales por 1 mes -> costo: $",costoElec12," millones \n")
    print(" --> OP3: No hacer nada. Aún es muy pronto para tomar medidas -> costo $0")
    print("\nPara la OP1 escribe '1', para la OP2 '2' y para la OP3 '3'\n")

    while iniciarJuego: 

        eleccion = validacion(1,3)
        
        if eleccion == 1 and presupuesto >= costoElec11:
            presupuesto -= costoElec11
            print("\nElegiste la opcion de cuarentena total por 20 dias. \n¿Funcionará esta decision? \nContinuemos con la siguiente ronda para comprobarlo.")
            variacionCantHabs = random.randint(10000, 15000) 
            matriz = alteracionPositivaMatriz(matriz, variacionCantHabs)
            iniciarJuego = False
            

        elif eleccion == 2 and presupuesto >= costoElec12:
            presupuesto -= costoElec12
            print("\nElegiste la opcion de suspender actividades no escenciales por 1 mes. \n¿Funcionará esta decision? \nContinuemos con la siguiente ronda para comprobarlo.")
            variacionCantHabs = random.randint(20000, 25000)
            matriz = alteracionPositivaMatriz(matriz, variacionCantHabs)
            iniciarJuego = False

        else:
            print("\nMala idea! Aumentaron los contagios...")
            variacionCantHabs = random.randint(30000, 35000)
            matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            iniciarJuego = False

    return matriz, presupuesto



# la siguiente funcion recibe como parametros, la lista de provincias y habitantes, la matriz y el presupuesto de la ronda anterior 
# de igual manera se inicializa una variable random como el costo de la eleccion que se le presentara al usuario y se cumple el mecanismo de la funcion anterior
# a diferencia de la ronda anterior, apartir de aqui los infectados pueden morir, la enfermedad se lleva a la mitad de infectados que haya al momento de la ejecucion 
# la condicion de cantidad de infectados para que la enfermedad sea mortal ira disminuyendo ronda a ronda
# apartir de este momento, las funciones de las rondas son similares entre si en su estructura logica, lo que va a variar seran las decisiones que se le presentaran al usuario y su costo
# Funcion de ronda 2
def parteUnoJuego(listaProvincias,listaHabitantes,matriz,presupuesto):
    costoElec21 = random.randint(5,10)

    print("\nTu estado actual de las provincias es el siguiente:\n")
    mostrarMatriz(listaProvincias,listaHabitantes,matriz)
    print(f"\nTu presupuesto es: $ {presupuesto} millones\n")
    print(" --> OP1: Implementación del barbijo -> costo: $",costoElec21," millones \n") 
    print(" --> OP2: No hacer nada. Aún es muy pronto para tomar medidas -> costo $0 ")
    print("\nPara la OP1 escribe '1' y para la OP2 '2'\n")

    parteUno = True

    while parteUno:
        eleccion = validacion(1,2)

        if eleccion == 1 and presupuesto >= costoElec21:
            print("\nElegiste la opcion de implementar barbijos. \n¿Funcionará esta decision? \nContinuemos con la siguiente ronda para comprobarlo.")  
            presupuesto -= costoElec21
            variacionCantHabs = random.randint(10000, 15000)
            matriz = alteracionPositivaMatriz(matriz,variacionCantHabs)
            parteUno = False
            
        elif eleccion == 1 and presupuesto <= costoElec21:
            print("\nNo tienes presupuesto suficiente. Por defecto, se eligió la opción de no hacer nada, lo cual te perjudica negativamente en los estados de los habitantes. \nContinuemos con la seguiente ronda.")  
            variacionCantHabs = random.randint(15000, 20000)
            matriz = alteracionNegativaMatriz(matriz,variacionCantHabs)
            parteUno = False

        else:
            print("\nProcura no elegir muchas veces esta opcion ya que no te beneficiara a lo largo del juego. \n")  
            variacionCantHabs = random.randint(15000, 20000)
            matriz = alteracionNegativaMatriz(matriz,variacionCantHabs)
            parteUno = False
                
    # En esta ronda el numero de infectados debe ser mayor a 20000
    for i in range(len(listaProvincias)):
        infectados = matriz[i][1]
        if infectados > 20000:
            muertos = infectados // 2  
            matriz[i][1] -= muertos 
            matriz[i][2] += muertos

    return matriz,presupuesto



# Funcion de ronda 3
def parteDosJuego(listaProvincias,listaHabitantes,matriz,presupuesto): 
    costoElec31 = random.randint(15,30)
    costoElec32 = random.randint(1,5)
    
    print("Tu estado actual de las provincias es el siguiente:\n")
    mostrarMatriz(listaProvincias,listaHabitantes,matriz)
    print(f"\nTu presupuesto es: $ {presupuesto} millones\n")
    print(" --> OP1: Trabajo y Educación a distancia hasta nuevo aviso -> costo: $",costoElec31," millones \n")
    print(" --> OP2: Emitir un comunicado para concientizar -> costo: $",costoElec32," millones \n")
    print(" --> OP3: No hacer nada. -> costo $0")
    print("\nPara la OP1 escribe '1', para la OP2 '2' y para la OP2 '3 \n")

    parteDos = True

    while parteDos:
        eleccion = validacion(1,3)
        
        if eleccion == 1 and presupuesto >= costoElec31:
            print("\nElegiste la opcion de trabajo y educacion a distancia hasta nuevo aviso. \n¿Funcionará esta decision? \nContinuemos con la siguiente ronda para comprobarlo.")
            presupuesto -= costoElec31
            variacionCantHabs = random.randint(10000, 15000)
            matriz = alteracionPositivaMatriz(matriz,variacionCantHabs)
            parteDos = False
            
        elif eleccion == 1 and presupuesto <= costoElec31:            
            print("\nNo tienes presupuesto suficiente. Por defecto, se eligió la opción de no hacer nada, lo cual te perjudica negativamente en los estados de los habitantes. \nContinuemos con la seguiente ronda.")  
            variacionCantHabs = random.randint(15000, 20000)
            matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            parteDos = False
            

        elif eleccion == 2 and presupuesto >= costoElec32:    
            print("\nElegiste la opcion de emitir un comunicado para cocientizar. \n¿Funcionará esta decision? \nContinuemos con la siguiente ronda para comprobarlo.\n")   
            presupuesto -= costoElec32
            variacionCantHabs = random.randint(7000, 10000)
            matriz = alteracionNegativaMatriz(matriz,variacionCantHabs)
            parteDos = False
        
        elif eleccion == 2 and presupuesto <= costoElec31:            
            print("\nNo tienes presupuesto suficiente. Por defecto, se eligió la opción de no hacer nada, lo cual te perjudica negativamente en los estados de los habitantes. \nContinuemos con la seguiente ronda.")  
            variacionCantHabs = random.randint(15000, 20000)
            matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            parteDos = False
           

        else:
            print("\nProcura no elegir muchas veces esta opcion ya que no te beneficiara a lo largo del juego. \nContinuemos con la siguiente ronda.")
            variacionCantHabs = random.randint(15000, 20000)
            matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            parteDos = False

    # En esta ronda el numero de infectados debe ser mayor a 15000
    for i in range(len(listaProvincias)):
        infectados = matriz[i][1]
        if infectados > 15000:
            muertos = infectados // 2  
            matriz[i][1] -= muertos 
            matriz[i][2] += muertos

    return matriz,presupuesto



# Funcion de ronda 4
def parteTresJuego(listaProvincias,listaHabitantes,matriz,presupuesto):
    costoElec41=random.randint(10,25)

    print("Tu estado actual de las provincias es el siguiente:\n")
    mostrarMatriz(listaProvincias,listaHabitantes,matriz)
    print(f"\nTu presupuesto es: $ {presupuesto} millones\n")
    print(" --> OP1: Cerrar fronteras -> costo: $",costoElec41," millones \n") 
    print(" --> OP2: No hacer nada -> costo $0")
    print("\nPara la OP1 escribe '1' y para la OP2 '2'\n")
    parteTres = True

    while parteTres: 
        eleccion = validacion(1,2)
        if eleccion == 1 and presupuesto >= costoElec41:
            presupuesto -= costoElec41
            variacionCantHabs = random.randint(10000, 15000)
            impacto = random.randint(0,1)
            if impacto == 1:
                print("\nElegiste la opcion de cerrar fronteras. \n¿Funcionará esta decision? \nContinuemos para comprobarlo.\n")
                matriz = alteracionPositivaMatriz(matriz, variacionCantHabs)
            else:
                print("\nElegiste la opcion de cerrar fronteras. \n¿Funcionará esta decision? \nContinuemos para comprobarlo.\n")
                matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            parteTres = False
        
        elif eleccion == 1 and presupuesto <= costoElec41:
            print("\nNo tienes presupuesto suficiente. Por defecto, se eligió la opción de no hacer nada, lo cual te perjudica negativamente en los estados de los habitantes. \n")  
            variacionCantHabs = random.randint(15000, 25000)
            matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            parteTres = False

        else:
            print("\nDecidiste no hacer nada! Te estas quedando sin recursos... \n")
            variacionCantHabs = random.randint(15000, 25000)
            matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
            parteTres = False

    # En esta ronda el numero de infectados debe ser mayor a 10000
    for i in range(len(listaProvincias)):
        infectados = matriz[i][1]
        if infectados > 10000:
            muertos = infectados // 2  
            matriz[i][1] -= muertos 
            matriz[i][2] += muertos
            
    return matriz,presupuesto


# Esta es la funcion final de el desarrollo del juego, se inicializa una nueva variable booleana llamada 'gano' 
# que se utilizara para determinar si el usuario alcanzo con su presupuesto para salvar a la humanidad, esta variable sera retornada ya que sera utilizada 
# por la funcion finJuego mas adelante para verificar si la cantidad de personas que se salvaron es mayor al total de habitantes, ya que 
# por mas que el usuario haya llegado con presupuesto a la ronda final, puede perder en caso de tener mas muertos que vivos 
# Funcion de ronda 5
def parteCuatroJuego(listaProvincias,listaHabitantes,matriz,presupuesto):
    gano = True
    costoElec51 = random.randint(15,30)
    costoElec52 = random.randint(3,7)
    parteCuatro = True
    while parteCuatro: 
        if presupuesto > costoElec52:
            print("\nTu estado actual de las provincias es el siguiente:\n")
            mostrarMatriz(listaProvincias,listaHabitantes,matriz)
            print(f"\nTu presupuesto es: $ {presupuesto} millones\n")
            print(f"\nEstas llegando al final del juego. Es tu ultima oportunidad para intentar salvar a la población. ¿Qué opcion vas a elegir?: ")  
            print(" --> OP1: Vacuna a los habitantes -> costo: $",costoElec51," millones \n") 
            print(" --> OP2: Desarrolla un medicamento -> costo $",costoElec52," millones ")
            print("\nPara la OP1 escribe '1' y para la OP2 '2'\n")
            
            
            eleccion = validacion(1,2)
            
            if eleccion == 1 and presupuesto >= costoElec51:
                presupuesto -= costoElec51
                print("\nElegiste la opcion de vacunar a los habitantes ¿Funcionará esta decision? Continuemos para comprobarlo...\n")
                variacionCantHabs = random.randint(10000, 15000)
                matriz = alteracionPositivaMatriz(matriz, variacionCantHabs)
                parteCuatro = False
                
            elif eleccion == 1 and presupuesto >= costoElec52:
                presupuesto -= costoElec51
                print("\nElegiste la opcion de vacunar a los habitantes pero no tienes presupuesto. No te quedará otra que probar suerte con el medicamento...\n")
                presupuesto -= costoElec52
                impacto = random.randint(0,1)
                variacionCantHabs = random.randint(20000, 25000)
                if impacto == 1:
                    print("Tuviste suerte! Se pudo desarrollar un medicamento óptimo")
                    matriz = alteracionPositivaMatriz(matriz, variacionCantHabs)
                    parteCuatro = False
                else:
                    print("Mala Suerte. \n No se consiguió desarrollar el medicamento! Habrás podido ganar igual? \n...")
                    matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
                    parteCuatro = False 

            else:
                presupuesto -= costoElec52
                impacto = random.randint(0,1)
                variacionCantHabs = random.randint(20000, 25000)
                if impacto == 1:
                    print("\nBuena decision! Se pudo desarrollar un medicamento óptimo")
                    matriz = alteracionPositivaMatriz(matriz, variacionCantHabs)
                    parteCuatro = False
                else:
                    print("\nMala Suerte. No se consiguió desarrollar el medicamento! Habrás podido ganar igual? \n...")
                    matriz = alteracionNegativaMatriz(matriz, variacionCantHabs)
                    parteCuatro = False
        
        else:
            print("\nLo lamento, te quedaste sin presupuesto suficiente. Perdiste el juego!")
            gano = False
            parteCuatro = False
            
    # En esta ronda el numero de infectados debe ser mayor a 5000
    for i in range(len(listaProvincias)):
        infectados = matriz[i][1]
        if infectados > 5000:
            muertos = infectados // 2  
            matriz[i][1] -= muertos 
            matriz[i][2] += muertos
            
    return matriz,presupuesto,gano



# Funcion que informa el porcentaje de muertos totales en ARG
# recibe como parametros la lista de habitantes y la matriz  
def porcentajeMuertosTotal(listaHabitantes, matriz):
    contadorTotalMuertos = 0
    totalHabitantes = sum(listaHabitantes)
    for i in range (len(listaHabitantes)):
        contadorTotalMuertos += matriz[i][2]
  
    porcentajeTotalMuertos = contadorTotalMuertos / totalHabitantes * 100
    print(f"El porcentaje total de los muertos de todo el pais es de {porcentajeTotalMuertos} % \n")



# Funcion que informa la provincia con mayor porcentaje de muertos 
def porcentajeMayorMuertosporProvincia(listaProvincias,listaHabitantes,matriz):
    listaPorcMuertos = []
    repetidos = 0
    listaProvinciasPorcMayor =[]
    for i in range(len(listaProvincias)):
        porcPorProvincia = (matriz[i][2] / listaHabitantes[i]) * 100
        listaPorcMuertos.append(porcPorProvincia)

    maximoPorcMuertos = max(listaPorcMuertos)
    repetidos = listaPorcMuertos.count(maximoPorcMuertos)
    for i in range(len(listaPorcMuertos)):
        if listaPorcMuertos[i] == maximoPorcMuertos:
            listaProvinciasPorcMayor.append(listaProvincias[i])
    if( repetidos >= 2):
        print(f"Las provincias {listaProvincias} son las que tienen el mayor porcentaje de muertes el cual es:  {maximoPorcMuertos} % \n")
    else:
        print(f"La provincia {listaProvinciasPorcMayor[0]} tiene el mayor porcentaje de muertes el cual es: {maximoPorcMuertos} %\n")



# Funcion que informa el porcentaje de las provincias con mayor infectados
def porcentajeMayorInfectadosPorProvincia(matriz, listaProvincias):
    listaPorcInfectados = []
    listaProvinciasPorc = []
    
    for i in range(len(listaProvincias)):
        total = matriz[i][0] + matriz[i][1]  
        porcentaje = (matriz[i][1] / total) * 100  
        listaPorcInfectados.append(porcentaje)

    maximoPorcInfectados = max(listaPorcInfectados)
    repetidos = listaPorcInfectados.count(maximoPorcInfectados)
    for i in range(len(listaPorcInfectados)):
        if listaPorcInfectados[i] == maximoPorcInfectados:
            listaProvinciasPorc.append(listaProvincias[i])
    if repetidos >= 2:
        print(f"Las provincias {listaProvinciasPorc} son las que tienen el mayor porcentaje de infectados el cual es: {maximoPorcInfectados:} % \n")
    else:
        print(f"La provincia {listaProvinciasPorc[0]} es la que tiene el mayor porcentaje de infectados el cual es: {maximoPorcInfectados:} % \n")



# La siguiente funcion lambda funciona como un filtro adicional de dificultad para el juego 
# sera utilizada para enviarle la variable 'conVirus' que incluye a los habitantes muertos e infectados variable calculada en la funcion finJuego
# par que el usuario pueda ganar, debe tener mas habitantes sanos que muertos e infectados * 3.5
calculoParaFinDelJuego = lambda cVirus : cVirus*3.5


# Funcion finJuego, calcula los ciudadanos que resultaron sanos entre toda la poblacion y aquellos infectados y muertos
# realiza el llamado a la funcion calculoParaFinDelJuego e informa si el jugador gano, o perdio
def finJuego(listaHabitantes, matriz, gano):
    totalSanos = 0
    totales = 0
    for i in range(len(listaHabitantes)):
        totalSanos += matriz[i][0]
        totales += listaHabitantes[i]
    
    conVirus = totales - totalSanos
    
    if gano == True:
        if totalSanos > calculoParaFinDelJuego(conVirus):
            print("\nGANASTE!\n")
        else:
            print("\nPERDISTE!\n")



# Declaracion del main
def main():
    listaProvincias, listaHabitantes, infectados = inicializarListas()
    matriz = inicializarMatriz(listaHabitantes,infectados)
    login = llamarLogin()
    
    if login == 1:
        #RONDA 1
        matriz,presupuesto = inicioDelJuego(listaProvincias,listaHabitantes,matriz)
        #RONDA 2
        matriz,presupuesto = parteUnoJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        #RONDA 3
        matriz,presupuesto = parteDosJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        #RONDA 4
        matriz,presupuesto = parteTresJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        #RONDA 5
        matriz,presupuesto,gano = parteCuatroJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        
        finJuego(listaHabitantes,matriz,gano)
        
        print("\n------------------------------------------------------------")
        print("\t\t\tINFORMES FINALES")
        print("------------------------------------------------------------ \n")
        print(" --> Informe porcentaje de mayor cantidad de infectados por Provincia: \n")
        porcentajeMayorInfectadosPorProvincia(matriz, listaProvincias)
        print(" --> Informe de mayor porcentaje de cantidad de muertos por Provincia: \n")
        porcentajeMayorMuertosporProvincia(listaProvincias,listaHabitantes,matriz)
        print(" --> Informe de porcentaje de muertes en todo el pais:\n")
        porcentajeMuertosTotal(listaHabitantes, matriz)    
    

main()