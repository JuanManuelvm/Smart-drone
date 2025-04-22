import tkinter as tk
from tkinter import Canvas, Button, Menu, filedialog
import os
import Amplitud, Costo, Profundidad, Avara, A
from tkinter import messagebox as MessageBox

class LaberintoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Laberinto Smart drone")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("750x650")
        
        # Variable para almacenar el archivo seleccionado
        self.NuevoAmbiente = "Prueba1.txt"  # Valor por defecto
        
        # Frame superior para controles
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=10)
        
        # Botón para seleccionar archivo
        self.btn_seleccionar = Button(self.top_frame, text="Seleccionar Ambiente", 
                                    command=self.seleccionar_archivo)
        self.btn_seleccionar.pack(side=tk.LEFT, padx=10)
        
        # Etiqueta para mostrar el archivo seleccionado
        self.lbl_archivo = tk.Label(self.top_frame, text=f"Archivo: {self.NuevoAmbiente}")
        self.lbl_archivo.pack(side=tk.LEFT, padx=10)
        
        # Cargar el laberinto inicial
        self.cargar_laberinto()
        
        # Tamaño de cada celda
        self.cell_size = 50
        
        # Crear el lienzo para el laberinto
        self.canvas = Canvas(root, bg='white', 
                            width=len(self.laberinto[0])*self.cell_size, 
                            height=len(self.laberinto)*self.cell_size)
        self.canvas.pack(expand=True)
        
        # Dibujar el laberinto
        self.dibujar_laberinto()
        
        # Crear un frame para los botones de algoritmos
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

    def seleccionar_archivo(self):
        """Abre un diálogo para seleccionar el archivo del ambiente"""
        # Obtener la lista de archivos .txt en el directorio actual
        archivos = [f for f in os.listdir() if f.endswith('.txt')]
        
        if not archivos:
            MessageBox.showwarning("Advertencia", "No se encontraron archivos .txt en la carpeta")
            return
        
        # Crear ventana de selección
        seleccion = tk.Toplevel(self.root)
        seleccion.title("Seleccionar archivo de ambiente")
        seleccion.geometry("300x400")
        
        # Lista de archivos
        lbl_titulo = tk.Label(seleccion, text="Seleccione un archivo:")
        lbl_titulo.pack(pady=10)
        
        lista = tk.Listbox(seleccion)
        for archivo in archivos:
            lista.insert(tk.END, archivo)
        lista.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
        
        # Botón de selección
        btn_aceptar = Button(seleccion, text="Seleccionar", 
                           command=lambda: self.actualizar_archivo(lista.get(tk.ACTIVE), seleccion))
        btn_aceptar.pack(pady=10)

    def actualizar_archivo(self, archivo, ventana_seleccion):
        """Actualiza el archivo seleccionado y recarga el laberinto"""
        self.NuevoAmbiente = archivo
        self.lbl_archivo.config(text=f"Archivo: {self.NuevoAmbiente}")
        ventana_seleccion.destroy()
        self.cargar_laberinto()
        self.reiniciar()
    
    def cargar_laberinto(self):
        """Carga la matriz del laberinto desde el archivo seleccionado"""
        try:
            with open(self.NuevoAmbiente, 'r') as archivo:
                self.laberinto = []
                for línea in archivo:
                    fila = [int(numero) for numero in línea.split()]
                    self.laberinto.append(fila)
        except FileNotFoundError:
            MessageBox.showerror("Error", f"No se encontró el archivo: {self.NuevoAmbiente}")
            self.laberinto = [[0]]  # Matriz vacía por defecto si hay error        
    
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
        datos = Amplitud.busqueda_amplitud(self.NuevoAmbiente)
        self.mover_dron_simple(datos[0],datos[1], datos[2])
        
    
    def mover_costo(self):
        """Implementación básica de movimiento por costo"""
        print("Ejecutando búsqueda de costo uniforme...")
        # Aquí iría el algoritmo real de búsqueda de 
        self.reiniciar()
        datos = Costo.busqueda_costo(self.NuevoAmbiente)
        self.mover_dron_simple(datos[0],datos[1], datos[2], datos[3])
    
    def mover_profundidad(self):
        """Implementación básica de movimiento por profundidad"""
        print("Ejecutando búsqueda en profundidad...")
        # Aquí iría el algoritmo real de búsqueda en profundidad
        self.reiniciar()
        datos = Profundidad.busqueda_profundidad(self.NuevoAmbiente)
        self.mover_dron_simple(datos[0],datos[1], datos[2])

    def mover_avara(self):
        """Implementación básica de movimiento por Avara"""
        print("Ejecutando búsqueda en Avara...")
        # Aquí iría el algoritmo real de búsqueda en Avara
        self.reiniciar()
        datos = Avara.busqueda_avara(self.NuevoAmbiente)
        self.mover_dron_simple(datos[0],datos[1], datos[2])
    
    def mover_A(self):
        """Implementación básica de movimiento por A*"""
        print("Ejecutando búsqueda en A*...")
        # Aquí iría el algoritmo real de búsqueda en A*
        self.reiniciar()
        datos = A.buscar_A(self.NuevoAmbiente)
        self.mover_dron_simple(datos[0],datos[1], datos[2], datos[3])
    
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
        mensaje = f"Profundidad = {pasos_totales}. \n"
        mensaje += f"Nodos expandios = {nodos}. \n"
        mensaje += f"Tiempo de ejecucion {tiempo} segundos. \n"         
        if costo is not None:
            mensaje += f"Costo total =  {costo}."
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
        self.cargar_laberinto()
        self.dron_pos = self.encontrar_dron()
        self.estrategia = None
        self.canvas.delete("all")
        self.dibujar_laberinto()

# Crear la ventana principal

root = tk.Tk()
app = LaberintoApp(root)
root.mainloop()
