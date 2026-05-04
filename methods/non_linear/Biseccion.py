
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

# Configuración para permitir sintaxis flexible (ej: 2x, x^2)
transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

def biseccion_interactivo():
    print("========================================")
    print("   MÉTODO DE BISECCIÓN (V2)")
    print("========================================\n")

    try:
        # --- ENTRADAS INTERACTIVAS ---
        fx_str    = input("Ingrese la función f(x): ")
        a         = float(input("Ingrese el extremo izquierdo del intervalo (a): "))
        b         = float(input("Ingrese el extremo derecho del intervalo (b): "))
        tolerancia = float(input("Ingrese el error relativo permitido: "))
        max_iter  = int(input("Ingrese el máximo de iteraciones: "))

        # --- PREPARACIÓN SIMBÓLICA ---
        x = sp.symbols('x')
        expresion = parse_expr(fx_str, transformations=transformaciones)

        # Convertir a función numérica para mayor velocidad
        f = sp.lambdify(x, expresion)

        # --- VALIDACIÓN DEL INTERVALO ---
        fa, fb = f(a), f(b)
        if fa * fb >= 0:
            print(f"\n[!] Error: f(a)·f(b) debe ser < 0.")
            print(f"    f({a}) = {fa:.6f}   f({b}) = {fb:.6f}")
            print("    Verifique que el intervalo contenga una raíz.")
            return

        print("\n--- INICIO DEL PROCESO ---")
        print(f"{'Iter':<5} | {'a':<12} | {'b':<12} | {'c (raíz)':<14} | {'f(c)':<12} | {'Error Rel.':<12}")
        print("-" * 78)

        c_prev    = None
        iteracion = 0

        while True:
            iteracion += 1

            c  = (a + b) / 2.0
            fc = f(c)

            # Cálculo del error relativo
            if c_prev is not None:
                if c != 0:
                    error_rel = abs((c - c_prev) / c)
                else:
                    error_rel = abs(c - c_prev)
            else:
                error_rel = abs(b - a)          # primera iteración: ancho del intervalo

            print(f"{iteracion:<5} | {a:<12.6f} | {b:<12.6f} | {c:<14.8f} | {fc:<12.2e} | {error_rel:<12.6f}")

            # --- CRITERIOS DE PARADA ---
            if error_rel < tolerancia:
                print("-" * 78)
                print(f"[✓] Convergencia alcanzada.")
                print(f"Resultado final (Raíz): {c}")
                break

            if iteracion >= max_iter:
                print("-" * 78)
                print(f"[!] Se alcanzó el límite de {max_iter} iteraciones.")
                print(f"Última aproximación: {c}")
                break

            # Actualización del intervalo
            c_prev = c
            if f(a) * fc < 0:
                b = c
            else:
                a = c

    except Exception as e:
        print(f"\n[!] Error en los datos: {e}")
        print("Asegúrese de usar una función válida.")

if __name__ == "__main__":
    biseccion_interactivo()