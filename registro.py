import tkinter as tk
from tkinter import messagebox

def guardar_registro():
    nombre = entrada_nombre.get()
    apellidos = entrada_apellidos.get()
    celular = entrada_celular.get()

    # Verificar datos
    if nombre == "" or apellidos == "" or celular == "":
        messagebox.showwarning(
            "Datos incompletos",
            "Por favor, completa todos los campos."
        )
        return

    # Mostrar registro
    messagebox.showinfo(
        "Registro exitoso",
        f"Persona registrada correctamente.\n\n"
        f"Nombre: {nombre}\n"
        f"Apellidos: {apellidos}\n"
        f"Número celular: {celular}\n"
        
    )


# ==========================================
# VENTANA PRINCIPAL
# ==========================================

ventana = tk.Tk()

ventana.title("Sistema de Registro Biométrico")
ventana.geometry("600x500")
ventana.resizable(False, False)


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="REGISTRO DE PERSONAS",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=20)


subtitulo = tk.Label(
    ventana,
    text="Registro mediante huella digital",
    font=("Arial", 12)
)

subtitulo.pack(pady=5)


# ==========================================
# DATOS PERSONALES
# ==========================================

marco_datos = tk.LabelFrame(
    ventana,
    text="Datos personales",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=20
)

marco_datos.pack(
    padx=30,
    pady=20,
    fill="x"
)


# Nombre
tk.Label(
    marco_datos,
    text="Nombre:"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=8
)

entrada_nombre = tk.Entry(
    marco_datos,
    width=40
)

entrada_nombre.grid(
    row=0,
    column=1,
    pady=8
)


# Apellidos
tk.Label(
    marco_datos,
    text="Apellidos:"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=8
)

entrada_apellidos = tk.Entry(
    marco_datos,
    width=40
)

entrada_apellidos.grid(
    row=1,
    column=1,
    pady=8
)


# Número celular
tk.Label(
    marco_datos,
    text="Número celular:"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=8
)

entrada_celular = tk.Entry(
    marco_datos,
    width=40
)

entrada_celular.grid(
    row=2,
    column=1,
    pady=8
)


boton_guardar = tk.Button(
    ventana,
    text="GUARDAR REGISTRO",
    command=guardar_registro,
    width=30,
    height=2
)

boton_guardar.pack(pady=20)

#jeje

# ==========================================
# EJECUTAR
# ==========================================

ventana.mainloop()