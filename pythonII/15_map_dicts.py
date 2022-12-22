items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

"""
def add_taxes_v1(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes_v1, items))
print("New list")
print(new_items)
print("Old list")
print(items)
"""

# Notar que se modificó la lista original y esto no debería pasar.
# Esto sucede porque cuando se trabaja con diccionarios se asigna
# una referencia en memoria, y cuando se hace una modificación se
# hace para el array original comno el nuevo, pues los dos comparten
# la misma referencia en memoria

# Para corregirlo se cambia la función
def add_taxes_v2(item):
    new_items = item.copy()
    new_items['taxes'] = new_items['price'] * .19
    return new_items

new_items_v2 = list(map(add_taxes_v2, items))
print("New list")
print(new_items_v2)
print("Old list")
print(items)

