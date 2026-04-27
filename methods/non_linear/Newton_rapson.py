import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

# Configuración para permitir sintaxis flexible (ej: 2x, x^2)
transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

def newton_raphson_interactivo():
    print("========================================")
    print("   MÉTODO DE NEWTON-RAPHSON (V2)")
    print("========================================\n")

    try:
        # --- ENTRADAS INTERACTIVAS ---
        fx_str = input("Ingrese la función f(x): ")
        x0 = float(input("Ingrese el valor inicial (x0): "))
        tolerancia = float(input("Ingrese el error relativo permitido: "))
        max_iter = int(input("Ingrese el máximo de iteraciones: "))

        # --- PREPARACIÓN SIMBÓLICA ---
        x = sp.symbols('x')
        expresion = parse_expr(fx_str, transformations=transformaciones)
        
        # Derivada automática
        derivada_expr = sp.diff(expresion, x)
        
        # Convertir a funciones numéricas para mayor velocidad
        f = sp.lambdify(x, expresion)
        df = sp.lambdify(x, derivada_expr)

        print("\n--- INICIO DEL PROCESO ---")
        print(f"{'Iter':<5} | {'xn':<12} | {'f(xn)':<12} | {'Error Rel.':<12}")
        print("-" * 55)

        xn = x0
        iteracion = 0

        while True:
            iteracion += 1
            
            val_f = f(xn)
            val_df = df(xn)

            # Evitar división por cero (derivada nula)
            if abs(val_df) < 1e-15:
                print(f"Error: La derivada en {xn} es cero. El método no puede continuar.")
                break

            # Fórmula de Newton-Raphson
            x_siguiente = xn - (val_f / val_df)
            
            # Cálculo del error relativo
            if x_siguiente != 0:
                error_rel = abs((x_siguiente - xn) / x_siguiente)
            else:
                error_rel = abs(x_siguiente - xn)

            print(f"{iteracion:<5} | {xn:<12.6f} | {val_f:<12.2e} | {error_rel:<12.6f}")

            # --- CRITERIOS DE PARADA ---
            if error_rel < tolerancia:
                print("-" * 55)
                print(f"[✓] Convergencia alcanzada.")
                print(f"Resultado final (Raíz): {x_siguiente}")
                break

            if iteracion >= max_iter:
                print("-" * 55)
                print(f"[!] Se alcanzó el límite de {max_iter} iteraciones.")
                print(f"Última aproximación: {x_siguiente}")
                break

            # Actualización para la siguiente vuelta
            xn = x_siguiente

    except Exception as e:
        print(f"\n[!] Error en los datos: {e}")
        print("Asegúrese de usar una función válida.")

if __name__ == "__main__":
    newton_raphson_interactivo()