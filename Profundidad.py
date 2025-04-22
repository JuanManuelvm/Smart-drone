import time

#Clase dron
class dron():
  def __init__(self,ubicacion, padre, cajas, cajasR,iteracion):
    self.ubicacion = ubicacion
    self.padre = padre
    self.cajas = cajas
    self.cajasR = cajasR
    self.iteracion = iteracion

def busqueda_profundidad(ambiente_txt):
    # Función para leer el archivo y organizar la información en una matriz
    def leer_matriz_desde_archivo(ambiente_txt):
        matriz = []
        with open(ambiente_txt, 'r') as archivo:
            for línea in archivo:
                fila = [int(numero) for numero in línea.split()]
                matriz.append(fila)
        return matriz

    # Leer la matriz desde el archivo
    ambiente = leer_matriz_desde_archivo(ambiente_txt)
    #=================================================================
    tiempoInicio = time.time()
    print(tiempoInicio)
    
    #Ciclo para definir cual es el inicio del dron
    inicio = [0,0]
    for fila in range(len(ambiente)):
        for columna in range(fila):
            if ambiente[fila][columna] == 2:
                inicio = [fila,columna]

    raiz = dron(inicio,dron(0,0,0,0,0),0,[],0)
    #Variables
    recorrido = [raiz]
    dronActual = recorrido[0]
    nodos = 0

    #Recorrido
    while dronActual.cajas != 3:
        recorrido.pop(0)

        derecha = [dronActual.ubicacion[0],dronActual.ubicacion[1] + 1]
        izquierda = [dronActual.ubicacion[0],dronActual.ubicacion[1] - 1]
        arriba = [dronActual.ubicacion[0] - 1, dronActual.ubicacion[1]]
        abajo = [dronActual.ubicacion[0] + 1, dronActual.ubicacion[1]]

        #comprobar el camino derecho
        if derecha[1] < len(ambiente[0]) and ambiente[derecha[0]][derecha[1]] != 1 and ([derecha[0],derecha[1]] != dronActual.padre.ubicacion or ambiente[derecha[0]][derecha[1]-1] == 4):
            if ambiente[derecha[0]][derecha[1]] == 4 and [derecha[0],derecha[1]] not in dronActual.cajasR:
                hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas+1,dronActual.cajasR+[[derecha[0],derecha[1]]], dronActual.iteracion + 1)
                recorrido.insert(0, hijo)
            else:
                hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.insert(0, hijo)

        #comprobar el camino izquierdo
        if izquierda[1] >= 0 and ambiente[izquierda[0]][izquierda[1]] != 1 and ([izquierda[0],izquierda[1]] != dronActual.padre.ubicacion or ambiente[izquierda[0]][izquierda[1]+1] == 4):
            if ambiente[izquierda[0]][izquierda[1]] == 4 and [izquierda[0],izquierda[1]] not in dronActual.cajasR:
                hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas+1, dronActual.cajasR + [[izquierda[0],izquierda[1]]], dronActual.iteracion + 1)
                recorrido.insert(0, hijo)
            else:
                hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.insert(0, hijo)

        #comprobar el camino arriba
        if arriba[0] >= 0 and ambiente[arriba[0]][arriba[1]] != 1 and ([arriba[0],arriba[1]] != dronActual.padre.ubicacion or ambiente[arriba[0]+1][arriba[1]] == 4):
            if ambiente[arriba[0]][arriba[1]] == 4 and [arriba[0],arriba[1]] not in dronActual.cajasR:
                hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas+1, dronActual.cajasR + [[arriba[0],arriba[1]]], dronActual.iteracion + 1)
                recorrido.insert(0, hijo)
            else:
                hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.insert(0, hijo)

        #comprobar el camino abajo
        if abajo[0] < len(ambiente) and ambiente[abajo[0]][abajo[1]] != 1 and ([abajo[0],abajo[1]] != dronActual.padre.ubicacion or ambiente[abajo[0]-1][abajo[1]] == 4):
            if ambiente[abajo[0]][abajo[1]] == 4 and [abajo[0],abajo[1]] not in dronActual.cajasR:
                hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas+1, dronActual.cajasR + [[abajo[0],abajo[1]]], dronActual.iteracion + 1)
                recorrido.insert(0, hijo)
            else:
                hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.insert(0, hijo)

        dronActual = recorrido[0]

        ciclo = dronActual.padre
        while ciclo.ubicacion != 0:
            if dronActual.ubicacion == ciclo.ubicacion:
                recorrido.pop(0)
                dronActual = recorrido[0]
            ciclo = ciclo.padre
        nodos += 1

    print("Termino en: ==================================")
    print(recorrido[0].ubicacion)
    print(recorrido[0].iteracion)
    print(recorrido[0].cajasR)
    print(recorrido[0].padre)

    pasos = []
    while dronActual.padre != 0:
        pasos.insert(0,dronActual.ubicacion)
        dronActual = dronActual.padre

    tiempoFinal = time.time()
    
    tiempo = tiempoFinal-tiempoInicio
    print(tiempo)
    return([pasos,nodos,tiempo])
