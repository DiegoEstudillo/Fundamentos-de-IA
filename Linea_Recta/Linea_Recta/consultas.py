import numpy as np

def generar_datos_grafica(m_str, b_str, rango=10):
    try:
        m_str = m_str.replace(',', '.')
        b_str = b_str.replace(',', '.')

        m = float(m_str)
        b = float(b_str)

        x_vals = np.linspace(-rango, rango, 400)
        y_vals = m * x_vals + b

        return x_vals, y_vals, None
    except ValueError:
        return None, None, "Error: 'm' y 'b' deben ser números válidos.\nUsar punto (.) o coma (,) para decimales."
    except Exception as e:
        return None, None, f"Error inesperado: {str(e)}"