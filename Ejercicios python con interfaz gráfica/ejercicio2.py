import tkinter as tk
from tkinter import messagebox, ttk

visitantes = []
PRECIO_JUEGO = 50

def calcular_total(edad, juegos):
    total = juegos * PRECIO_JUEGO
    if edad < 10:
        total *= 0.75
    elif edad <= 17:
        total *= 0.90
    return total

def registrar():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        juegos = int(entry_juegos.get())
        if edad <= 0 or juegos < 0:
            raise ValueError
        total = calcular_total(edad, juegos)
        visitantes.append((nombre, edad, juegos, total))
        messagebox.showinfo("Total a pagar", f"{nombre}, total: S/. {total:.2f}")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_juegos.delete(0, tk.END)
        actualizar_historial()
    except:
        messagebox.showerror("Error", "Ingrese datos válidos")

def actualizar_historial():
    for row in tree.get_children():
        tree.delete(row)
    total_recaudado = 0
    for v in visitantes:
        tree.insert("", tk.END, values=v)
        total_recaudado += v[3]
    lbl_total.config(text=f"Total recaudado: S/. {total_recaudado:.2f}")

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_nombre, entry_edad, entry_juegos, tree, lbl_total
    ventana = tk.Tk()
    ventana.title("Ejercicio 2 - Parque de diversiones")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
    entry_edad = tk.Entry(ventana)
    entry_edad.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Juegos usados:").grid(row=2, column=0, padx=5, pady=5)
    entry_juegos = tk.Entry(ventana)
    entry_juegos.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=3, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=4, column=0, columnspan=2, pady=5)

    tree = ttk.Treeview(ventana, columns=("Nombre", "Edad", "Juegos", "Total"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Edad", text="Edad")
    tree.heading("Juegos", text="Juegos")
    tree.heading("Total", text="Total S/.")
    tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    lbl_total = tk.Label(ventana, text="Total recaudado: S/. 0.00")
    lbl_total.grid(row=6, column=0, columnspan=2, pady=5)

    ventana.mainloop()