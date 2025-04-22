import time

#Clase dron
class dron():
  def __init__(self,ubicacion, padre, cajas, cajasR,iteracion):
    self.ubicacion = ubicacion
    self.padre = padre
    self.cajas = cajas
    self.cajasR = cajasR
    self.iteracion = iteracion

def busqueda_avara(ambiente_txt):
    # Función para leer el archivo y organizar la información en una matriz
    def leer_matriz_desde_archivo(ambiente_txt):
        matriz = []
        with open(ambiente_txt, 'r') as archivo:
            for línea in archivo:
                # Convertir cada línea en una lista de enteros
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


        #Bloque para la heuristica ========================================================
        min_heuristica = float('inf') 
        mejor_indice = 0

        print(f"{dronActual.ubicacion}==========================================================")
        print(f"Cajas recolectadas: {dronActual.cajas}, Restantes: {len(dronActual.cajasR)}")

        # Ciclo para evaluar nodos para encontrar el mejor
        for d in range(len(recorrido)):
            if recorrido[d].cajasR:
                # Calcular distancia Manhattan a cada paquete restante
                distancias = [abs(recorrido[d].ubicacion[0] - caja[0]) + abs(recorrido[d].ubicacion[1] - caja[1]) 
                            for caja in recorrido[d].cajasR]
                h_actual = min(distancias)  # Tomar la distancia al más cercano
                
                print(f"Heurística para {recorrido[d].ubicacion}: {h_actual} (paquetes restantes: {len(recorrido[d].cajasR)})")
                
                # Actualizar el mejor nodo encontrado
                if h_actual < min_heuristica or (h_actual == min_heuristica and len(recorrido[d].cajasR) < len(recorrido[mejor_indice].cajasR)):
                    min_heuristica = h_actual
                    mejor_indice = d
            else:
                # Si encontramos nodo sin cajas restantes, seleccionarlo inmediatamente
                mejor_indice = d
                break

        print(f"Transición: {dronActual.ubicacion} -> {recorrido[mejor_indice].ubicacion}")

        # Asignar el mejor nodo encontrado
        dronActual = recorrido[mejor_indice]

        print(f"Mínima heurística encontrada: {min_heuristica}")
        print(f"Seleccionado: {dronActual.ubicacion} con {len(dronActual.cajasR)} cajas restantes")
        # Fin del bloque =======================================================
        
        recorrido.pop(mejor_indice)

        #Bloque para eliminar ciclos ====================================================
        if dronActual.padre.ubicacion != 0:
            ancestro = dronActual.padre
            es_ciclo_simple = False
            
            #Ciclo para evitar devolverse
            while ancestro.ubicacion != 0:
                if dronActual.ubicacion == ancestro.ubicacion and dronActual.cajas == ancestro.cajas:
                    es_ciclo_simple = True
                    break
                ancestro = ancestro.padre
            
            # Solo eliminar el ciclo si no hemos recolectado una caja en el camino
            if es_ciclo_simple:
                print(f"¡Ciclo detectado en {dronActual.ubicacion}! Eliminando nodo repetido.")
                # Buscar y eliminar nodos duplicados en el recorrido
                recorrido = [nodo for nodo in recorrido if nodo.ubicacion != dronActual.ubicacion or nodo.cajas != dronActual.cajas]
                
                # Si quedan nodos en el recorrido, tomar el siguiente mejor
                if recorrido:
                    min_heuristica = float('inf')
                    mejor_indice = 0
                    for d in range(len(recorrido)):
                        if recorrido[d].cajasR:
                            distancias = [abs(recorrido[d].ubicacion[0] - caja[0]) + abs(recorrido[d].ubicacion[1] - caja[1]) 
                                        for caja in recorrido[d].cajasR]
                            h_actual = min(distancias)
                            if h_actual < min_heuristica:
                                min_heuristica = h_actual
                                mejor_indice = d
                    dronActual = recorrido[mejor_indice]
                    recorrido.pop(mejor_indice)
        #Fin del bloque ==================================
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
