import tkinter as tk
from tkinter import messagebox, ttk

trabajadores = []

def calcular_aumento(sueldo):
    if sueldo < 4000:
        return sueldo * 0.15
    elif sueldo <= 7000:
        return sueldo * 0.10
    else:
        return sueldo * 0.08

def registrar():
    try:
        nombre = entry_nombre.get()
        sueldo = float(entry_sueldo.get())
        if sueldo <= 0:
            raise ValueError
        aumento = calcular_aumento(sueldo)
        nuevo_sueldo = sueldo + aumento
        trabajadores.append((nombre, sueldo, nuevo_sueldo))
        messagebox.showinfo("Éxito", f"Aumento: {aumento:.2f}\nNuevo sueldo: {nuevo_sueldo:.2f}")
        entry_nombre.delete(0, tk.END)
        entry_sueldo.delete(0, tk.END)
        actualizar_historial()
    except:
        messagebox.showerror("Error", "Ingrese datos válidos")

def actualizar_historial():
    for row in tree.get_children():
        tree.delete(row)
    for t in trabajadores:
        tree.insert("", tk.END, values=t)

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_nombre, entry_sueldo, tree
    ventana = tk.Tk()
    ventana.title("Ejercicio 1 - Aumento de sueldos")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Sueldo básico:").grid(row=1, column=0, padx=5, pady=5)
    entry_sueldo = tk.Entry(ventana)
    entry_sueldo.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=2, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=3, column=0, columnspan=2, pady=5)

    tree = ttk.Treeview(ventana, columns=("Nombre", "Sueldo", "Nuevo"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Sueldo", text="Sueldo")
    tree.heading("Nuevo", text="Nuevo Sueldo")
    tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    ventana.mainloop()