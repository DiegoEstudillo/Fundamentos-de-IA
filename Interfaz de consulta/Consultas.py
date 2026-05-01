import customtkinter as ctk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

PASTEL_COLORS = ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF', '#D4B8D4', '#FFCCE5', '#B5EAD7']

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, on_success):
        super().__init__(parent, fg_color="white")
        self.on_success = on_success
    
        card = ctk.CTkFrame(self, fg_color="white", corner_radius=20, border_width=2, border_color="#FF8C00")
        card.pack(expand=True, padx=40, pady=40)
        
        ctk.CTkLabel(card, text="MCDONALD'S", font=ctk.CTkFont(size=28, weight="bold"), text_color="#FF8C00").pack(pady=20)
        ctk.CTkLabel(card, text="Sistema de Consultas", font=ctk.CTkFont(size=16), text_color="gray").pack(pady=(0,30))
        
        ctk.CTkLabel(card, text="Usuario", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=40)
        self.user_entry = ctk.CTkEntry(card, width=300, height=40, fg_color="#F5F5F5", border_color="#FF8C00")
        self.user_entry.pack(pady=(5,15), padx=40)
        
        ctk.CTkLabel(card, text="Contraseña", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=40)
        self.pass_entry = ctk.CTkEntry(card, width=300, height=40, show="*", fg_color="#F5F5F5", border_color="#FF8C00")
        self.pass_entry.pack(pady=(5,25), padx=40)
        
        self.btn_login = ctk.CTkButton(card, text="INGRESAR", width=200, height=45, 
                                       fg_color="#FF8C00", hover_color="#E67E00", 
                                       font=ctk.CTkFont(size=14, weight="bold"), command=self.verify)
        self.btn_login.pack(pady=10)
        
        self.load_credentials()
    
    def load_credentials(self):
        if os.path.exists("credentials.txt"):
            with open("credentials.txt", "r") as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    self.user, self.pwd = lines[0].strip(), lines[1].strip()
                    return
        self.user, self.pwd = "admin", "admin123"
        with open("credentials.txt", "w") as f:
            f.write(f"{self.user}\n{self.pwd}")
    
    def verify(self):
        if self.user_entry.get() == self.user and self.pass_entry.get() == self.pwd:
            self.on_success()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.user_entry.delete(0, 'end')
            self.pass_entry.delete(0, 'end')

class QueryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="white")
        self.load_data()
        self.create_widgets()
    
    def load_data(self):
        try:
            self.df = pd.read_csv('mcdonalds_dataset.csv')
            print(f"Datos cargados: {len(self.df)} registros")
        except FileNotFoundError:
            print("Archivo no encontrado")
    
    def create_widgets(self):
        header = ctk.CTkFrame(self, fg_color="#FF8C00", height=60, corner_radius=0)
        header.pack(fill="x")
        ctk.CTkLabel(header, text="MCDONALD'S - CONSULTAS", font=ctk.CTkFont(size=20, weight="bold"), 
                     text_color="white").pack(pady=15)
        
        btn_container = ctk.CTkScrollableFrame(self, fg_color="white", orientation="horizontal", height=80)
        btn_container.pack(fill="x", padx=10, pady=10)
        
        queries = [
            ("Activos por Estado", self.grafico_activos_estado),
            ("Top Ciudades", self.grafico_top_ciudades),
            ("% Dañados", self.grafico_porcentaje_danados),
            ("Mapa de Ubicaciones", self.grafico_mapa),
            ("Tiempo Verificación", self.grafico_tiempo_verificacion),
            ("Actividad por Estado", self.grafico_actividad_estado),
            ("Tipo de Vía", self.grafico_tipo_via),
            ("Working vs Broken", self.grafico_working_broken),
            ("Patrones en Calles", self.grafico_patrones_calles),
            ("Resumen General", self.grafico_resumen)
        ]
        
        for text, command in queries:
            btn = ctk.CTkButton(btn_container, text=text, command=command, 
                               fg_color="#FF8C00", hover_color="#E67E00",
                               font=ctk.CTkFont(size=12, weight="bold"), width=180, height=50)
            btn.pack(side="left", padx=5, pady=5)
        
        self.plot_frame = ctk.CTkFrame(self, fg_color="white")
        self.plot_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.status = ctk.CTkLabel(self.plot_frame, text="Seleccione una consulta", 
                                   font=ctk.CTkFont(size=16, weight="bold"), text_color="#FF8C00")
        self.status.pack(expand=True)
    
    def mostrar_grafica(self, fig, titulo):
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        
        self.status = ctk.CTkLabel(self.plot_frame, text=f"{titulo}", 
                                   font=ctk.CTkFont(size=14, weight="bold"), text_color="#FF8C00")
        self.status.pack(pady=10)
        
        canvas = FigureCanvasTkAgg(fig, self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
        plt.close(fig)
    
    #graficas
    
    def grafico_activos_estado(self):
        datos = self.df[self.df['is_active'] == True].groupby('state').size().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(datos.index, datos.values, color=PASTEL_COLORS[:len(datos)], edgecolor='white', linewidth=2)
        ax.set_title('Locales Activos por Estado', fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('Estado', fontsize=11)
        ax.set_ylabel('Cantidad de Locales', fontsize=11)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, datos.values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                   str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        self.mostrar_grafica(fig, "Locales Activos por Estado")
    
    def grafico_top_ciudades(self):
        datos = self.df.groupby('city').size().nlargest(8).sort_values(ascending=True)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(datos.index, datos.values, color=PASTEL_COLORS[:len(datos)], edgecolor='white', linewidth=2)
        ax.set_title('Top Ciudades con Más Locales', fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('Cantidad de Locales', fontsize=11)
        ax.set_ylabel('Ciudad', fontsize=11)
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, datos.values):
            ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
                   str(val), ha='left', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        self.mostrar_grafica(fig, "Top Ciudades")
    
    def grafico_porcentaje_danados(self):
        total = len(self.df)
        danados = len(self.df[self.df['is_broken'] == True])
        activos = total - danados
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.pie([activos, danados], labels=['Activos', 'Dañados'], autopct='%1.1f%%',
               colors=['#BAFFC9', '#FFB3BA'], explode=(0, 0.05), shadow=True,
               textprops={'fontsize': 11, 'fontweight': 'bold'})
        ax1.set_title('Distribución General', fontsize=12, fontweight='bold')
        
        bars = ax2.bar(['Activos', 'Dañados'], [activos, danados], 
                      color=['#BAFFC9', '#FFB3BA'], edgecolor='white', linewidth=2)
        ax2.set_title('Cantidad de Locales', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Cantidad', fontsize=11)
        ax2.grid(axis='y', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, [activos, danados]):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    str(val), ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        fig.suptitle('Estado de los Locales', fontsize=14, fontweight='bold')
        plt.tight_layout()
        self.mostrar_grafica(fig, "Porcentaje de Locales Dañados")
    
    def grafico_mapa(self):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        working = self.df[self.df['dot'] == 'working']
        broken = self.df[self.df['dot'] == 'broken']
        
        ax.scatter(working['lon'], working['lat'], c='#BAFFC9', s=100, alpha=0.7, 
                  edgecolors='white', linewidth=1.5, label='Working')
        ax.scatter(broken['lon'], broken['lat'], c='#FFB3BA', s=100, alpha=0.7, 
                  edgecolors='white', linewidth=1.5, label='Broken', marker='s')
        
        ax.set_xlabel('Longitud', fontsize=11, fontweight='bold')
        ax.set_ylabel('Latitud', fontsize=11, fontweight='bold')
        ax.set_title('Distribución Geográfica de Locales', fontsize=14, fontweight='bold')
        ax.legend(loc='upper right', fontsize=11)
        ax.grid(True, alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        self.mostrar_grafica(fig, "Mapa de Ubicaciones")
    
    def grafico_tiempo_verificacion(self):
        def get_minutes(txt):
            try:
                return int(txt.split()[1])
            except:
                return 999
        
        self.df['minutes'] = self.df['last_checked'].apply(get_minutes)
        
        bins = [0, 30, 60, 120, 240, float('inf')]
        labels = ['<30 min', '30-60 min', '1-2h', '2-4h', '>4h']
        self.df['rango'] = pd.cut(self.df['minutes'], bins=bins, labels=labels, right=False)
        
        datos = self.df['rango'].value_counts().sort_index()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(datos.index, datos.values, color=PASTEL_COLORS[:len(datos)], edgecolor='white', linewidth=2)
        ax.set_title('Tiempo desde Última Verificación', fontsize=14, fontweight='bold')
        ax.set_xlabel('Tiempo', fontsize=11)
        ax.set_ylabel('Cantidad de Locales', fontsize=11)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, datos.values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                   str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        self.mostrar_grafica(fig, "Tiempo de Verificación")
    
    def grafico_actividad_estado(self):
        total = self.df.groupby('state').size()
        activos = self.df[self.df['is_active'] == True].groupby('state').size()
        pct = (activos / total * 100).fillna(0).sort_values(ascending=True)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(pct.index, pct.values, color=PASTEL_COLORS[:len(pct)], edgecolor='white', linewidth=2)
        ax.set_title('Porcentaje de Actividad por Estado', fontsize=14, fontweight='bold')
        ax.set_xlabel('Porcentaje de Actividad (%)', fontsize=11)
        ax.set_ylabel('Estado', fontsize=11)
        ax.set_xlim(0, 105)
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, pct.values):
            ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                   f'{val:.1f}%', ha='left', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        self.mostrar_grafica(fig, "Actividad por Estado")
    
    def grafico_tipo_via(self):
        """NUEVA CONSULTA: Distribución de locales por tipo de vía (CORREGIDA)"""
        tipos_via = {
            'Street (Calle)': self.df['street'].str.contains('Street|St', case=False, na=False).sum(),
            'Avenue (Avenida)': self.df['street'].str.contains('Avenue|Ave', case=False, na=False).sum(),
            'Boulevard (Bulevar)': self.df['street'].str.contains('Boulevard|Blvd', case=False, na=False).sum(),
            'Broadway': self.df['street'].str.contains('Broadway', case=False, na=False).sum(),
            'Road (Carretera)': self.df['street'].str.contains('Road|Rd', case=False, na=False).sum(),
            'Drive': self.df['street'].str.contains('Drive|Dr', case=False, na=False).sum(),
            'Court': self.df['street'].str.contains('Court|Ct', case=False, na=False).sum(),
            'Lane': self.df['street'].str.contains('Lane|Ln', case=False, na=False).sum(),
        }
        
        total_patrones = sum(tipos_via.values())
        otros = len(self.df) - total_patrones
        if otros > 0:
            tipos_via['Otros'] = otros
        
        tipos_via = {k: v for k, v in tipos_via.items() if v > 0}
        
        sorted_items = sorted(tipos_via.items(), key=lambda x: x[1], reverse=True)
        tipos = [item[0] for item in sorted_items]
        cantidades = [item[1] for item in sorted_items]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        ax1.pie(cantidades, labels=tipos, autopct='%1.1f%%',
               colors=PASTEL_COLORS[:len(tipos)], shadow=True,
               textprops={'fontsize': 9})
        ax1.set_title('Distribución por Tipo de Vía', fontsize=12, fontweight='bold')
        
        bars = ax2.barh(tipos, cantidades, color=PASTEL_COLORS[:len(tipos)], 
                       edgecolor='white', linewidth=2)
        ax2.set_title('Cantidad por Tipo de Vía', fontsize=12, fontweight='bold')
        ax2.set_xlabel('Cantidad de Locales', fontsize=11)
        ax2.set_ylabel('Tipo de Vía', fontsize=11)
        ax2.grid(axis='x', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, cantidades):
            ax2.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                    str(val), ha='left', va='center', fontsize=10, fontweight='bold')
        
        fig.suptitle('DISTRIBUCIÓN DE LOCALES POR TIPO DE VÍA', fontsize=14, fontweight='bold')
        plt.tight_layout()
        self.mostrar_grafica(fig, "Distribución por Tipo de Vía")
    
    def grafico_working_broken(self):
        pivot = pd.crosstab(self.df['state'], self.df['dot'])
        
        if 'working' not in pivot.columns:
            pivot['working'] = 0
        if 'broken' not in pivot.columns:
            pivot['broken'] = 0
        
        fig, ax = plt.subplots(figsize=(12, 7))
        pivot[['working', 'broken']].plot(kind='bar', stacked=True, ax=ax, 
                                          color=['#BAFFC9', '#FFB3BA'], edgecolor='white', linewidth=1)
        ax.set_title('Working vs Broken por Estado', fontsize=14, fontweight='bold')
        ax.set_xlabel('Estado', fontsize=11)
        ax.set_ylabel('Cantidad de Locales', fontsize=11)
        ax.legend(title='Estado', labels=['Working', 'Broken'])
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        for container in ax.containers:
            ax.bar_label(container, label_type='center', fontsize=9, fontweight='bold')
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        self.mostrar_grafica(fig, "Working vs Broken")
    
    def grafico_patrones_calles(self):
        tipos_via = {
            'Street/St': self.df['street'].str.contains('Street|St', case=False, na=False).sum(),
            'Avenue/Ave': self.df['street'].str.contains('Avenue|Ave', case=False, na=False).sum(),
            'Boulevard/Blvd': self.df['street'].str.contains('Boulevard|Blvd', case=False, na=False).sum(),
            'Broadway': self.df['street'].str.contains('Broadway', case=False, na=False).sum(),
            'Road/Rd': self.df['street'].str.contains('Road|Rd', case=False, na=False).sum(),
        }
        
        total_patrones = sum(tipos_via.values())
        otros = len(self.df) - total_patrones
        if otros > 0:
            tipos_via['Otros'] = otros
        
        tipos_via = {k: v for k, v in tipos_via.items() if v > 0}
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(tipos_via.keys(), tipos_via.values(), 
                     color=PASTEL_COLORS[:len(tipos_via)], edgecolor='white', linewidth=2)
        ax.set_title('Patrones en Nombres de Calles', fontsize=14, fontweight='bold')
        ax.set_xlabel('Tipo de Vía', fontsize=11)
        ax.set_ylabel('Cantidad', fontsize=11)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        for bar, val in zip(bars, tipos_via.values()):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                   str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        self.mostrar_grafica(fig, "Patrones en Calles")
    
    def grafico_resumen(self):
        total = len(self.df)
        activos = len(self.df[self.df['is_active'] == True])
        danados = len(self.df[self.df['is_broken'] == True])
        estados = self.df['state'].nunique()
        ciudades = self.df['city'].nunique()
        working = len(self.df[self.df['dot'] == 'working'])
        broken = len(self.df[self.df['dot'] == 'broken'])
        
        fig = plt.figure(figsize=(14, 10))
        
        ax1 = plt.subplot(2, 3, 1)
        metrics = ['Total', 'Activos', 'Dañados', 'Estados', 'Ciudades', 'Working', 'Broken']
        values = [total, activos, danados, estados, ciudades, working, broken]
        colors = ['#BAFFC9', '#BAFFC9', '#FFB3BA', '#BAE1FF', '#D4B8D4', '#BAFFC9', '#FFB3BA']
        bars = ax1.bar(metrics, values, color=colors, edgecolor='white', linewidth=2)
        ax1.set_title('Métricas Generales', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Cantidad', fontsize=10)
        for bar, val in zip(bars, values):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        
        ax2 = plt.subplot(2, 3, 2)
        top_estados = self.df.groupby('state').size().nlargest(5)
        ax2.pie(top_estados.values, labels=top_estados.index, autopct='%1.1f%%',
               colors=PASTEL_COLORS[:len(top_estados)], shadow=True)
        ax2.set_title('Top 5 Estados', fontsize=12, fontweight='bold')
        
        ax3 = plt.subplot(2, 3, 3)
        ax3.pie([activos, total-activos], labels=['Activos', 'Inactivos'], autopct='%1.1f%%',
               colors=['#BAFFC9', '#FFDFBA'], explode=(0.05, 0))
        ax3.set_title('Nivel de Actividad', fontsize=12, fontweight='bold')
        
        ax4 = plt.subplot(2, 3, 4)
        ax4.pie([working, broken], labels=['Working', 'Broken'], autopct='%1.1f%%',
               colors=['#BAFFC9', '#FFB3BA'], explode=(0.05, 0))
        ax4.set_title('Estado Operativo', fontsize=12, fontweight='bold')
        
        ax5 = plt.subplot(2, 3, 5)
        top_ciudades = self.df.groupby('city').size().nlargest(5).sort_values(ascending=True)
        bars = ax5.barh(top_ciudades.index, top_ciudades.values, 
                       color=PASTEL_COLORS[:len(top_ciudades)], edgecolor='white', linewidth=2)
        ax5.set_title('Top 5 Ciudades', fontsize=12, fontweight='bold')
        ax5.set_xlabel('Cantidad', fontsize=10)
        for bar, val in zip(bars, top_ciudades.values):
            ax5.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
                    str(val), ha='left', va='center', fontsize=9, fontweight='bold')
        
        ax6 = plt.subplot(2, 3, 6)
        ax6.pie([danados, total-danados], labels=['Dañados', 'En buen estado'], autopct='%1.1f%%',
               colors=['#FFB3BA', '#BAFFC9'], explode=(0.05, 0))
        ax6.set_title('Estado Físico', fontsize=12, fontweight='bold')
        
        fig.suptitle('RESUMEN GENERAL DE LOCALES MCDONALD\'S', fontsize=16, fontweight='bold')
        plt.tight_layout()
        self.mostrar_grafica(fig, "Resumen General")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("McDonald's - Sistema de Consultas")
        self.geometry("1400x900")
        self.minsize(1200, 700)
        
        self.login = LoginFrame(self, self.mostrar_consultas)
        self.login.pack(fill="both", expand=True)
    
    def mostrar_consultas(self):
        self.login.pack_forget()
        self.query = QueryFrame(self)
        self.query.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()