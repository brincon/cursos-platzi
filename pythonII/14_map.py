# la función principal de map es hacer transformaciones
# a una lista de elementos
numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i*2)

print(numbers)
print(numbers_v2)

# La misma transformación con la función map
numbers_v3 = list(map(lambda i: i*2, numbers))
print(numbers_v3)

# Transformación con dos listas de diferentes tamaños se obtiene
# el largo de la lista más pequeña
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

