import time

#Clase dron
class dron():
  def __init__(self,ubicacion, padre, cajas, cajasR,iteracion,costo):
    self.ubicacion = ubicacion
    self.padre = padre
    self.cajas = cajas
    self.cajasR = cajasR
    self.iteracion = iteracion
    self.costo = costo

def busqueda_costo(ambiente_txt):
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

  raiz = dron(inicio,dron(0,0,0,0,0,0),0,cajas,0,0)
  #Variables
  recorrido = [raiz]
  dronActual = recorrido[0]

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
        hijo = dron([derecha[0],derecha[1]],dronActual,dronActual.cajas+1,newCajas, dronActual.iteracion + 1, dronActual.costo+1)
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

    if not recorrido:
      return [[], nodos, time.time()-tiempoInicio, 0]
            
    # Encontrar el nodo con menor costo
    menor_costo = float('inf')
    indice_menor = 0
    for i, nodo in enumerate(recorrido):
      if nodo.costo < menor_costo:
        menor_costo = nodo.costo
        indice_menor = i
        
    # Eliminar el nodo seleccionado
    dronActual = recorrido.pop(indice_menor)
    nodos += 1

    ancestro = dronActual.padre
    print(ancestro.ubicacion)
    while ancestro != 0:
      if (dronActual.ubicacion == ancestro.ubicacion and 
        sorted(dronActual.cajasR) == sorted(ancestro.cajasR) and
        dronActual.costo >= ancestro.costo):
        # Ciclo detectado, seleccionar nuevo nodo
        if not recorrido:
          return [[], nodos, time.time()-tiempoInicio, 0]
                
        # Volver a seleccionar el siguiente nodo
        menor_costo = float('inf')
        indice_menor = 0
        for i, nodo in enumerate(recorrido):
          if nodo.costo < menor_costo:
            menor_costo = nodo.costo
            indice_menor = i
        dronActual = recorrido.pop(indice_menor)
        nodos += 1
        break
                
      ancestro = ancestro.padre

  print("Termino en: ==================================")
  print(recorrido[0].ubicacion)
  print(recorrido[0].iteracion)
  print(recorrido[0].cajasR)
  print(recorrido[0].padre)

  pasos = []
  costo = dronActual.costo
  while dronActual.padre != 0:
    pasos.insert(0,dronActual.ubicacion)
    dronActual = dronActual.padre

  tiempoFinal = time.time()
  
  tiempo = tiempoFinal-tiempoInicio
  print(tiempo)
  return([pasos,nodos,tiempo,costo])