import numpy as np

print("--- CONFIGURACIÓN DEL SISTEMA ---")
n = int(input("Ingresa el tamaño del sistema (ej. 3 para 3x3): "))

# 1. ENTRADA DE DATOS DIRECTA (Sin SymPy)
A_lista = []
print("\n--- INGRESO DE LA MATRIZ A ---")
print("Nota: Ingresa los valores de la matriz que cumpla la diagonal dominante")
for i in range(n):
    fila = []
    for j in range(n):
        # Convertimos la entrada de texto directamente a float
        valor = float(input(f"Ingresa el valor para A[{i+1}][{j+1}]: "))
        fila.append(valor)
    A_lista.append(fila)

b_lista = []
print("\n--- INGRESO DEL VECTOR b ---")
for i in range(n):
    valor = float(input(f"Ingresa el valor para b[{i+1}]: "))
    b_lista.append(valor)

tolerancia = float(input("\nIngresa el error de tolerancia (ej. 0.0001): "))
iteraciones = int(input("\n¿Cuántas iteraciones quieres calcular?: "))

print("\n==================================")
print("INICIANDO CÁLCULO CON NUMPY")
print("==================================")

# 2. PROCESAMIENTO MATRICIAL
A = np.array(A_lista)
b = np.array(b_lista)
x_jacobi = np.zeros(n)

diagonal_A = np.diag(A)
R = A - np.diag(diagonal_A)

# 3. BUCLE DE ITERACIONES
for k in range(iteraciones):
    # GUARDAMOS el estado anterior antes del cálculo
    x_anterior = x_jacobi.copy() 
    
    # [AQUÍ VA TU CÁLCULO VECTORIZADO DE JACOBI]
    x_jacobi = (b - np.dot(R, x_jacobi)) / diagonal_A
    
    # CÁLCULO DEL ERROR RELATIVO
    # np.linalg.norm calcula la magnitud del vector (distancia)
    if np.linalg.norm(x_jacobi) != 0: # Evitar división por cero en la primera iteración
        error_relativo = np.linalg.norm(x_jacobi - x_anterior) / np.linalg.norm(x_jacobi)
    else:
        error_relativo = 1.0 # Si es 0, asignamos un error alto inicial

    resultados_formateados = np.array2string(x_jacobi, formatter={'float_kind':lambda x: f"{x:.6f}"})
    print(f"Iteración {k+1}: x = {resultados_formateados} | Error: {error_relativo:.6f}")
    
    # CONDICIÓN DE PARADA
    if error_relativo < tolerancia:
        print(f"\nEl método paró por CONVERGENCIA en la iteración {k+1}.")
        print(f"El error relativo ({error_relativo:.6f}) es menor a la tolerancia ({tolerancia}).")
        break
    
if error_relativo >= tolerancia:
    print(f"\n⚠️ El método paró por LÍMITE DE ITERACIONES.")
    print(f"Se alcanzó el máximo de {iteraciones} iteraciones sin llegar a la tolerancia deseada.")

print("==================================")