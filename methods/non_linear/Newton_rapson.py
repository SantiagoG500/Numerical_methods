import sympy as sp

def newton_raphson(funcion_str, x0, tolerancia, max_iteraciones):
    # Definimos la variable simbólica
    x = sp.symbols('x')
    
    # Convertimos el string de la función a una expresión de sympy
    f = sp.sympify(funcion_str)
    
    # Calculamos la derivada automáticamente
    df = sp.diff(f, x)
    
    # Convertimos las expresiones en funciones numéricas rápidas (lambdify)
    f_num = sp.lambdify(x, f)
    df_num = sp.lambdify(x, df)
    
    print(f"{'Iteración':<12} | {'xn':<15} | {'f(xn)':<15} | {'Error':<15}")
    print("-" * 65)
    
    xn = x0
    for i in range(max_iteraciones):
        fxn = f_num(xn)
        dfxn = df_num(xn)
        
        # Evitar división por cero
        if abs(dfxn) < 1e-15:
            print("Error: La derivada es demasiado cercana a cero. El método no puede continuar.")
            return None
        
        # Fórmula de Newton-Raphson: x_{n+1} = x_n - f(x_n) / f'(x_n)
        x_siguiente = xn - fxn / dfxn
        error = abs(x_siguiente - xn)
        
        print(f"{i+1:<12} | {xn:<15.8f} | {fxn:<15.8e} | {error:<15.8e}")
        
        # Verificamos si alcanzamos la precisión deseada
        if error < tolerancia:
            print("-" * 65)
            print(f"Raíz encontrada: {x_siguiente:.10f} con un error de {error:.10e}")
            return x_siguiente
        
        xn = x_siguiente
        
    print("-" * 65)
    print("Se alcanzó el máximo de iteraciones sin llegar a la tolerancia.")
    return xn

# --- Configuración del ejercicio ---
# Ejemplo: f(x) = x^2 - 2 (para encontrar raíz de 2)
funcion_usuario = "x**3 - 4*x - 9"
valor_inicial = 3.0
precision = 1e-5
maximo_pasos = 30

newton_raphson(funcion_usuario, valor_inicial, precision, maximo_pasos)