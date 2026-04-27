import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

# --- ENTRADAS ---
gx = input("Ingrese la funcion g(x): ")
x0 = float(input("Ingrese el valor inicial x0: "))
tolerance = float(input("Ingrese el valor de la tolerancia: "))
max_iter = int(input("Ingrese el numero maximo de iteraciones: "))

x = sp.symbols('x')
g_expr = parse_expr(gx, transformations=transformaciones)

# --- INICIALIZACIÓN ---
iteracion = 0

print("\n--- INICIO DEL PROCESO ---")
print(f"{'Iter':<5} | {'X_{i+1}':<12} | {'Error Abs.':<12}")
print("-" * 40)

while True:
    iteracion += 1
    
    x_new = float(g_expr.subs(x, x0))
    error = abs(x_new - x0)
    
    print(f"{iteracion:<5} | {x_new:<12.6f} | {error:<12.6f}")
    
    # --- CRITERIOS DE PARADA ---
    if error < tolerance:
        print(f"\n[✓] Convergencia alcanzada por tolerancia.")
        break
    
    if iteracion >= max_iter:
        print(f"\n[!] Proceso detenido por límite de iteraciones ({max_iter}).")
        break
        
    # Actualización
    x0 = x_new

print(f"\nResultado final (Punto fijo): {x_new}")


