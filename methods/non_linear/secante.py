import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

def secante_metodo(fx, x_i, x_j, relative_error, max_iter):
    x = sp.symbols('x')
    expresion = parse_expr(fx, transformations=transformaciones)

    fxi = float(expresion.subs(x, x_i))
    fxj = float(expresion.subs(x, x_j))

    iteracion = 0
    resultados = []

    while True:
        iteracion += 1
        
        if (fxj - fxi) == 0:
            print("Error: División por cero.")
            break

        x_k = x_i - ((fxi * (x_j - x_i)) / (fxj - fxi))
        relative_x_k = abs((x_k - x_i) / x_k)
        
        resultados.append((iteracion, x_k, relative_x_k))

        if relative_x_k < relative_error:
            return f"\nResultado final (Raiz): {x_k}", resultados
        
        if iteracion >= max_iter:
            return f"\nResultado final (Raiz): {x_k}", resultados
            
        x_j = x_i
        x_i = x_k
        fxi = float(expresion.subs(x, x_i))
        fxj = float(expresion.subs(x, x_j))

    return f"\nResultado final (Raiz): {x_k}", resultados





# # --- ENTRADAS ---
# fx = input("Ingrese la funcion: ")
# x_i = float(input("Ingrese el valor de Xi: "))
# x_j = float(input("Ingrese el valor de Xi-1: "))
# relative_error = float(input("Ingrese el valor del error relativo permitido: "))
# max_iter = int(input("Ingrese el numero maximo de iteraciones: ")) # Nueva entrada

# x = sp.symbols('x')
# expresion = parse_expr(fx, transformations=transformaciones)

# fxi = float(expresion.subs(x, x_i))
# fxj = float(expresion.subs(x, x_j))

# # --- INICIALIZACIÓN ---
# iteracion = 0 # Contador que empieza en cero

# print("\n--- INICIO DEL PROCESO ---")
# print(f"{'Iter':<5} | {'X_i+1':<12} | {'Error Rel.':<12}")
# print("-" * 35)

# while True:
#     iteracion += 1 # Sumamos una iteración al empezar el ciclo
    
#     # Evitar división por cero
#     if (fxj - fxi) == 0:
#         print("Error: División por cero.")
#         break

#     x_k = x_i - ((fxi * (x_j - x_i)) / (fxj - fxi))
#     relative_x_k = abs((x_k - x_i) / x_k)
    
#     # Imprimimos con formato para que se vea ordenado
#     print(f"{iteracion:<5} | {x_k:<12.6f} | {relative_x_k:<12.6f}")
    
#     # --- CRITERIOS DE PARADA ---
#     # 1. Si ya convergió por error
#     if relative_x_k < relative_error:
#         print(f"\n[✓] Convergencia alcanzada por error relativo.")
#         break
    
#     # 2. Si ya se alcanzó el máximo de iteraciones
#     if iteracion >= max_iter:
#         print(f"\n[!] Proceso detenido por límite de iteraciones ({max_iter}).")
#         break
        
#     # Actualizaciones
#     x_j = x_i
#     x_i = x_k
#     fxi = float(expresion.subs(x, x_i))
#     fxj = float(expresion.subs(x, x_j))

# print(f"\nResultado final (Raiz): {x_k}")
