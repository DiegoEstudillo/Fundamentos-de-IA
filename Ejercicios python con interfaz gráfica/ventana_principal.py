import tkinter as tk
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4_5_6
import ejercicio7
import ejercicio8
import ejercicio9
import ejercicio10

def abrir():
    ventana = tk.Tk()
    ventana.title("Menú Principal")

    tk.Label(ventana, text="Menú Principal", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Button(ventana, text="Ejercicio 1 - Aumento de sueldos", width=35, command=ejercicio1.abrir).grid(row=1, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 2 - Parque de diversiones", width=35, command=ejercicio2.abrir).grid(row=2, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 3 - Descuentos por mes", width=35, command=ejercicio3.abrir).grid(row=3, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 4,5,6 - Validaciones", width=35, command=ejercicio4_5_6.abrir).grid(row=4, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 7 - Suma de n números", width=35, command=ejercicio7.abrir).grid(row=5, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 8 - Suma acumulativa", width=35, command=ejercicio8.abrir).grid(row=6, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 9 - Suma hasta límite", width=35, command=ejercicio9.abrir).grid(row=7, column=0, columnspan=2, pady=2)
    tk.Button(ventana, text="Ejercicio 10 - Pago de trabajadores", width=35, command=ejercicio10.abrir).grid(row=8, column=0, columnspan=2, pady=2)

    tk.Button(ventana, text="Cerrar", width=20, command=ventana.destroy).grid(row=9, column=0, columnspan=2, pady=10)

    ventana.mainloop()