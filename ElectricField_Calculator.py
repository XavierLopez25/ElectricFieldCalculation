# Importando las bibliotecas necesarias
import tkinter as tk  # Biblioteca estándar para crear interfaces gráficas en Python
from tkinter import ttk  # Módulo que proporciona acceso a widgets adicionales de tkinter
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arrays
from scipy.integrate import quad  # Función para realizar integraciones numéricas
import matplotlib.pyplot as plt  # Biblioteca para crear gráficos y visualizaciones
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Permite embeber gráficos de Matplotlib en una aplicación tkinter

# Definición de la clase principal de la aplicación
class ElectricFieldApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Creación de una etiqueta para seleccionar la distribución de carga
        self.label_combo = ttk.Label(self, text="Distribución de carga:")
        self.label_combo.pack(pady=5)

        # Creación de un combobox para que el usuario elija una distribución de carga
        self.combo = ttk.Combobox(self, values=["Anillo", "Disco", "Línea de carga"], state="readonly")
        self.combo.bind("<<ComboboxSelected>>", self.update_fields)
        self.combo.pack(pady=5)
        
        # Creación de una etiqueta y un campo de entrada para la carga
        self.label_charge = ttk.Label(self, text="Carga (Q) en Coulombs:")
        self.label_charge.pack(pady=5)
        self.entry_charge = ttk.Entry(self)
        self.entry_charge.pack(pady=5)

        # Creación de una etiqueta y un campo de entrada para parámetros adicionales (radio o longitud)
        self.label_param = ttk.Label(self, text="")
        self.label_param.pack(pady=5)
        self.entry_param = ttk.Entry(self)
        self.entry_param.pack(pady=5)

        # Creación de una etiqueta y un campo de entrada para la posición en el eje x
        self.label_position = ttk.Label(self, text="Posición en eje x (x):")
        self.label_position.pack(pady=5)
        self.entry_position = ttk.Entry(self)
        self.entry_position.pack(pady=5)

        # Creación de un botón para iniciar el cálculo del campo eléctrico
        self.button = ttk.Button(self, text="Calcular", command=self.calculate_field)
        self.button.pack(pady=20)

        # Creación de etiquetas para mostrar leyendas sobre la gráfica
        self.label_arrow_legend = ttk.Label(self, text="⬆ Flecha roja: Campo eléctrico en el punto x.")
        self.label_arrow_legend.pack(pady=5)

        # Etiqueta de leyenda para las líneas/distribuciones azules
        self.label_distribution_legend = ttk.Label(self, text="Azul: Distribución de carga (Anillo, Disco, Línea de carga).")
        self.label_distribution_legend.pack(pady=5)

        # Creación de una etiqueta para mostrar el resultado del cálculo
        self.label_result = ttk.Label(self, text="")
        self.label_result.pack(pady=5)

        # Canvas para mostrar la gráfica
        self.canvas = None

    # Método para actualizar los campos de entrada según la distribución seleccionada
    def update_fields(self, event):
        selection = self.combo.get()

        # Restablecer la etiqueta y la entrada
        self.label_param.config(text="")
        self.entry_param.delete(0, tk.END)

        if selection == "Anillo" or selection == "Disco":
            self.label_param.config(text="Radio (R):")
        elif selection == "Línea de carga":
            self.label_param.config(text="Longitud (l):")
    
    # Método para calcular el campo eléctrico según la distribución seleccionada
    def calculate_field(self):
        try:
            Q = float(self.entry_charge.get())  # Obtener la carga ingresada por el usuario
        except ValueError:
            self.label_result.config(text="Por favor, ingrese una carga válida.")
            return

        if self.combo.get() == "Anillo":
            self.electric_field_anillo(float(self.entry_param.get()), float(self.entry_position.get()), Q)
        elif self.combo.get() == "Disco":
            self.electric_field_disco(float(self.entry_param.get()), float(self.entry_position.get()), Q)
        elif self.combo.get() == "Línea de carga":
            self.electric_field_line(float(self.entry_param.get()), float(self.entry_position.get()), Q)


# ---------------------------------------------------------------------------------

        # Define la longitud de la flecha en función de la magnitud de E y de los límites del eje.
        arrow_length = 10 * np.abs(E) / 10  
        
        # Limita la longitud máxima de la flecha a cierto valor 
        arrow_length = min(arrow_length, 50)
        
        # Ajusta el tamaño de la punta de la flecha basándote en la longitud de la flecha
        head_length = 0.2 * (arrow_length/2)  
        head_width = head_length  
        
        # Dibuja campo eléctrico en dirección del eje x
        direction = np.sign(E)
        ax.arrow(x, 0, direction * arrow_length, 0, head_width=head_width, head_length=head_length, fc='red', ec='red')
        
        # Dimensiones para el plano cartesiano de la interfaz
        ax.set_xlim([-100, 100])
        ax.set_ylim([-100, 100])
        
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Inicialización y ejecución de la aplicación
app = ElectricFieldApp()
app.mainloop()