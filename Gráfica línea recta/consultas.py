import numpy as np

def validar_rango(m_str, b_str, min_val=-100, max_val=100):
    try:
        m_str = m_str.replace(',', '.')
        b_str = b_str.replace(',', '.')
        
        m = float(m_str)
        b = float(b_str)
        
        errores = []
        
        if m < min_val or m > max_val:
            errores.append(f"'m' = {m} está fuera del rango ({min_val} a {max_val})")
        
        if b < min_val or b > max_val:
            errores.append(f"'b' = {b} está fuera del rango ({min_val} a {max_val})")
        
        if errores:
            return False, " | ".join(errores) + \
                   f"\nPor favor, ingrese valores entre {min_val} y {max_val}."
        
        return True, ""
        
    except ValueError:
        return False, "Error: Los valores deben ser números válidos."

def generar_datos_grafica(m_str, b_str, rango=100):
    try:
        m_str = m_str.replace(',', '.')
        b_str = b_str.replace(',', '.')

        m = float(m_str)
        b = float(b_str)

        x_vals = np.linspace(-rango, rango, 500)
        y_vals = m * x_vals + b

        return x_vals, y_vals, None
        
    except ValueError:
        return None, None, "Error: 'm' y 'b' deben ser números válidos.\nUse punto (.) o coma (,) para decimales."
    except Exception as e:
        return None, None, f"Error inesperado: {str(e)}"