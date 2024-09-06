import random

def imprimirMatriz(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range (filas): 
        for c in range(columnas): 
            print(matriz[f][c], end=" ")
        print()

def inicializarListas():
    listaProvincias = ['Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Cordoba', 'Corrientes', 'Entre Rios', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquen', 'Rio Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucuman']
    listaHabitantes = [random.randint(1000000, 15000000) for _ in range(23)]
    infectados = [random.randint(1000, 5500) for _ in range(23)]
    #Estas 3 listas trabajaran de manera paralela 

    return listaProvincias, listaHabitantes

def inicializarMatriz(listaHabitantes,infectados): 
    filas = 23
    columnas = 3
    matriz = [[0] * columnas for i in range(filas)] 
    # Se preinicializa la matriz por comprension con valores en 0 para luego ser remplazados
    # El siguiente bucle for, accede directamente a las 3 posiciones (columnas) de la matriz 
    # De sanos, infectados y muertos, correspondientemente y recorre pais por pais asignando sus valores random 
    for f in range(filas):
        matriz[f][0] = (listaHabitantes[f] - infectados[f]) #sanos 
        matriz[f][1] = infectados[f] #infectados 
        matriz[f][2] = 0 #muertos

    return matriz