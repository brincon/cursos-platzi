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

def add_taxes_v2(item):
    new_items = item.copy()
    new_items['taxes'] = new_items['price'] * .19
    return new_items

new_items_v2 = list(map(add_taxes_v2, items))
print("New list")
print(new_items_v2)
print("Old list")
print(items)

