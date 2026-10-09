import tkinter as tk
from tkinter import ttk, messagebox

class RegistroHuella:
    def __init__(self, id_registro, nombre, edad, sexo, telefono, estado):
        self.id_registro = id_registro
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.telefono = telefono
        self.estado = estado

    def get_id_registro(self): return self.id_registro
    def get_nombre(self): return self.nombre
    def get_edad(self): return self.edad
    def get_sexo(self): return self.sexo
    def get_telefono(self): return self.telefono
    def get_estado(self): return self.estado


class SistemaHuellaDigital(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro con Huella digital")
        self.geometry("900x600")
        self.minsize(800, 500)

        self.registros = []

        # Contenedor principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Menú Lateral
        self.crear_menu()

        # Contenedor de Tarjetas (Frames)
        self.panel_cards = tk.Frame(self)
        self.panel_cards.grid(row=0, column=1, sticky="nsew")
        self.panel_cards.grid_rowconfigure(0, weight=1)
        self.panel_cards.grid_columnconfigure(0, weight=1)

        # Diccionario para almacenar las vistas
        self.frames = {}
        self.crear_vistas()

        self.mostrar_panel("Inicio")

    def crear_menu(self):
        menu = tk.Frame(self, bg="#006699", width=200)
        menu.grid(row=0, column=0, sticky="nsew")
        menu.grid_propagate(False)

        for i in range(4):
            menu.grid_rowconfigure(i, weight=0)
        menu.grid_columnconfigure(0, weight=1)

        btn_inicio = tk.Button(menu, text="Inicio", bg="#006699", fg="white", font=("Arial", 11, "bold"), bd=0, command=lambda: self.mostrar_panel("Inicio"))
        btn_registrar = tk.Button(menu, text="Registrar", bg="#006699", fg="white", font=("Arial", 11, "bold"), bd=0, command=lambda: self.mostrar_panel("Registrar"))
        btn_ver_registros = tk.Button(menu, text="Ver Registros", bg="#006699", fg="white", font=("Arial", 11, "bold"), bd=0, command=self.abrir_ver_registros)
        btn_salir = tk.Button(menu, text="Salir", bg="#006699", fg="white", font=("Arial", 11, "bold"), bd=0, command=self.quit)

        botones = [btn_inicio, btn_registrar, btn_ver_registros, btn_salir]
        for idx, btn in enumerate(botones):
            btn.grid(row=idx, column=0, sticky="ew", padx=10, pady=10)

    def crear_vistas(self):
        for F, nombre in [
            (self.panel_inicio, "Inicio"),
            (self.panel_registrar_persona, "Registrar"),
            (self.panel_ver_registros, "VerRegistros")
        ]:
            frame = F(self.panel_cards)
            self.frames[nombre] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_panel(self, nombre):
        frame = self.frames[nombre]
        frame.tkraise()

    def panel_inicio(self, parent):
        panel = tk.Frame(parent)
        titulo = tk.Label(panel, text="Sistema de Registro con Huella Digital", font=("Arial", 22, "bold"))
        titulo.pack(expand=True)
        return panel

    def panel_registrar_persona(self, parent):
        panel = tk.Frame(parent)
        
        form_frame = tk.Frame(panel)
        form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(form_frame, text="ID Registro:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        txt_id = tk.Entry(form_frame, width=20)
        txt_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Nombre:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        txt_nombre = tk.Entry(form_frame, width=20)
        txt_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Edad:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        combo_edad = ttk.Combobox(form_frame, values=list(range(1, 101)), width=17, state="readonly")
        combo_edad.current(0)
        combo_edad.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Sexo:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        var_sexo = tk.StringVar(value="Masculino")
        panel_sexo = tk.Frame(form_frame)
        tk.Radiobutton(panel_sexo, text="Masculino", variable=var_sexo, value="Masculino").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(panel_sexo, text="Femenino", variable=var_sexo, value="Femenino").pack(side=tk.LEFT, padx=5)
        panel_sexo.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        tk.Label(form_frame, text="Teléfono:", font=("Arial", 10)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        txt_telefono = tk.Entry(form_frame, width=20)
        txt_telefono.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Estado / Observación:", font=("Arial", 10)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        txt_estado = tk.Entry(form_frame, width=20)
        txt_estado.grid(row=5, column=1, padx=5, pady=5)

        def guardar():
            if not txt_id.get().strip() or not txt_nombre.get().strip():
                messagebox.showerror("Error", "Faltan datos obligatorios del registro")
                return

            r = RegistroHuella(
                txt_id.get(),
                txt_nombre.get(),
                int(combo_edad.get()),
                var_sexo.get(),
                txt_telefono.get(),
                txt_estado.get()
            )
            self.registros.append(r)
            messagebox.showinfo("Éxito", "Registro con huella guardado correctamente")

            txt_id.delete(0, tk.END)
            txt_nombre.delete(0, tk.END)
            txt_telefono.delete(0, tk.END)
            txt_estado.delete(0, tk.END)
            combo_edad.current(0)
            var_sexo.set("Masculino")

        btn_guardar = tk.Button(form_frame, text="Guardar Registro", bg="#006699", fg="white", command=guardar)
        btn_guardar.grid(row=6, column=1, sticky="e", pady=15)

        return panel

    def panel_ver_registros(self, parent):
        panel = tk.Frame(parent)
        panel.grid_rowconfigure(1, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        # Panel Superior
        p_sup = tk.Frame(panel, padx=10, pady=10)
        p_sup.grid(row=0, column=0, sticky="ew")
        
        tk.Label(p_sup, text="Registros de Huella Digital", font=("Arial", 14, "bold")).pack(anchor="center", pady=5)
        
        p_busq = tk.Frame(p_sup)
        p_busq.pack(fill=tk.X, pady=5)

        tk.Label(p_busq, text="Buscar por nombre:").pack(side=tk.LEFT, padx=5)
        self.txt_buscar_registro = tk.Entry(p_busq)
        self.txt_buscar_registro.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.txt_buscar_registro.bind("<Return>", lambda e: self.buscar_registros())

        tk.Button(p_busq, text="Mostrar todos", command=lambda: [self.txt_buscar_registro.delete(0, tk.END), self.actualizar_registros()]).pack(side=tk.RIGHT, padx=2)
        tk.Button(p_busq, text="Buscar", command=self.buscar_registros).pack(side=tk.RIGHT, padx=2)

        # Tabla (Treeview)
        columnas = ("ID", "Nombre", "Edad", "Sexo", "Teléfono", "Estado / Observación")
        self.tabla_registros = ttk.Treeview(panel, columns=columnas, show="headings")
        
        for col in columnas:
            self.tabla_registros.heading(col, text=col)
            self.tabla_registros.column(col, width=100, anchor="center")

        scrollbar = ttk.Scrollbar(panel, orient=tk.VERTICAL, command=self.tabla_registros.yview)
        self.tabla_registros.configure(yscroll=scrollbar.set)

        self.tabla_registros.grid(row=1, column=0, sticky="nsew", padx=10)
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Panel Inferior
        p_inf = tk.Frame(panel, padx=10, pady=10)
        p_inf.grid(row=2, column=0, sticky="e")

        def eliminar():
            seleccion = self.tabla_registros.selection()
            if not seleccion:
                messagebox.showwarning("Aviso", "Selecciona un registro de la tabla para eliminarlo.")
                return
            
            item = self.tabla_registros.item(seleccion)
            id_en_tabla = item['values'][0]
            nombre_en_tabla = item['values'][1]

            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el registro de \"{nombre_en_tabla}\" (ID: {id_en_tabla})?"):
                self.registros = [r for r in self.registros if r.get_id_registro() != str(id_en_tabla)]
                self.actualizar_registros()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")

        btn_eliminar = tk.Button(p_inf, text="Eliminar Registro Seleccionado", bg="#b43232", fg="white", command=eliminar)
        btn_eliminar.pack()

        return panel

    def abrir_ver_registros(self):
        self.txt_buscar_registro.delete(0, tk.END)
        self.actualizar_registros()
        self.mostrar_panel("VerRegistros")

    def actualizar_registros(self):
        for row in self.tabla_registros.get_children():
            self.tabla_registros.delete(row)
        for r in self.registros:
            self.tabla_registros.insert("", tk.END, values=(
                r.get_id_registro(),
                r.get_nombre(),
                r.get_edad(),
                r.get_sexo(),
                r.get_telefono(),
                r.get_estado()
            ))

    def buscar_registros(self):
        nombre_buscado = self.txt_buscar_registro.get().strip().lower()
        for row in self.tabla_registros.get_children():
            self.tabla_registros.delete(row)
        for r in self.registros:
            if nombre_buscado in r.get_nombre().lower():
                self.tabla_registros.insert("", tk.END, values=(
                    r.get_id_registro(),
                    r.get_nombre(),
                    r.get_edad(),
                    r.get_sexo(),
                    r.get_telefono(),
                    r.get_estado()
                ))

if __name__ == "__main__":
    app = SistemaHuellaDigital()
    app.mainloop()
#jejeje
    