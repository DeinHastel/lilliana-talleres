import numpy as np

# Crear un array NumPy tridimensional
array_tridimensional = np.array([  [[1, 2, 3]  ,  [4, 5, 6]]  ,  [[7, 8, 9]  ,  [10, 11, 12]]  ])

# Acceder a elementos en un array tridimensional
elemento = array_tridimensional[0, 1, 2]  # Acceder al valor 6 (primer nivel: 0, segundo nivel: 1, tercer nivel: 2)

# Modificar un elemento en el array
array_tridimensional[1, 0, 1] = 99  # Cambiar el valor de 8 a 99

# Forma del array tridimensional
forma = array_tridimensional.shape  # Devuelve (2, 2, 3) ya que hay 2 niveles en el primer nivel, 2 niveles en el segundo nivel y 3 elementos en el tercer nivel

# Sumar todos los elementos en el array
suma_total = np.sum(array_tridimensional)
print(array_tridimensional)