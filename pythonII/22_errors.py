# error de sintaxis
#print(0/0))

# error por la división en cero
#print(0/0)

# error nameError, variables que no existe
#print(result)

# Error assertionError, una función no esta funcionana como debería
suma = lambda x, y: x + y
# suma = lambda x, y: x + (y * 2)
assert suma(2,2) == 4

# lanzar nuestro propio error
age = 10
if age < 18:
    raise Exception("No se permite menores de edad")







