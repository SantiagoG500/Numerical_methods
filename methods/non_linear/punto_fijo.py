import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

def punto_fijo_metodo(gx, x0, tolerance, max_iter):
    x = sp.symbols('x')
    g_expr = parse_expr(gx, transformations=transformaciones)

    iteracion = 0
    resultados = []

    while iteracion < max_iter:
        iteracion += 1
        
        x_new = float(g_expr.subs(x, x0))
        error = abs(x_new - x0)
        
        resultados.append((iteracion, x_new, error))
        
        # Actualización
        x0 = x_new
        
        if error < tolerance:
            return f"\n[✓] Convergencia alcanzada por tolerancia. Error: {error}", resultados
        
        if iteracion >= max_iter:
            return f"\n[!] Proceso detenido por límite de iteraciones ({max_iter}).", resultados
            

