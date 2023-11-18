import tkinter as tk
from tkinter import ttk
import webbrowser
import pandas as pd
import plotly.express as px
import plotly.io as pio
from PIL import Image, ImageTk

df = pd.read_excel("dataset\Radicaciones y pagos.xlsx")

def cargar_imagen(ruta):
    imagen_pillow = Image.open(ruta)
    imagen_tk = ImageTk.PhotoImage(imagen_pillow)
    return imagen_tk

def mostrar_imagenes():
    imagenes = [cargar_imagen("Gráficas/Gráfica rendimiento de los asesores.png"),
                cargar_imagen("Gráficas/Gráfica rendimiento del convenio.png"),
                cargar_imagen("Gráficas/Gráfica rendimiento asesores por monto prestado.png"),
                cargar_imagen("Gráficas/Gráfica estado de los creditos.png"),
                cargar_imagen("Gráficas/Relacion entre monto y el estado.png")
                ]
    for imagen_tk in imagenes:
        etiqueta_imagen = tk.Label(frame_interior, image=imagen_tk, borderwidth=2, relief="solid")
        etiqueta_imagen.imagen_tk = imagen_tk
        etiqueta_imagen.pack(pady=10, padx=10, anchor="center")

ventana = tk.Tk()
ventana.title("Visualizador de Gráficas")
ventana.configure(bg='plum')  

frame_imagenes = tk.Frame(ventana, bg='plum', padx=20, pady=20)
frame_imagenes.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame_imagenes, bg='plum')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

estilo_scrollbar = ttk.Style()
estilo_scrollbar.configure("TScrollbar", troughcolor="plum", slidercolor="gray")
scrollbar = ttk.Scrollbar(frame_imagenes, orient=tk.VERTICAL, command=canvas.yview, style="TScrollbar")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame_interior = tk.Frame(canvas, bg='plum')
canvas.create_window((0, 0), window=frame_interior, anchor=tk.NW)

mostrar_imagenes()

tipo_letra = ('Times New Roman', 18, 'italic')
titulo_otro = tk.Label(ventana, text="Zaga Financiera", font=tipo_letra, bg='plum', fg='purple')
titulo_otro.pack(pady=10)

frame_interior.update_idletasks()
canvas.config(scrollregion=canvas.bbox(tk.ALL))

ventana.mainloop()

#lat='X5 latitude', lon='X6 longitude', size='Y house price of unit area'