import tkinter as tk
from tkinter import messagebox

numeros = []
suma = 0

def agregar():
    global suma
    try:
        num = int(entry_num.get())
        numeros.append(num)
        suma += num
        lbl_parcial.config(text=f"Suma parcial: {suma}")
        entry_num.delete(0, tk.END)
        if suma > 100:
            messagebox.showinfo("Límite superado", f"Números: {numeros}\nCantidad: {len(numeros)}\nSuma final: {suma}")
            ventana.destroy()
    except:
        messagebox.showerror("Error", "Ingrese un número entero")

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_num, lbl_parcial, ventana, numeros, suma
    numeros = []
    suma = 0
    
    ventana = tk.Tk()
    ventana.title("Ejercicio 9 - Suma hasta límite")

    tk.Label(ventana, text="Ingrese números:").grid(row=0, column=0, padx=5, pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Agregar", command=agregar).grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=2, column=0, columnspan=2, pady=5)

    lbl_parcial = tk.Label(ventana, text="Suma parcial: 0", font=("Arial", 10))
    lbl_parcial.grid(row=3, column=0, columnspan=2, pady=10)

    ventana.mainloop()