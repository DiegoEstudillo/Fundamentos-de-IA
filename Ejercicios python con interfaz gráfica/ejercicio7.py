import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError
        suma = 0
        secuencia = []
        for i in range(1, n+1):
            suma += i
            secuencia.append(str(i))
        lbl_resultado.config(text=f"Secuencia: {' + '.join(secuencia)} = {suma}")
    except:
        messagebox.showerror("Error", "Ingrese un número entero positivo")

def cerrar(ventana):
    ventana.destroy()

def abrir():
    global entry_n, lbl_resultado
    ventana = tk.Tk()
    ventana.title("Ejercicio 7 - Suma de n números")

    tk.Label(ventana, text="Ingrese n:").grid(row=0, column=0, padx=5, pady=5)
    entry_n = tk.Entry(ventana)
    entry_n.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Calcular", command=calcular).grid(row=1, column=0, columnspan=2, pady=5)
    tk.Button(ventana, text="Cerrar", command=lambda: cerrar(ventana)).grid(row=2, column=0, columnspan=2, pady=5)

    lbl_resultado = tk.Label(ventana, text="", font=("Arial", 10))
    lbl_resultado.grid(row=3, column=0, columnspan=2, pady=10)

    ventana.mainloop()