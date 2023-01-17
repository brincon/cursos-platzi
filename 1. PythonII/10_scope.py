price = 100 # variable global

def increment():
    price = 10 # variable local, solo dentro de la función
    price = price + 10
    print(price)
    return price

print(price)
price_2 = increment()
print(price_2)

# Ejemplo con dos variables locales
def increment():
    price = 10 # variable local, solo dentro de la función
    result = price + 10 # varianle local, solo dentro de la función
    print(result)
    return result

print(price)
price_2 = increment()
print(price_2)