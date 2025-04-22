import time

def buscar_A(ambiente_txt):
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
    #Clase dron
    class dron():
        def __init__(self,ubicacion, padre, cajas, cajasR,iteracion,costo):
            self.ubicacion = ubicacion
            self.padre = padre
            self.cajas = cajas
            self.cajasR = cajasR
            self.iteracion = iteracion
            self.costo = costo

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
    raiz = dron(inicio,dron(0,0,0,0,0,0),0,cajas,0,0)
    #Variables
    recorrido = [raiz]
    dronActual = recorrido[0]
    recorrido.pop(0)

    #Resultados finales
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
                hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas+1, newCajas, dronActual.iteracion + 1, dronActual.costo+1)
                recorrido.append(hijo)
            else:
                if ambiente[derecha[0]][derecha[1]] == 3:
                    hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+8)
                    recorrido.append(hijo)
                else:
                    hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+1)
                    recorrido.append(hijo)

        #comprobar el camino izquierdo
        if izquierda[1] >= 0 and ambiente[izquierda[0]][izquierda[1]] != 1 and ([izquierda[0],izquierda[1]] != dronActual.padre.ubicacion or ambiente[izquierda[0]][izquierda[1]+1] == 4):
            if ambiente[izquierda[0]][izquierda[1]] == 4 and [izquierda[0],izquierda[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([izquierda[0],izquierda[1]])
                hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas+1, newCajas, dronActual.iteracion + 1, dronActual.costo+1)
                recorrido.append(hijo)
            else:
                if ambiente[izquierda[0]][izquierda[1]] == 3:
                    hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+8)
                    recorrido.append(hijo)
                else:
                    hijo = dron([izquierda[0],izquierda[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+1)
                    recorrido.append(hijo)

        #comprobar el camino arriba
        if arriba[0] >= 0 and ambiente[arriba[0]][arriba[1]] != 1 and ([arriba[0],arriba[1]] != dronActual.padre.ubicacion or ambiente[arriba[0]+1][arriba[1]] == 4):
            if ambiente[arriba[0]][arriba[1]] == 4 and [arriba[0],arriba[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([arriba[0],arriba[1]])
                hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas+1, newCajas, dronActual.iteracion + 1, dronActual.costo+1)
                recorrido.append(hijo)
            else:
                if ambiente[arriba[0]][arriba[1]] == 3:
                    hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+8)
                    recorrido.append(hijo)
                else:
                    hijo = dron([arriba[0],arriba[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+1)
                    recorrido.append(hijo)

        #comprobar el camino abajo
        if abajo[0] < len(ambiente) and ambiente[abajo[0]][abajo[1]] != 1 and ([abajo[0],abajo[1]] != dronActual.padre.ubicacion or ambiente[abajo[0]-1][abajo[1]] == 4):
            if ambiente[abajo[0]][abajo[1]] == 4 and [abajo[0],abajo[1]] in dronActual.cajasR:
                newCajas = dronActual.cajasR.copy()
                newCajas.remove([abajo[0],abajo[1]])
                hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas+1, newCajas, dronActual.iteracion + 1, dronActual.costo+1)
                recorrido.append(hijo)
            else:
                if ambiente[abajo[0]][abajo[1]] == 3:
                    hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+8)
                    recorrido.append(hijo)
                else:
                    hijo = dron([abajo[0],abajo[1]],dronActual,dronActual.cajas, dronActual.cajasR, dronActual.iteracion + 1, dronActual.costo+1)
                    recorrido.append(hijo)

        #Bloque para la heuristica ========================================================
        min_total = float('inf')  # f(n) = g(n) + h(n)
        mejor_indice = 0

        print(f"{dronActual.ubicacion}==========================================================")
        print(f"Cajas recolectadas: {dronActual.cajas}, Restantes: {len(dronActual.cajasR)}")
        print(f"Costo acumulado: {dronActual.costo}")

        for d in range(len(recorrido)):
            if recorrido[d].cajasR:
                # Calcular heurística (distancia al paquete más cercano)
                distancias = [abs(recorrido[d].ubicacion[0] - caja[0]) + abs(recorrido[d].ubicacion[1] - caja[1]) 
                            for caja in recorrido[d].cajasR]
                h_actual = min(distancias) if distancias else 0
                
                # Calcular f(n) = g(n) + h(n)
                f_actual = recorrido[d].costo + h_actual
                
                print(f"Nodo {recorrido[d].ubicacion}: costo={recorrido[d].costo}, heurística={h_actual}, total={f_actual}")
                
                # Seleccionar el nodo con menor f(n)
                if f_actual < min_total or (f_actual == min_total and len(recorrido[d].cajasR) < len(recorrido[mejor_indice].cajasR)):
                    min_total = f_actual
                    mejor_indice = d
            else:
                # Si no hay cajas restantes, seleccionar este nodo inmediatamente
                mejor_indice = d
                break

        print(f"Seleccionado: {recorrido[mejor_indice].ubicacion} con f(n)={min_total}")
        dronActual = recorrido[mejor_indice]
        # Fin del bloque =======================================================

        recorrido.pop(mejor_indice)
        
        #Bloque para eliminar ciclos ====================================================
        if dronActual.padre.ubicacion != 0:  # No es el nodo raíz
            ancestro = dronActual.padre
            ciclo_detectado = False
            
            # Ciclo para evitar devolvernos a una posición anterior sin haber recolectado cajas
            while ancestro.ubicacion != 0:
                if (dronActual.ubicacion == ancestro.ubicacion and 
                    dronActual.cajas == ancestro.cajas and 
                    dronActual.costo >= ancestro.costo):
                    ciclo_detectado = True
                    break
                ancestro = ancestro.padre
            
            if ciclo_detectado:
                print(f"¡Ciclo detectado en {dronActual.ubicacion}! Eliminando nodo redundante.")
                # Buscar y eliminar nodos duplicados en el recorrido con mayor o igual costo
                recorrido = [nodo for nodo in recorrido 
                            if not (nodo.ubicacion == dronActual.ubicacion and 
                                  nodo.cajas == dronActual.cajas and 
                                  nodo.costo >= dronActual.costo)]
        #Fin del bloque ==================================

        nodos += 1

    print("Termino en: ==================================")
    print(recorrido[0].ubicacion)
    print(recorrido[0].iteracion)
    print(recorrido[0].cajasR)
    print(recorrido[0].padre)

    pasos = []
    costo = dronActual.costo
    while dronActual.padre != 0:
        print(dronActual.ubicacion)
        print(dronActual.iteracion)
        pasos.insert(0,dronActual.ubicacion)
        dronActual = dronActual.padre

    tiempoFinal = time.time()
    
    tiempo = tiempoFinal-tiempoInicio
    print(tiempo)
    return([pasos,nodos,tiempo, costo])