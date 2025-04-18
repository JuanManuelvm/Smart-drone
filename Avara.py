import time
#Ingresar los datos de un mundo determinado por medio de un archivo de texto que siga las convenciones dadas anteriormente.
# Función para leer el archivo y organizar la información en una matriz
def leer_matriz_desde_archivo(ambiente_txt):
    matriz = []
    with open(ambiente_txt, 'r') as archivo:
        for línea in archivo:
            # Convertir cada línea en una lista de enteros
            fila = [int(numero) for numero in línea.split()]
            matriz.append(fila)
    return matriz

# Nombre del archivo
ambiente_txt = 'Prueba1.txt'

# Leer la matriz desde el archivo
ambiente = leer_matriz_desde_archivo(ambiente_txt)

# Imprimir la matriz
for fila in ambiente:
    print(fila)


#Clase dron
class dron():
  def __init__(self,ubicacion, padre, cajas, cajasR,iteracion):
    self.ubicacion = ubicacion
    self.padre = padre
    self.cajas = cajas
    self.cajasR = cajasR
    self.iteracion = iteracion

def busqueda_avara():
    tiempoInicio = time.time()
    print(tiempoInicio)
    #Ciclo para definir cual es el inicio del dron
    inicio = [0,0]
    cajas = []
    for fila in range(len(ambiente)):
        for columna in range(len(ambiente[fila])):
            if ambiente[fila][columna] == 2:
                inicio = [fila,columna]
            if ambiente[fila][columna] == 4:
                cajas.append([fila,columna])
    print(cajas)
    raiz = dron(inicio,dron(0,0,0,0,0),0,cajas,0)
    #Variables
    recorrido = [raiz]
    dronActual = recorrido[0]
    recorrido.pop(0)
    nodos = 0

    #Recorrido
    while dronActual.cajasR != []:
        derecha = [dronActual.ubicacion[0],dronActual.ubicacion[1] + 1]
        izquierda = [dronActual.ubicacion[0],dronActual.ubicacion[1] - 1]
        arriba = [dronActual.ubicacion[0] - 1, dronActual.ubicacion[1]]
        abajo = [dronActual.ubicacion[0] + 1, dronActual.ubicacion[1]]

        #comprobar el camino derecho
        if derecha[1] < len(ambiente[0]) and ambiente[derecha[0]][derecha[1]] != 1 and ([derecha[0],derecha[1]] != dronActual.padre.ubicacion or ambiente[derecha[0]][derecha[1]-1] == 4):
            if ambiente[derecha[0]][derecha[1]] == 4 and [derecha[0],derecha[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([derecha[0],derecha[1]])
                hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas+1,newCajas, dronActual.iteracion + 1)
                recorrido.append(hijo)
            else:
                hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.append(hijo)

        #comprobar el camino izquierdo
        if izquierda[1] >= 0 and ambiente[izquierda[0]][izquierda[1]] != 1 and ([izquierda[0],izquierda[1]] != dronActual.padre.ubicacion or ambiente[izquierda[0]][izquierda[1]+1] == 4):
            if ambiente[izquierda[0]][izquierda[1]] == 4 and [izquierda[0],izquierda[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([izquierda[0],izquierda[1]])
                hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas+1,newCajas, dronActual.iteracion + 1)
                recorrido.append(hijo)
            else:
                hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.append(hijo)

        #comprobar el camino arriba
        if arriba[0] >= 0 and ambiente[arriba[0]][arriba[1]] != 1 and ([arriba[0],arriba[1]] != dronActual.padre.ubicacion or ambiente[arriba[0]+1][arriba[1]] == 4):
            if ambiente[arriba[0]][arriba[1]] == 4 and [arriba[0],arriba[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([arriba[0],arriba[1]])
                hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas+1, newCajas, dronActual.iteracion + 1)
                recorrido.append(hijo)
            else:
                hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.append(hijo)

        #comprobar el camino abajo
        if abajo[0] < len(ambiente) and ambiente[abajo[0]][abajo[1]] != 1 and ([abajo[0],abajo[1]] != dronActual.padre.ubicacion or ambiente[abajo[0]-1][abajo[1]] == 4):
            if ambiente[abajo[0]][abajo[1]] == 4 and [abajo[0],abajo[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([abajo[0],abajo[1]])
                hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas+1, newCajas, dronActual.iteracion + 1)
                recorrido.append(hijo)
            else:
                hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1)
                recorrido.append(hijo)


        min_heuristica = 10000

        print(str(dronActual.ubicacion)+"==========================================================")
        print(dronActual.cajas)
        for d in range(len(recorrido)):
            hTotal = 0
            if recorrido[d].cajasR != []:
                for caja in recorrido[d].cajasR:
                    diferenciaFila = recorrido[d].ubicacion[0] - caja[0]
                    diferenciaColumna = recorrido[d].ubicacion[1] - caja[1]
                    h = abs(diferenciaFila) + abs(diferenciaColumna)
                    print("Heuristica de" +str(recorrido[d].ubicacion)+ " es de "+str(h)+" hasta "+str(caja))
                    hTotal += h
                print("Heuristica total: "+str(hTotal))
                if min_heuristica >= hTotal:
                    min_heuristica = hTotal
                    dronActual = recorrido[d]
                    indice = d
            else:
                min_heuristica = hTotal
                dronActual = recorrido[d]
                indice = d

        print("Minima heuristica: "+str(min_heuristica))
        print(dronActual.ubicacion)

        recorrido.pop(indice)

        ciclo = dronActual.padre
        while ciclo.ubicacion != 0:
            if dronActual.ubicacion == ciclo.ubicacion:
                recorrido.pop(0)
                dronActual = recorrido[0]
            ciclo = ciclo.padre
        nodos += 1

    print("Termino en: ==================================")
    print(dronActual.ubicacion)
    print(dronActual.iteracion)

    pasos = []
    while dronActual.padre != 0:
        print(dronActual.ubicacion)
        print(dronActual.iteracion)
        pasos.insert(0,dronActual.ubicacion)
        dronActual = dronActual.padre

    tiempoFinal = time.time()
  
    tiempo = tiempoFinal-tiempoInicio
    print(tiempo)
    return([pasos,nodos,tiempo,])
