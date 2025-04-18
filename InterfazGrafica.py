import tkinter as tk
from tkinter import Canvas, Button, Menu
import Amplitud, Costo, Profundidad, Avara, A
from tkinter import messagebox as MessageBox

class LaberintoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Laberinto Smart drone")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("750x600")
        
        # Matriz del laberinto (0: vacío, 1: muro, 2: dron, 3: alerta, 4: caja)
        self.laberinto = [
            [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 2, 0, 3, 4, 4, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [3, 3, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 4, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # Tamaño de cada celda
        self.cell_size = 50
        
        # Crear el lienzo para el laberinto
        self.canvas = Canvas(root, bg='white', 
                            width=len(self.laberinto[0])*self.cell_size, 
                            height=len(self.laberinto)*self.cell_size)
        
        self.canvas.pack(expand=True)

        # Dibujar el laberinto
        self.dibujar_laberinto()
        
        
        # Crear un frame para los botones
        self.botones_frame = tk.Frame(root)
        
        self.botones_frame.pack(expand=True, pady=10)
        
        # Crear botón 1 con menú desplegable
        self.boton1 = Button(self.botones_frame, text="No informado", command=self.mostrar_menu_noInformado)
        self.boton1.pack(side=tk.LEFT, padx=10)
        
        # Crear botón 3 con menú desplegable
        self.boton2 = Button(self.botones_frame, text="Informado", command=self.mostrar_menu_Informado)
        self.boton2.pack(side=tk.LEFT, padx=10)

        # Crear botón 2
        self.boton3 = Button(self.botones_frame, text="Reiniciar", command=self.reiniciar)
        self.boton3.pack(side=tk.LEFT, padx=10)
        
        # Posición inicial del dron
        self.dron_pos = self.encontrar_dron()
        
        # Variable para almacenar la estrategia seleccionada
        self.estrategia = None
        
    
    def mostrar_menu_noInformado(self):
        """Muestra un menú desplegable con las opciones de movimiento"""
        menu = Menu(self.root, tearoff=0)
        menu.add_command(label="Amplitud", command=lambda: self.seleccionar_estrategia("Amplitud"))
        menu.add_command(label="Costo", command=lambda: self.seleccionar_estrategia("Costo"))
        menu.add_command(label="Profundidad", command=lambda: self.seleccionar_estrategia("Profundidad"))
        
        # Mostrar el menú cerca del botón
        x = self.boton1.winfo_rootx()
        y = self.boton1.winfo_rooty() + self.boton1.winfo_height()
        menu.post(x, y)
    
    def mostrar_menu_Informado(self):
        """Muestra un menú desplegable con las opciones de movimiento"""
        menu = Menu(self.root, tearoff=0)
        menu.add_command(label="Avara", command=lambda: self.seleccionar_estrategia("Avara"))
        menu.add_command(label="A*", command=lambda: self.seleccionar_estrategia("A*"))
        
        # Mostrar el menú cerca del botón
        x = self.boton2.winfo_rootx()
        y = self.boton2.winfo_rooty() + self.boton1.winfo_height()
        menu.post(x, y)
    
    def seleccionar_estrategia(self, estrategia):
        """Establece la estrategia seleccionada y muestra un mensaje"""
        self.estrategia = estrategia
        print(f"Estrategia seleccionada: {estrategia}")
        
        # Aquí podrías implementar la lógica de movimiento según la estrategia
        if estrategia == "Amplitud":
            self.mover_amplitud()
        elif estrategia == "Costo":
            self.mover_costo()
        elif estrategia == "Profundidad":
            self.mover_profundidad()
        elif estrategia == "Avara":
            self.mover_avara()
        elif estrategia == "A*":
            self.mover_A()
    
    def mover_amplitud(self):
        """Implementación básica de movimiento por amplitud"""
        print("Ejecutando búsqueda en amplitud...")
        # Aquí iría el algoritmo real de búsqueda en amplitud
        self.reiniciar()
        datos = Amplitud.busqueda_amplitud()
        self.mover_dron_simple(datos[0],datos[1], datos[2])
        
    
    def mover_costo(self):
        """Implementación básica de movimiento por costo"""
        print("Ejecutando búsqueda de costo uniforme...")
        # Aquí iría el algoritmo real de búsqueda de 
        self.reiniciar()
        datos = Costo.busqueda_costo()
        self.mover_dron_simple(datos[0],datos[1], datos[2], datos[3])
    
    def mover_profundidad(self):
        """Implementación básica de movimiento por profundidad"""
        print("Ejecutando búsqueda en profundidad...")
        # Aquí iría el algoritmo real de búsqueda en profundidad
        self.reiniciar()
        datos = Profundidad.busqueda_profundidad()
        self.mover_dron_simple(datos[0],datos[1], datos[2])

    def mover_avara(self):
        """Implementación básica de movimiento por Avara"""
        print("Ejecutando búsqueda en Avara...")
        # Aquí iría el algoritmo real de búsqueda en Avara
        self.reiniciar()
        datos = Avara.busqueda_avara()
        self.mover_dron_simple(datos[0],datos[1], datos[2])
    
    def mover_A(self):
        """Implementación básica de movimiento por A*"""
        print("Ejecutando búsqueda en A*...")
        # Aquí iría el algoritmo real de búsqueda en A*
        self.reiniciar()
        pasos = A.buscar_A()
        self.mover_dron_simple(pasos)
    
    def mover_dron_simple(self, pasos, nodos, tiempo, costo=None):
        """Función simple para mover el dron (ejemplo) y actualizar inmediatamente el laberinto"""
        if not self.dron_pos:
            return

        # Función interna para mover el dron de un paso
        def mover_paso(ni, nj):
            i, j = self.dron_pos
            if 0 <= ni < len(self.laberinto) and 0 <= nj < len(self.laberinto[0]):
                if self.laberinto[ni][nj] == 0 or self.laberinto[ni][nj] == 3 or self.laberinto[ni][nj] == 4:  # Solo se puede mover a espacios vacíos
                    # Actualizar matriz
                    self.laberinto[i][j] = 0
                    self.laberinto[ni][nj] = 2
                    self.dron_pos = (ni, nj)

                    # Redibujar laberinto
                    self.canvas.delete("all")
                    self.dibujar_laberinto()

        # Función recursiva para mover el dron en cada paso con retraso
        def mover_con_retraso(indice_paso):
            if indice_paso < len(pasos):
                ni, nj = pasos[indice_paso]
                mover_paso(ni, nj)
                # Llamar a la función nuevamente después de 500 ms para el siguiente paso
                root.after(500, mover_con_retraso, indice_paso + 1)

        # Comenzar el movimiento con el primer paso
        pasos_totales = len(pasos)
        mover_con_retraso(0)

         # Al finalizar el recorrido, mostrar mensaje con los resultados
        if costo is not None:
            self.mostrar_resultados(pasos_totales, nodos, tiempo, costo)
        else:
            self.mostrar_resultados(pasos_totales, nodos, tiempo,)

    def mostrar_resultados(self, pasos_totales, nodos, tiempo, costo=None):
        """Muestra los resultados al final del recorrido"""
        mensaje = f"El recorrido finalizó con un arbol de profundidad {pasos_totales} . \n"
        mensaje += f"El recorrido finalizó con {nodos} nodos expandidos . \n"
        mensaje += f"El recorrido finalizó con un tiempo de {tiempo} segundos . \n"         
        if costo is not None:
            mensaje += f"El costo total fue: {costo}."
        print(mensaje)
        MessageBox.showinfo("Resultado!", mensaje) # título, mensaje

    def encontrar_dron(self):
        """Encuentra la posición del dron en la matriz"""
        for i, fila in enumerate(self.laberinto):
            for j, valor in enumerate(fila):
                if valor == 2:
                    return (i, j)
        return None
    
    def dibujar_laberinto(self):
        """Dibuja el laberinto completo basado en la matriz"""
        for i, fila in enumerate(self.laberinto):
            for j, valor in enumerate(fila):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if valor == 1:  # Muro
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray", outline="black")
                elif valor == 2:  # Dron
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                    self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="blue")
                elif valor == 3:  # Alerta
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                    self.canvas.create_polygon(x1+10, y2-10, x2-10, y2-10, (x1+x2)/2, y1+10, fill="yellow")
                elif valor == 4:  # Caja
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                    self.canvas.create_rectangle(x1+5, y1+5, x2-5, y2-5, fill="brown")
                else:  # Espacio vacío (0)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")          
        
    def reiniciar(self):
        """Reinicia el laberinto a su estado original"""
        self.laberinto = [
            [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 2, 0, 3, 4, 4, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [3, 3, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 4, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.dron_pos = self.encontrar_dron()
        self.estrategia = None
        self.canvas.delete("all")
        self.dibujar_laberinto()

# Crear la ventana principal

root = tk.Tk()
app = LaberintoApp(root)
root.mainloop()
