import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

intentos_ej6 = []
numero_correcto_ej6 = None

# ejercicio 4
def validar_ejercicio4():
    try:
        num = int(entry_ej4.get())
        if num < 10:
            lbl_resultado_ej4.config(text=f"Número correcto: {num}")
            messagebox.showinfo("Ejercicio 4 - Éxito", f"Número válido: {num}")
        else:
            messagebox.showerror("Ejercicio 4 - Error", "El número debe ser menor que 10")
            lbl_resultado_ej4.config(text=f"{num} es incorrecto, intente de nuevo")
            entry_ej4.delete(0, tk.END)
            entry_ej4.focus()
    except:
        messagebox.showerror("Ejercicio 4 - Error", "Ingrese un número entero válido")
        entry_ej4.delete(0, tk.END)
        entry_ej4.focus()

def limpiar_ejercicio4():
    entry_ej4.delete(0, tk.END)
    lbl_resultado_ej4.config(text="")

# ejercicio 5
def validar_rango(num):
    return 0 < num < 20

def validar_ejercicio5():
    try:
        num = int(entry_ej5.get())
        if validar_rango(num):
            lbl_resultado_ej5.config(text=f"Número correcto: {num}")
            messagebox.showinfo("Ejercicio 5 - Éxito", f"Número válido: {num} dentro del rango (0,20)")
        else:
            messagebox.showerror("Ejercicio 5 - Error", "El número debe estar entre 0 y 20 (sin incluir los extremos)")
            lbl_resultado_ej5.config(text=f"{num} está fuera del rango")
            entry_ej5.delete(0, tk.END)
            entry_ej5.focus()
    except:
        messagebox.showerror("Ejercicio 5 - Error", "Ingrese un número entero válido")
        entry_ej5.delete(0, tk.END)
        entry_ej5.focus()

def limpiar_ejercicio5():
    entry_ej5.delete(0, tk.END)
    lbl_resultado_ej5.config(text="")

# ejercicio 6
def validar_rango_ej6(num):
    return 0 < num < 20

def verificar_ejercicio6():
    global numero_correcto_ej6
    try:
        num = int(entry_ej6.get())
        intentos_ej6.append(num)
        
        if validar_rango_ej6(num):
            numero_correcto_ej6 = num
            incorrectos = len([n for n in intentos_ej6 if not validar_rango_ej6(n)])
            
            historial_texto = "\n".join([f"Intento {i+1}: {n}" for i, n in enumerate(intentos_ej6)])
            
            lbl_resultado_ej6.config(
                text=f"Número correcto: {numero_correcto_ej6}\n"
                     f"Total de intentos: {len(intentos_ej6)}\n"
                     f"Intentos incorrectos: {incorrectos}\n\n"
                     f"Historial de intentos:\n{historial_texto}"
            )
            messagebox.showinfo("Ejercicio 6 - Éxito", 
                              f"Número válido: {numero_correcto_ej6}\n"
                              f"Intentos totales: {len(intentos_ej6)}\n"
                              f"Incorrectos: {incorrectos}")
            entry_ej6.config(state="disabled")
        else:
            messagebox.showerror("Ejercicio 6 - Error", f"Número {num} fuera del rango (0,20)")
            lbl_estado_ej6.config(text=f"Intento {len(intentos_ej6)}: {num} - Incorrecto")
            entry_ej6.delete(0, tk.END)
            entry_ej6.focus()
    except:
        messagebox.showerror("Ejercicio 6 - Error", "Ingrese un número entero válido")
        entry_ej6.delete(0, tk.END)
        entry_ej6.focus()

def reiniciar_ejercicio6():
    global intentos_ej6, numero_correcto_ej6
    intentos_ej6 = []
    numero_correcto_ej6 = None
    entry_ej6.delete(0, tk.END)
    entry_ej6.config(state="normal")
    lbl_estado_ej6.config(text="")
    lbl_resultado_ej6.config(text="")
    messagebox.showinfo("Ejercicio 6", "Se reinició la validación")
    entry_ej6.focus()


def abrir():
    global entry_ej4, lbl_resultado_ej4, entry_ej5, lbl_resultado_ej5
    global entry_ej6, lbl_estado_ej6, lbl_resultado_ej6, intentos_ej6, numero_correcto_ej6

    intentos_ej6 = []
    numero_correcto_ej6 = None

    ventana = tk.Tk()
    ventana.title("Validaciones")
    ventana.geometry("400x500")

    tk.Label(ventana, text="Validaciones", font=("Arial", 14)).pack(pady=10)
    frame_ej4 = tk.LabelFrame(ventana, text="Ejercicio 4", padx=10, pady=10)
    frame_ej4.pack(fill="x", padx=10, pady=5)

    tk.Label(frame_ej4, text="Número < 10:").grid(row=0, column=0, padx=5, pady=5)
    entry_ej4 = tk.Entry(frame_ej4, width=15)
    entry_ej4.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_ej4, text="Validar", command=validar_ejercicio4).grid(row=0, column=2, padx=5, pady=5)

    lbl_resultado_ej4 = tk.Label(frame_ej4, text="", fg="blue")
    lbl_resultado_ej4.grid(row=1, column=0, columnspan=3, pady=5)
    frame_ej5 = tk.LabelFrame(ventana, text="Ejercicio 5", padx=10, pady=10)
    frame_ej5.pack(fill="x", padx=10, pady=5)

    tk.Label(frame_ej5, text="Número (0,20):").grid(row=0, column=0, padx=5, pady=5)
    entry_ej5 = tk.Entry(frame_ej5, width=15)
    entry_ej5.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_ej5, text="Validar", command=validar_ejercicio5).grid(row=0, column=2, padx=5, pady=5)
    lbl_resultado_ej5 = tk.Label(frame_ej5, text="", fg="blue")
    lbl_resultado_ej5.grid(row=1, column=0, columnspan=3, pady=5)

    frame_ej6 = tk.LabelFrame(ventana, text="Ejercicio 6", padx=10, pady=10)
    frame_ej6.pack(fill="x", padx=10, pady=5)
    tk.Label(frame_ej6, text="Número (0,20):").grid(row=0, column=0, padx=5, pady=5)
    entry_ej6 = tk.Entry(frame_ej6, width=15)
    entry_ej6.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_ej6, text="Validar", command=verificar_ejercicio6).grid(row=0, column=2, padx=5, pady=5)
    lbl_estado_ej6 = tk.Label(frame_ej6, text="", fg="orange")
    lbl_estado_ej6.grid(row=1, column=0, columnspan=3, pady=5)
    lbl_resultado_ej6 = tk.Label(frame_ej6, text="", fg="green", justify="left")
    lbl_resultado_ej6.grid(row=2, column=0, columnspan=3, pady=5)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)

    entry_ej4.focus()

    ventana.mainloop()