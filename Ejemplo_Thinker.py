import tkinter as tk

# Función que se ejecuta cuando se hace clic en el botón
def mostrar_datos():
    numero_local = entrada_numero.get()
    nombre_local = entrada_nombre.get()
    unidad_negocio = entrada_unidad.get()
    
    mensaje = f"Número de Local: {numero_local}\nNombre del Local: {nombre_local}\nUnidad de Negocio: {unidad_negocio}"
    etiqueta_resultado.config(text=mensaje)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Interfaz para Datos de Local")
ventana.geometry("400x300")  # Establece un tamaño para la ventana

# Cargar una imagen para usar como icono
imagen_icono = tk.PhotoImage(file="C:/ejemplos/tata.jpg")  # Ajusta la ruta a tu imagen

# Configurar la imagen como icono de ventana
ventana.iconphoto(True, imagen_icono)

# Etiqueta para Número de Local
etiqueta_numero = tk.Label(ventana, text="Número de Local:")
etiqueta_numero.pack()
entrada_numero = tk.Entry(ventana)
entrada_numero.pack()

# Etiqueta para Nombre del Local
etiqueta_nombre = tk.Label(ventana, text="Nombre del Local:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Etiqueta para Unidad de Negocio
etiqueta_unidad = tk.Label(ventana, text="Unidad de Negocio:")
etiqueta_unidad.pack()
entrada_unidad = tk.Entry(ventana)
entrada_unidad.pack()

# Botón para mostrar los datos ingresados
boton = tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos)
boton.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
