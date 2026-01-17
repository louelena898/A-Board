import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw

# Variables globales para rastrear la posición
ultima_x, ultima_y = None, None

color_inicial = "white" # Color inicial

imagen_pil = Image.new("RGB", (1500, 800), "darkgreen")
draw = ImageDraw.Draw(imagen_pil)

def presionar(event):
    # Establece el punto de partida del dibujo.
    global ultima_x, ultima_y
    # Guarda las coordenadas (x, y) donde ocurrió el clic
    # 'event.x' y 'event.y' son las coordenadas actuales del puntero
    ultima_x, ultima_y = event.x, event.y

def pintar(event):
    # Crea la ilusión de trazo continuo uniendo puntos con líneas.
    global ultima_x, ultima_y
    
    if ultima_x is not None and ultima_y is not None:
    
        canvas.create_line(
            ultima_x, ultima_y, # Punto A (anterior)
            event.x, event.y,   # Punto B (donde está el mouse ahora)
            fill=color_inicial, # Color del trazo
            width=5,            # Grosor de la línea en píxeles
            capstyle=tk.ROUND,  # Hace que los extremos de la línea sean redondeados 
            smooth=True         # Suaviza un poco el trazo para que no se vea "pixelado"
        )

    ultima_x, ultima_y = event.x, event.y

def cambiar_rojo():
    global color_inicial
    color_inicial = "red"

def cambiar_rosado():
    global color_inicial
    color_inicial = "pink"

def cambiar_naranja():
    global color_inicial
    color_inicial = "orange"

def cambiar_amarillo():
    global color_inicial
    color_inicial = "yellow"

def cambiar_azul():
    global color_inicial
    color_inicial = "lightblue"

def cambiar_morado():
    global color_inicial
    color_inicial = "medium purple"

def cambiar_blanco():
    global color_inicial
    color_inicial = "white"

def borrador():
    global color_inicial
    color_inicial = "darkgreen"

def limpiar_pantalla():
    canvas.delete("all")

def guardar_imagen():
    try:
        nombre_archivo = "mi_dibujo_A-Board.png"
        imagen_pil.save(nombre_archivo)
        imagen_pil.show()
        messagebox.showinfo("Guardado", f"Imagen guardada como {nombre_archivo}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
        
def pintar(event):
    global ultima_x, ultima_y
    if ultima_x is not None and ultima_y is not None:
        # Esto dibuja en la pantalla (Tkinter)
        canvas.create_line(ultima_x, ultima_y, event.x, event.y, 
                           fill=color_inicial, width=5, capstyle=tk.ROUND, smooth=True)

        # Esto dibuja en el archivo (Pillow)
        draw.line([ultima_x, ultima_y, event.x, event.y], fill=color_inicial, width=5)

    ultima_x, ultima_y = event.x, event.y

# Interfaz gráfica
root = tk.Tk()
root.title("A-Board")

# Para el logo
logo = tk.PhotoImage(file='imagenes/A-Board_Logo.png')
root.iconphoto(False, logo)

canvas = tk.Canvas(root, bg="dark green", width=1500, height=800)
canvas.pack()

barra_herramientas = tk.Frame(root, bg="lightgray", pady=5)
barra_herramientas.pack(side=tk.TOP, fill=tk.X)

# Botones colores
btn_rojo = tk.Button(barra_herramientas, text="Rojo", command=cambiar_rojo)
btn_rojo.pack(side=tk.LEFT, padx=5)

btn_rosado = tk.Button(barra_herramientas, text="Rosado", command=cambiar_rosado)
btn_rosado.pack(side=tk.LEFT, padx=5)

btn_naranja = tk.Button(barra_herramientas, text="Naranja", command=cambiar_naranja)
btn_naranja.pack(side=tk.LEFT, padx=5)

btn_amarillo = tk.Button(barra_herramientas, text="Amarillo", command=cambiar_amarillo)
btn_amarillo.pack(side=tk.LEFT, padx=5)

btn_azul = tk.Button(barra_herramientas, text="Azul", command=cambiar_azul)
btn_azul.pack(side=tk.LEFT, padx=5)

btn_morado = tk.Button(barra_herramientas, text="Morado", command=cambiar_morado)
btn_morado.pack(side=tk.LEFT, padx=5)

btn_blanco = tk.Button(barra_herramientas, text="Blanco", command=cambiar_blanco)
btn_blanco.pack(side=tk.LEFT, padx=5)

btn_limpiar = tk.Button(barra_herramientas, text="Limpiar Todo", command=limpiar_pantalla)
btn_limpiar.pack(side=tk.RIGHT, padx=5)

btn_borrador = tk.Button(barra_herramientas, text="Borrador", command=borrador)
btn_borrador.pack(side=tk.RIGHT, padx=5)

btn_generar = tk.Button(barra_herramientas, text="Guardar PNG", command=guardar_imagen)
btn_generar.pack(side=tk.RIGHT, padx=5)

canvas.pack()

canvas.bind("<Button-1>", presionar)
canvas.bind("<B1-Motion>", pintar)

root.mainloop()

# Gracias por usar este programa. Atte. Lourdes :)