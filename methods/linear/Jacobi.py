import numpy as np

def jacobi_metodo(n_dimension, a_lista, b_lista, tolerancia, max_iter):
    a = np.array(a_lista).astype(float)
    b = np.array(b_lista).astype(float).flatten()

    x_jacobi = np.zeros(n_dimension)
    error_relativo = 1.0

    diagonal_a = np.diag(a)
        
    if np.any(diagonal_a == 0):
        return "Error: Hay ceros en la diagonal principal. El método no puede continuar.", ""

    r = a - np.diag(diagonal_a)


    for k in range(max_iter):
        x_prev = x_jacobi.copy()

        x_jacobi = (b - np.dot(r, x_jacobi)) / diagonal_a

        if np.linalg.norm(x_jacobi) != 0:
            error_relativo = np.linalg.norm(x_jacobi - x_prev) / np.linalg.norm(x_jacobi)
        else:
            error_relativo = 1.0
        
        results = np.array2string(x_jacobi, formatter={'float_kind': lambda x: f"{x:.6f}"})

        if error_relativo < tolerancia:
            return f"El error relativo ({error_relativo:.6f}) es menor a la tolerancia ({tolerancia}).", results
        
    if error_relativo >= tolerancia:
        return f"Se alcanzó el máximo de {max_iter} iteraciones sin llegar a la tolerancia deseada.", results
    
