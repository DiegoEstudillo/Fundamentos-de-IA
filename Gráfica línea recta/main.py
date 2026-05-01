# main.py
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from consultas import generar_datos_grafica, validar_rango
import tkinter.messagebox as msg

ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("blue") 

class AplicacionRecta(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Graficador de Recta: f(x) = mx + b (Rango -100 a 100)")
        self.geometry("900x700")
        self.minsize(800, 600)
        self.configure(fg_color="white")
        self.m_var = ctk.StringVar(value="1")
        self.b_var = ctk.StringVar(value="0")
        self.estado_var = ctk.StringVar(value="Listo para graficar. Rango permitido: -100 a 100.")
        self.crear_widgets()
        self.actualizar_grafica()

    def crear_widgets(self):
        frame_controles = ctk.CTkFrame(self, corner_radius=15, fg_color="white", border_width=2, border_color="#0078D4")
        frame_controles.pack(pady=15, padx=20, fill="x")

        ctk.CTkLabel(frame_controles, text="Parámetros de la Recta", font=ctk.CTkFont(size=18, weight="bold"), text_color="#0078D4").pack(pady=(15, 15))

        grid_frame = ctk.CTkFrame(frame_controles, fg_color="white")
        grid_frame.pack(padx=20, pady=5)

        ctk.CTkLabel(grid_frame, text="Pendiente (m):", width=120, font=ctk.CTkFont(size=13), text_color="black").grid(row=0, column=0, padx=10, pady=8, sticky="e")
        self.entry_m = ctk.CTkEntry(grid_frame, textvariable=self.m_var, width=150, placeholder_text="Ej: 2.5", border_color="#0078D4",fg_color="#F0F8FF")
        self.entry_m.grid(row=0, column=1, padx=10, pady=8)

        ctk.CTkLabel(grid_frame, text="Ordenada (b):", width=120, font=ctk.CTkFont(size=13), text_color="black").grid(row=1, column=0, padx=10, pady=8, sticky="e")
        self.entry_b = ctk.CTkEntry(grid_frame, textvariable=self.b_var, width=150, placeholder_text="Ej: -3", border_color="#0078D4",fg_color="#F0F8FF")
        self.entry_b.grid(row=1, column=1, padx=10, pady=8)

        rango_label = ctk.CTkLabel(grid_frame, text="Rango válido: -100 a 100", font=ctk.CTkFont(size=11), text_color="#666666")
        rango_label.grid(row=2, column=0, columnspan=2, pady=(10, 5))

        btn_frame = ctk.CTkFrame(frame_controles, fg_color="white")
        btn_frame.pack(pady=15)

        btn_graficar = ctk.CTkButton(btn_frame, text="Graficar Recta", command=self.actualizar_grafica, width=160, height=40, fg_color="#0078D4", hover_color="#005A9E", font=ctk.CTkFont(size=14, weight="bold"))
        btn_graficar.pack(side="left", padx=15)

        btn_limpiar = ctk.CTkButton(btn_frame, text="Limpiar Campos", command=self.limpiar_campos, fg_color="#0078D4", hover_color="#005A9E", width=160, height=40, font=ctk.CTkFont(size=14, weight="bold"))
        btn_limpiar.pack(side="left", padx=15)

        self.etiqueta_estado = ctk.CTkLabel(frame_controles, textvariable=self.estado_var, text_color="#666666", font=ctk.CTkFont(size=12), wraplength=600)
        self.etiqueta_estado.pack(pady=(5, 15))

        frame_grafica = ctk.CTkFrame(self, corner_radius=15, fg_color="white", border_width=2, border_color="#0078D4")
        frame_grafica.pack(pady=10, padx=20, fill="both", expand=True)

        self.figura = Figure(figsize=(7, 5), dpi=100, facecolor='white')
        self.ax = self.figura.add_subplot(111)
        self.ax.set_facecolor('#F8F9FA')  
        self.ajustar_estilo_grafica()
        self.canvas = FigureCanvasTkAgg(self.figura, master=frame_grafica)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=15)

    def ajustar_estilo_grafica(self):
        self.ax.set_xlabel("Eje X", fontsize=11, color='black')
        self.ax.set_ylabel("Eje Y", fontsize=11, color='black')
        self.ax.set_title("f(x) = mx + b \n(Rango: -100 a 100)", fontsize=14, fontweight="bold", color='black', pad=15)
        self.ax.grid(True, linestyle='--', alpha=0.4, color='gray')
        self.ax.axhline(y=0, color='black', linewidth=1.2)
        self.ax.axvline(x=0, color='black', linewidth=1.2)
        self.ax.set_xlim(-100, 100)
        self.ax.set_ylim(-100, 100)
        self.ax.set_xticks(range(-100, 101, 20))
        self.ax.set_yticks(range(-100, 101, 20))
        self.ax.tick_params(colors='black', labelsize=9)

    def actualizar_grafica(self):
        m_text = self.m_var.get().strip()
        b_text = self.b_var.get().strip()

        if not m_text or not b_text:
            self.mostrar_error("Los campos 'm' y 'b' no pueden estar vacíos.")
            return

        es_valido, mensaje_rango = validar_rango(m_text, b_text)
        if not es_valido:
            self.mostrar_error(mensaje_rango)
            return

        x_vals, y_vals, error = generar_datos_grafica(m_text, b_text, rango=100)

        if error:
            self.mostrar_error(error)
            return

        self.ax.clear()
        self.ajustar_estilo_grafica()

        m_float = float(m_text.replace(',', '.'))
        b_float = float(b_text.replace(',', '.'))

        self.ax.plot(x_vals, y_vals, linewidth=3, color="#0078D4", label=f"y = {m_float}x + {b_float}", alpha=0.9)
        self.ax.legend(loc="upper left", fontsize=11, facecolor='white', edgecolor='#0078D4')
        self.ax.scatter([0], [b_float], color='red', s=80, zorder=5, label=f'Origen (0,{b_float})')
        self.canvas.draw()
        self.estado_var.set(f"✓ Recta graficada: m = {m_float}, b = {b_float} (Rango -100 a 100)")
        self.etiqueta_estado.configure(text_color="#28a745")

    def mostrar_error(self, mensaje):
        self.estado_var.set(mensaje)
        self.etiqueta_estado.configure(text_color="#DC3545")
        msg.showerror("Error de validación", mensaje)

    def limpiar_campos(self):
        self.m_var.set("1")
        self.b_var.set("0")
        self.estado_var.set("Campos restablecidos. Rango válido: -100 a 100.")
        self.etiqueta_estado.configure(text_color="#0078D4")
        self.actualizar_grafica()

if __name__ == "__main__":
    app = AplicacionRecta()
    app.mainloop()