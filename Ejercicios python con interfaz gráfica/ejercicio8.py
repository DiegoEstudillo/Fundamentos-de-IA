import tkinter as tk
from tkinter import messagebox

numeros = []
suma_acumulada = 0

def agregar():
    global suma_acumulada
    try:
        num = int(entry_num.get())
        if num == 0:
            finalizar()
            return
        numeros.append(num)
        suma_acumulada += num
        lbl_acumulado.config(text=f"Suma acumulada: {suma_acumulada}")
        entry_num.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Ingrese un número entero")

def finalizar():
    messagebox.showinfo("Resultado", f"Números: {numeros}\nCantidad: {len(numeros)}\nSuma total: {suma_acumulada}")
    ventana.destroy()

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_num, lbl_acumulado, ventana, numeros, suma_acumulada
    numeros = []
    suma_acumulada = 0
    
    ventana = tk.Tk()
    ventana.title("Ejercicio 8 - Suma acumulativa")

    tk.Label(ventana, text="Ingrese números (0 para terminar):").grid(row=0, column=0, padx=5, pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Agregar", command=agregar).grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=2, column=0, columnspan=2, pady=5)

    lbl_acumulado = tk.Label(ventana, text="Suma acumulada: 0", font=("Arial", 10))
    lbl_acumulado.grid(row=3, column=0, columnspan=2, pady=10)

    ventana.mainloop()