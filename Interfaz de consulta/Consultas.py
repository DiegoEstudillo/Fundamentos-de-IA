import customtkinter as ctk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, fg_color="transparent")
        self.parent = parent
        self.on_login_success = on_login_success
        
        # Frame central para el login
        self.login_frame = ctk.CTkFrame(self, corner_radius=20)
        self.login_frame.pack(expand=True, padx=40, pady=40)
        
        ctk.CTkLabel(self.login_frame, text="SISTEMA DE CONSULTAS MCDONALD'S", 
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)
        
        ctk.CTkLabel(self.login_frame, text="Usuario:", font=ctk.CTkFont(size=14)).pack(pady=(20,5))
        self.user_entry = ctk.CTkEntry(self.login_frame, width=300, height=40)
        self.user_entry.pack(pady=5)
        
        ctk.CTkLabel(self.login_frame, text="Contraseña:", font=ctk.CTkFont(size=14)).pack(pady=(10,5))
        self.pass_entry = ctk.CTkEntry(self.login_frame, width=300, height=40, show="*")
        self.pass_entry.pack(pady=5)
        
        self.login_btn = ctk.CTkButton(self.login_frame, text="Iniciar Sesión", 
                                        width=200, height=45, command=self.verify_login,
                                        font=ctk.CTkFont(size=14, weight="bold"))
        self.login_btn.pack(pady=30)
        
        # Cargar credenciales desde archivo
        self.credentials = self.load_credentials()
        
    def load_credentials(self):
        """Carga credenciales desde archivo credentials.txt"""
        if os.path.exists("credentials.txt"):
            with open("credentials.txt", "r") as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    return lines[0].strip(), lines[1].strip()
        # Credenciales por defecto si no existe el archivo
        default_user, default_pass = "admin", "admin123"
        with open("credentials.txt", "w") as f:
            f.write(f"{default_user}\n{default_pass}")
        return default_user, default_pass
    
    def verify_login(self):
        user = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()
        
        if user == self.credentials[0] and password == self.credentials[1]:
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.user_entry.delete(0, 'end')
            self.pass_entry.delete(0, 'end')

