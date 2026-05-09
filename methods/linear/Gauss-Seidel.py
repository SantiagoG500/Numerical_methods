import numpy as np

print("--- CONFIGURACIÓN DEL SISTEMA ---")
n = int(input("Ingresa el tamaño del sistema (ej. 3 para 3x3): "))

# 1. ENTRADA DE DATOS
A_lista = []
print("\n--- INGRESO DE LA MATRIZ A ---")
print("Nota: Ingresa los valores de la matriz que cumpla la diagonal dominante")
for i in range(n):
    fila = []
    for j in range(n):
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
print("INICIANDO CÁLCULO GAUSS-SEIDEL")
print("==================================")

# 2. PROCESAMIENTO MATRICIAL
A = np.array(A_lista)
b = np.array(b_lista)
x_gauss = np.zeros(n)

# 3. BUCLE DE ITERACIONES
for k in range(iteraciones):
    
    # 1. GUARDAMOS el vector actual ANTES de empezar a modificarlo en esta iteración
    x_anterior = x_gauss.copy()
    
    # En Gauss-Seidel, calculamos ecuación por ecuación (fila por fila)
    for i in range(n):
        # np.dot(A[i], x_gauss) multiplica toda la fila 'i' por el vector 'x' actual.
        # Como x_gauss se está actualizando en este mismo instante, los elementos 
        # anteriores a 'i' ya tienen los valores nuevos de esta iteración.
        
        # Le restamos el valor de la diagonal (A[i][i] * x_gauss[i]) porque ese es 
        # el que estamos intentando despejar.
        suma = np.dot(A[i], x_gauss) - (A[i, i] * x_gauss[i])
        
        # Actualizamos la variable directamente. ¡El próximo paso del bucle ya usará este nuevo valor!
        x_gauss[i] = (b[i] - suma) / A[i, i]
    
    # 2. CÁLCULO DEL ERROR RELATIVO (Se hace fuera del bucle 'i', cuando ya se actualizó todo 'x')
    if np.linalg.norm(x_gauss) != 0:
        error_relativo = np.linalg.norm(x_gauss - x_anterior) / np.linalg.norm(x_gauss)
    else:
        error_relativo = 1.0 # Asignamos un error alto si el vector es [0,0,0] para evitar división por cero
        
    # Imprimimos los resultados de la iteración completa incluyendo el error
    resultados_formateados = np.array2string(x_gauss, formatter={'float_kind':lambda x: f"{x:.6f}"})
    print(f"Iteración {k+1}: x = {resultados_formateados} | Error: {error_relativo:.6f}")

    # 3. CONDICIÓN DE PARADA DENTRO DEL BUCLE
    if error_relativo < tolerancia:
        print(f"\n✅ El método paró por CONVERGENCIA en la iteración {k+1}.")
        print(f"El error relativo ({error_relativo:.6f}) es menor a la tolerancia ({tolerancia}).")
        break

# 4. VALIDACIÓN FUERA DEL BUCLE (Sin indentación)
# Si el bucle termina normalmente sin hacer 'break', verificamos si no alcanzó la tolerancia
if error_relativo >= tolerancia:
    print(f"\n⚠️ El método paró por LÍMITE DE ITERACIONES.")
    print(f"Se alcanzó el máximo de {iteraciones} iteraciones sin llegar a la tolerancia deseada.")

print("==================================")