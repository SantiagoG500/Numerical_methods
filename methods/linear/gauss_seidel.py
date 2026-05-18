import numpy as np

def gauss_seidel_metodo(n_dimension, a_lista, b_lista, tolerancia, max_iter):

    """
    Implementa el método iterativo de Gauss-Seidel para resolver sistemas de ecuaciones lineales Ax = b.

    Este método es una variante del método de Jacobi que utiliza los valores más recientes
    de las variables en cada iteración, lo que generalmente acelera la convergencia.
    Requiere que la matriz A sea diagonalmente dominante para garantizar convergencia.

    Parámetros:
    -----------
    - `n_dimesion` : int
        Dimensión del sistema (tamaño n x n de la matriz A).
    - `a_lista` : list of lists
        Matriz de coeficientes A representada como lista de listas (n x n).
        Debe ser diagonalmente dominante para convergencia.
    - `b_lista` : list
        Vector de términos independientes b (tamaño n).
    - `tolerancia` : float
        Tolerancia para el criterio de convergencia (error relativo).
    - `max_iter` : int
        Número máximo de iteraciones permitidas.

    Retorna:
    --------
    `tuple`
        Una tupla con dos elementos:
        - str: Mensaje indicando si convergió o alcanzó el máximo de iteraciones.
        - str: Representación formateada del vector solución x con 6 decimales.

    Notas:
    ------
    - El método itera hasta max_iter o hasta que el error relativo sea menor que tolerancia.
    - El error relativo se calcula como `||x_k - x_{k-1}|| / ||x_k||`.
    - Si el vector solución es cero, se asigna error_rel = 1.0 para evitar división por cero.
    """
    
    # Matrix processing
    try:
        a = np.array(a_lista, dtype=float)
        b = np.array(b_lista, dtype=float).flatten()  # Ensure b is 1D
        x_gauss = np.zeros(n_dimension, dtype=float)
        
        # Validate dimensions
        if a.shape != (n_dimension, n_dimension):
            raise ValueError(f"La matriz A debe ser de dimensión {n_dimension}x{n_dimension}")
        if b.shape[0] != n_dimension:
            raise ValueError(f"El vector b debe tener dimensión {n_dimension}")
            
    except (ValueError, TypeError) as e:
        return f"Error en los datos de entrada: {str(e)}", "[]"

    resultados_arr = []
    for k in range(max_iter):
        x_prev = x_gauss.copy()

        for i in range(n_dimension):
            if abs(a[i, i]) < 1e-12:  # Check for near-zero diagonal elements
                return f"Error: Elemento diagonal A[{i+1}][{i+1}] es cero o muy cercano a cero", "[]"
            suma = np.dot(a[i], x_gauss) - (a[i, i] * x_gauss[i])
            x_gauss[i] = (b[i] - suma) / a[i, i]

        if np.linalg.norm(x_gauss) != 0:
            err_rel = np.linalg.norm(x_gauss - x_prev) / np.linalg.norm(x_gauss)
        else:
            err_rel = 1.0

        resultados_formateados = np.array2string(x_gauss, formatter={'float_kind': lambda x: f"{x:.6f}"})
        resultados_arr.append(( k+1, resultados_formateados, err_rel ))

        if err_rel < tolerancia:
            resultados = np.array2string(x_gauss, formatter={'float_kind': lambda x: f"{x:.6f}"})
            return f"El error relativo ({err_rel:.6f}) es menor a la tolerancia ({tolerancia})", resultados_arr

    # resultados = np.array2string(x_gauss, formatter={'float_kind': lambda x: f"{x:.6f}"})
    return f"Se alcanzó el máximo de iteraciones {max_iter} sin llegar a la tolerancia deseada", resultados_arr
