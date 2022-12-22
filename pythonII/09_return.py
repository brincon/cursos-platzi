# Funciones con parámetros por defecto
def find_volume(length=1, width=1, depth=1):
    return length * width * depth

result = find_volume()
print(result)

result = find_volume(10, 20, 3)
print(result)


def find_volume1(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

result, width, text = find_volume1(width=10)
print(result)
print(width)
print(text) 