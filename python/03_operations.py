set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union con funcion
set_c = set_a.union(set_b)
print(set_c)

# Union con operador
print(set_a | set_b)

# Interseccion con funcion y operador
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# Diferencia
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# Diferencia simetrica, es una unión sin los elementos que tienen en común
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
