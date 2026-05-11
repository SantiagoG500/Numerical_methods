import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

# Configuración para permitir sintaxis flexible (ej: 2x, x^2)
transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

def newton_raphson_metodo(fx_str, x0, tolerancia, max_iter):
    try:
        # --- PREPARACIÓN SIMBÓLICA ---
        x = sp.symbols('x')

        if '=' in fx_str:
            return "Error: ingresa la función como expresión, no como ecuación. Ej: 'x-3' en vez de 'x=3'", []
    

        expresion = parse_expr(fx_str, transformations=transformaciones)
        
        # Derivada automática
        derivada_expr = sp.diff(expresion, x)
        
        # Convertir a funciones numéricas para mayor velocidad
        f = sp.lambdify(x, expresion)
        df = sp.lambdify(x, derivada_expr)

        resultados = []
        xn = x0

        for iteracion in range(1, max_iter + 1):
            val_f = f(xn)
            val_df = df(xn)

            # Evitar división por cero (derivada nula)
            if abs(val_df) < 1e-15:
                return f"Error: La derivada en {xn} es cero. El método no puede continuar.", []

            # Fórmula de Newton-Raphson
            x_siguiente = xn - (val_f / val_df)
            
            # Cálculo del error relativo
            if x_siguiente != 0:
                error_rel = abs((x_siguiente - xn) / x_siguiente)
            else:
                error_rel = abs(x_siguiente - xn)

            resultados.append((iteracion, xn, val_f, val_df, error_rel))

            # --- CRITERIOS DE PARADA ---
            if error_rel < tolerancia:
                return f"Convergencia alcanzada. Raíz: {x_siguiente}", resultados

            xn = x_siguiente

        return f"Se alcanzó el límite de {max_iter} iteraciones. Última aproximación: {xn}", resultados

    except Exception as e:
        return f"Error en los datos: {e}. Asegúrese de usar una función válida.", []
