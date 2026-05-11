
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

# Configuración para permitir sintaxis flexible (ej: 2x, x^2)
transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

def biseccion_metodo(f, a, b, tol, max_iter):
    x = sp.symbols('x')
    expresion = parse_expr(f, transformations=transformaciones)

    f = sp.lambdify(x, expresion)

    iteracion = 0
    c_prev = None
    
    if f(a) * f(b) >= 0:
        raise ValueError("f(a)·f(b) debe ser < 0. El intervalo no contiene una raíz.")


    fa, fb = f(a), f(b)

    if fa * fb >= 0:
        return "Error: f(a)·f(b) debe ser < 0. Verifique el intervalo."

    resultados = []

    while iteracion < max_iter:
        iteracion += 1
        c = (a + b) / 2.0
        fc = f(c)

        if c_prev is not None:
            error_rel = abs((c - c_prev) / c) if c != 0 else abs(c - c_prev)
        else:
            error_rel = abs(b - a)

        resultados.append((iteracion, a, b, c, fc, error_rel))

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        c_prev = c

    print("Límite de iteraciones alcanzado.")
    raiz_final = (a + b) / 2.0

    if error_rel < tol:
        return f"Convergencia alcanzada, raíz: {raiz_final}", resultados
    else:
        return f"Final de iteraciones alcanzado, raíz aproximada: {raiz_final}", resultados
