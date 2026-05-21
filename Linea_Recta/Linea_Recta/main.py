# main.py
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from consultas import generar_datos_grafica
import tkinter.messagebox as msg

ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("blue")

class AplicacionRecta(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Graficador de Recta: f(x) = mx + b")
        self.geometry("850x650")
        self.configure(fg_color="white")
        self.minsize(750, 550)
        self.m_var = ctk.StringVar(value="1")
        self.b_var = ctk.StringVar(value="0")
        self.estado_var = ctk.StringVar(value="Listo para graficar.")
        self.crear_widgets()
        self.actualizar_grafica()

    def crear_widgets(self):
        frame_controles = ctk.CTkFrame(self, corner_radius=10, fg_color="#F5F7FA")
        frame_controles.pack(pady=15, padx=20, fill="x")

        ctk.CTkLabel(frame_controles, text="Parámetros de la Recta", font=ctk.CTkFont(size=16, weight="bold"), text_color="#2C3E50").pack(pady=(10, 15))

        grid_frame = ctk.CTkFrame(frame_controles, fg_color="transparent")
        grid_frame.pack(padx=20, pady=5)

        ctk.CTkLabel(grid_frame, text="Pendiente (m):", text_color="#34495E", width=100).grid(row=0, column=0, padx=10, pady=8, sticky="e")
        entry_m = ctk.CTkEntry(grid_frame, textvariable=self.m_var, width=120, placeholder_text="Ej: 2.5", fg_color="white")
        entry_m.grid(row=0, column=1, padx=10, pady=8)

        ctk.CTkLabel(grid_frame, text="Ordenada (b):", text_color="#34495E", width=100).grid(row=1, column=0, padx=10, pady=8, sticky="e")
        entry_b = ctk.CTkEntry(grid_frame, textvariable=self.b_var, width=120, placeholder_text="Ej: -3", fg_color="white")
        entry_b.grid(row=1, column=1, padx=10, pady=8)

        #botones
        btn_frame = ctk.CTkFrame(frame_controles, fg_color="transparent")
        btn_frame.pack(pady=15)

        btn_graficar = ctk.CTkButton(
            btn_frame, 
            text="Graficar Recta", 
            command=self.actualizar_grafica,
            width=140, 
            height=35,
            fg_color="#4A9EFF",    
            hover_color="#6BB3FF",    
            text_color="white"
        )
        
        btn_graficar.pack(side="left", padx=10)

        btn_limpiar = ctk.CTkButton(
            btn_frame, 
            text="Limpiar Campos", 
            command=self.limpiar_campos,
            width=140, 
            height=35,
            fg_color="#B0BEC5",    
            hover_color="#90A4AE",    
            text_color="white"
        )
        btn_limpiar.pack(side="left", padx=10)

        self.etiqueta_estado = ctk.CTkLabel(
            frame_controles, 
            textvariable=self.estado_var,
            text_color="#7F8C8D", 
            font=ctk.CTkFont(size=12)
        )
        
        self.etiqueta_estado.pack(pady=(5, 15))

        frame_grafica = ctk.CTkFrame(
            self, 
            corner_radius=10, 
            fg_color="white",
            border_width=1, 
            border_color="#E0E5EC"
        )
        frame_grafica.pack(pady=10, padx=20, fill="both", expand=True)

        self.figura = Figure(figsize=(6, 4.5), dpi=100)
        self.ax = self.figura.add_subplot(111)
        self.ajustar_estilo_grafica()
        self.canvas = FigureCanvasTkAgg(self.figura, master=frame_grafica)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    def ajustar_estilo_grafica(self):
        self.ax.set_facecolor('#FAFBFC') 
        self.ax.set_xlabel("Eje X", fontsize=10, color="#2C3E50")
        self.ax.set_ylabel("Eje Y", fontsize=10, color="#2C3E50")
        self.ax.set_title("f(x) = mx + b", fontsize=14, fontweight="bold", color="#2C3E50")
        self.ax.grid(True, linestyle='--', alpha=0.6, color='#BDC3C7')
        self.ax.axhline(y=0, color='#2C3E50', linewidth=0.8)
        self.ax.axvline(x=0, color='#2C3E50', linewidth=0.8)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

    def actualizar_grafica(self):
        m_text = self.m_var.get()
        b_text = self.b_var.get()
        x_vals, y_vals, error = generar_datos_grafica(m_text, b_text)

        if error:
            self.estado_var.set(error)
            self.etiqueta_estado.configure(text_color="#E74C3C")  # Rojo para error
            msg.showerror("Datos no válidos", error)
            return

        self.ax.clear()
        self.ajustar_estilo_grafica()

        m_float = float(m_text.replace(',', '.'))
        b_float = float(b_text.replace(',', '.'))
        self.ax.plot(
            x_vals, y_vals, 
            linewidth=2.5, 
            color="#4A9EFF", 
            label=f"y = {m_float}x + {b_float}"
        )
        self.ax.legend(loc="upper left", fontsize=10, facecolor='white', edgecolor='#E0E5EC')
        self.canvas.draw()
        self.estado_var.set(f"Recta graficada: m = {m_float}, b = {b_float}")
        self.etiqueta_estado.configure(text_color="#27AE60")  # Verde éxito

    def limpiar_campos(self):
        self.m_var.set("1")
        self.b_var.set("0")
        self.estado_var.set("Campos restablecidos a m=1, b=0. ¡Grafica de nuevo!")
        self.etiqueta_estado.configure(text_color="#7F8C8D")
        self.actualizar_grafica()

if __name__ == "__main__":
    app = AplicacionRecta()
    app.mainloop()