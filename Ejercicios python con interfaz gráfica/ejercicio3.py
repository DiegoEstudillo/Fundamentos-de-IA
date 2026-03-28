import tkinter as tk
from tkinter import messagebox, ttk

compras = []

def calcular_descuento(mes, importe):
    desc = 0
    if mes.lower() == "octubre":
        desc = 0.15
    elif mes.lower() == "diciembre":
        desc = 0.20
    elif mes.lower() == "julio":
        desc = 0.10
    return importe * desc

def registrar():
    try:
        nombre = entry_nombre.get()
        mes = entry_mes.get()
        importe = float(entry_importe.get())
        if importe <= 0:
            raise ValueError
        descuento = calcular_descuento(mes, importe)
        total = importe - descuento
        compras.append((nombre, mes, importe, total))
        messagebox.showinfo("Total", f"Descuento: {descuento:.2f}\nTotal a pagar: {total:.2f}")
        entry_nombre.delete(0, tk.END)
        entry_mes.delete(0, tk.END)
        entry_importe.delete(0, tk.END)
        actualizar_historial()
    except:
        messagebox.showerror("Error", "Datos inválidos")

def actualizar_historial():
    for row in tree.get_children():
        tree.delete(row)
    total_vendido = 0
    for c in compras:
        tree.insert("", tk.END, values=c)
        total_vendido += c[3]
    lbl_total.config(text=f"Total vendido en el día: S/. {total_vendido:.2f}")

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_nombre, entry_mes, entry_importe, tree, lbl_total
    ventana = tk.Tk()
    ventana.title("Ejercicio 3 - Descuentos por mes")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Mes:").grid(row=1, column=0, padx=5, pady=5)
    entry_mes = tk.Entry(ventana)
    entry_mes.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Importe:").grid(row=2, column=0, padx=5, pady=5)
    entry_importe = tk.Entry(ventana)
    entry_importe.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=3, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=4, column=0, columnspan=2, pady=5)

    tree = ttk.Treeview(ventana, columns=("Nombre", "Mes", "Importe", "Total"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Mes", text="Mes")
    tree.heading("Importe", text="Importe")
    tree.heading("Total", text="Total a pagar")
    tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    lbl_total = tk.Label(ventana, text="Total vendido en el día: S/. 0.00")
    lbl_total.grid(row=6, column=0, columnspan=2, pady=5)

    ventana.mainloop()