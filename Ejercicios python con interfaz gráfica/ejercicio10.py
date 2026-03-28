import tkinter as tk
from tkinter import messagebox, ttk

trabajadores = []

def calcular_pago(horas_normales, pago_hora, horas_extras, hijos):
    normal = horas_normales * pago_hora
    extra = horas_extras * (pago_hora * 1.5)
    bono = hijos * 0.5 * pago_hora
    total = normal + extra + bono
    return normal, extra, bono, total

def registrar():
    try:
        nombre = entry_nombre.get()
        horas_n = float(entry_horas_n.get())
        pago_h = float(entry_pago_h.get())
        horas_e = float(entry_horas_e.get())
        hijos = int(entry_hijos.get())
        if horas_n < 0 or pago_h <= 0 or horas_e < 0 or hijos < 0:
            raise ValueError
        normal, extra, bono, total = calcular_pago(horas_n, pago_h, horas_e, hijos)
        trabajadores.append((nombre, normal, extra, bono, total))
        messagebox.showinfo("Pago", f"Pago normal: {normal:.2f}\nPago extra: {extra:.2f}\nBono: {bono:.2f}\nTotal: {total:.2f}")
        entry_nombre.delete(0, tk.END)
        entry_horas_n.delete(0, tk.END)
        entry_pago_h.delete(0, tk.END)
        entry_horas_e.delete(0, tk.END)
        entry_hijos.delete(0, tk.END)
        actualizar_historial()
    except:
        messagebox.showerror("Error", "Datos inválidos")

def actualizar_historial():
    for row in tree.get_children():
        tree.delete(row)
    for t in trabajadores:
        tree.insert("", tk.END, values=t)

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_nombre, entry_horas_n, entry_pago_h, entry_horas_e, entry_hijos, tree
    ventana = tk.Tk()
    ventana.title("Ejercicio 10 - Pago de trabajadores")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Horas normales:").grid(row=1, column=0, padx=5, pady=5)
    entry_horas_n = tk.Entry(ventana)
    entry_horas_n.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Pago por hora:").grid(row=2, column=0, padx=5, pady=5)
    entry_pago_h = tk.Entry(ventana)
    entry_pago_h.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Horas extras:").grid(row=3, column=0, padx=5, pady=5)
    entry_horas_e = tk.Entry(ventana)
    entry_horas_e.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Número de hijos:").grid(row=4, column=0, padx=5, pady=5)
    entry_hijos = tk.Entry(ventana)
    entry_hijos.grid(row=4, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Registrar", command=registrar).grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=6, column=0, columnspan=2, pady=5)

    tree = ttk.Treeview(ventana, columns=("Nombre", "Normal", "Extra", "Bono", "Total"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Normal", text="Normal")
    tree.heading("Extra", text="Extra")
    tree.heading("Bono", text="Bono")
    tree.heading("Total", text="Total")
    tree.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    ventana.mainloop()