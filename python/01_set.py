set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

# Conjunto con números/valores repetidos no los imprime
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

# Un conjunto a partir de un string, como la o se repite al pasarlo 
# a un conjunto se elimina
set_from_string = set('hoola')
print(set_from_string)

# Un conjunto a partir de una tupla
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# Un conjunto a partir de una lista, si se transforma solo se queda 
# con los valores únicos
numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)

# si necesito esos valores únicos en una lista se vuelve a transformar
unique_numbers = list(set_numbers
)