class QueryFrame(ctk.CTkFrame):
    def __init__(self, parent, main_app):
        super().__init__(parent, fg_color="transparent")
        self.main_app = main_app
        self.df = None
        self.load_data()
        self.create_widgets()
        
    def load_data(self):
        try:
            import io
            data = """lat,lon,alt,is_broken,is_active,dot,state,city,street,country,last_checked
-73.988281,40.71883,0,False,True,working,NY,New York,114 Delancey St,USA,Checked 142 minutes ago
-74.00509,40.728794,0,False,True,working,NY,New York,208 Varick St,USA,Checked 142 minutes ago
-73.993408,40.729197,0,False,True,working,NY,New York,724 Broadway,USA,Checked 142 minutes ago
-73.985855,40.726555,0,False,True,working,NY,New York,102 1st Ave,USA,Checked 142 minutes ago
-73.991692,40.691383,0,True,True,broken,NY,Brooklyn,82 Court St,USA,Checked 142 minutes ago
-73.982277,40.731014,0,False,True,working,NY,New York,404 E 14th St,USA,Checked 142 minutes ago
-73.996726,40.737864,0,False,True,working,NY,New York,541 6th Ave,USA,Checked 142 minutes ago
-73.990517,40.736977,0,True,True,broken,NY,New York,39 Union Square W,USA,Checked 142 minutes ago
-74.0387,40.726501,0,False,True,working,NJ,Jersey City,30 Mall Dr W,USA,Checked 142 minutes ago
-74.043057,40.719843,0,True,True,broken,NJ,Jersey City,325 Grove St,USA,Checked 142 minutes ago"""
            self.df = pd.read_csv(io.StringIO(data))
        except Exception as e:
            print(f"Error loading data: {e}")
            self.df = pd.DataFrame({
                'lat': [-73.988], 'lon': [40.718], 'alt': [0], 'is_broken': [False],
                'is_active': [True], 'dot': ['working'], 'state': ['NY'], 'city': ['New York'],
                'street': ['Test St'], 'country': ['USA'], 'last_checked': ['Checked 142 minutes ago']
            })
    
    def create_widgets(self):
        btn_frame = ctk.CTkFrame(self, corner_radius=10)
        btn_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(btn_frame, text="CONSULTAS COMPLEJAS", 
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        
        # Grid de botones
        queries = [
            ("1. Locales activos por estado", self.query_1),
            ("2. Top 5 ciudades con más locales", self.query_2),
            ("3. Porcentaje de locales dañados", self.query_3),
            ("4. Promedio de lat/lon por estado", self.query_4),
            ("5. Locales verificados en última hora", self.query_5),
            ("6. Estados con solo locales working", self.query_6),
            ("7. Ciudades con más de 3 locales", self.query_7),
            ("8. Distribución dot por estado", self.query_8),
            ("9. Locales por patrón de calle", self.query_9),
            ("10. Estados ordenados por actividad", self.query_10)
        ]
        
        for i, (text, command) in enumerate(queries):
            row, col = i // 2, i % 2
            btn = ctk.CTkButton(btn_frame, text=text, command=command, 
                                width=280, height=45, font=ctk.CTkFont(size=12))
            btn.grid(row=row, column=col, padx=10, pady=8)
        
        result_frame = ctk.CTkFrame(self, corner_radius=10)
        result_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        header_frame = ctk.CTkFrame(result_frame)
        header_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(header_frame, text="RESULTADOS DE LA CONSULTA", 
                     font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=10)
        
        self.status_label = ctk.CTkLabel(header_frame, text="Seleccione una consulta", 
                                         font=ctk.CTkFont(size=12), text_color="gray")
        self.status_label.pack(side="right", padx=10)
        
        self.setup_treeview(result_frame)
        
    def setup_treeview(self, parent):
        table_frame = ctk.CTkFrame(parent)
        table_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical")
        hsb = ttk.Scrollbar(table_frame, orient="horizontal")
        
        self.tree = ttk.Treeview(table_frame, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
    def clear_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree['columns'] = ()
        self.tree['show'] = 'tree'
    
    def show_result(self, data, columns, title):
        self.clear_treeview()
        self.status_label.configure(text=f"{title} - {len(data)} registros", text_color="green")
        
        self.tree['columns'] = columns
        self.tree['show'] = 'headings'
        
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=120, minwidth=80)
        
        for row in data:
            self.tree.insert("", "end", values=row)
        
    def query_1(self):
        """Locales activos por estado"""
        active_by_state = self.df[self.df['is_active'] == True].groupby('state').size().reset_index()
        active_by_state.columns = ['Estado', 'Locales Activos']
        data = active_by_state.values.tolist()
        self.show_result(data, ['Estado', 'Locales Activos'], "Consulta 1: Locales Activos por Estado")
    
    def query_2(self):
        """Top 5 ciudades con más locales"""
        top_cities = self.df.groupby('city').size().reset_index(name='count').nlargest(5, 'count')
        top_cities.columns = ['Ciudad', 'Cantidad de Locales']
        data = top_cities.values.tolist()
        self.show_result(data, ['Ciudad', 'Cantidad de Locales'], "Consulta 2: Top 5 Ciudades")
    
    def query_3(self):
        """Porcentaje de locales dañados"""
        total = len(self.df)
        broken = len(self.df[self.df['is_broken'] == True])
        pct = (broken / total * 100) if total > 0 else 0
        data = [["Locales Dañados", broken], ["Locales Activos", total - broken], 
                ["Total Locales", total], ["Porcentaje Dañado", f"{pct:.2f}%"]]
        self.show_result(data, ['Concepto', 'Valor'], "Consulta 3: Porcentaje de Locales Dañados")
    
    def query_4(self):
        """Promedio de lat/lon por estado"""
        avg_lat_lon = self.df.groupby('state').agg({'lat': 'mean', 'lon': 'mean'}).round(6).reset_index()
        avg_lat_lon.columns = ['Estado', 'Latitud Promedio', 'Longitud Promedio']
        data = avg_lat_lon.values.tolist()
        self.show_result(data, ['Estado', 'Latitud Promedio', 'Longitud Promedio'], "Consulta 4: Promedio Lat/Lon por Estado")
    
    def query_5(self):
        """Locales verificados en última hora"""
        def get_minutes_ago(last_checked):
            try:
                parts = last_checked.split()
                if len(parts) >= 3 and parts[1] == 'minutes':
                    return int(parts[0])
                return 999
            except:
                return 999
        
        self.df['minutes_ago'] = self.df['last_checked'].apply(get_minutes_ago)
        recent = self.df[self.df['minutes_ago'] <= 60].copy()
        recent = recent[['city', 'state', 'street', 'last_checked', 'minutes_ago']]
        recent.columns = ['Ciudad', 'Estado', 'Calle', 'Última Verificación', 'Minutos']
        data = recent.values.tolist()
        self.show_result(data, ['Ciudad', 'Estado', 'Calle', 'Última Verificación', 'Minutos'], 
                        "Consulta 5: Locales Verificados en Última Hora")
    
    def query_6(self):
        """Estados con solo locales working"""
        state_dot = self.df.groupby('state')['dot'].nunique().reset_index()
        only_working = state_dot[state_dot['dot'] == 1]
        only_working_valid = []
        for state in only_working['state']:
            if (self.df[self.df['state'] == state]['dot'] == 'working').all():
                only_working_valid.append([state])
        self.show_result(only_working_valid, ['Estado'], "Consulta 6: Estados con solo locales 'working'")
    
    def query_7(self):
        """Ciudades con más de 3 locales"""
        city_counts = self.df.groupby('city').size().reset_index(name='count')
        cities = city_counts[city_counts['count'] > 3].sort_values('count', ascending=False)
        cities.columns = ['Ciudad', 'Cantidad de Locales']
        data = cities.values.tolist()
        self.show_result(data, ['Ciudad', 'Cantidad de Locales'], "Consulta 7: Ciudades con más de 3 locales")
    
    def query_8(self):
        """Distribución de dot (estado del local) por estado"""
        pivot = pd.crosstab(self.df['state'], self.df['dot']).reset_index()
        data = pivot.values.tolist()
        columns = ['Estado'] + list(pivot.columns[1:])
        self.show_result(data, columns, "Consulta 8: Distribución de 'dot' por Estado")
    
    def query_9(self):
        """Locales cuyo nombre de calle contiene patrón específico"""
        # Buscar calles con "St", "Ave", "Blvd"
        pattern = '|'.join(['St', 'Ave', 'Blvd', 'Street', 'Avenue', 'Boulevard'])
        filtered = self.df[self.df['street'].str.contains(pattern, case=False, na=False)]
        result = filtered[['city', 'state', 'street']].head(20)
        result.columns = ['Ciudad', 'Estado', 'Calle']
        data = result.values.tolist()
        self.show_result(data, ['Ciudad', 'Estado', 'Calle'], "Consulta 9: Calles con patrón (St, Ave, Blvd, etc.)")
    
    def query_10(self):
        """Estados ordenados por porcentaje de locales activos"""
        total_by_state = self.df.groupby('state').size().reset_index(name='total')
        active_by_state = self.df[self.df['is_active'] == True].groupby('state').size().reset_index(name='active')
        merged = total_by_state.merge(active_by_state, on='state', how='left').fillna(0)
        merged['pct_active'] = (merged['active'] / merged['total'] * 100).round(2)
        merged = merged.sort_values('pct_active', ascending=False)
        merged.columns = ['Estado', 'Total Locales', 'Locales Activos', '% Activos']
        data = merged.values.tolist()
        self.show_result(data, ['Estado', 'Total Locales', 'Locales Activos', '% Activos'], 
                        "Consulta 10: Estados ordenados por porcentaje de actividad")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Consultas - McDonald's Locations")
        self.geometry("1300x800")
        self.minsize(1000, 600)
        self.login_frame = LoginFrame(self, self.on_login)
        self.login_frame.pack(fill="both", expand=True)
        self.query_frame = None
        
    def on_login(self):
        self.login_frame.pack_forget()
        self.query_frame = QueryFrame(self, self)
        self.query_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()