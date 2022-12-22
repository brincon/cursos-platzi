set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

# Preguntar por un elemento especifico
print('col' in set_countries)
print('pe' in set_countries)

# agregar elementos al conjunto
set_countries.add('pe')
print(set_countries)

set_countries.add('pe')
print(set_countries)

# Update o actualizar
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove o eliminar
set_countries.remove('col')
print(set_countries)

# remover un elemento que no existe lanza error
#set_countries.remove('arg')
set_countries.remove('ar')
print(set_countries)

# elimina un elemento y si no lo encuentra no falla el programa
set_countries.discard('ar')

set_countries.add('arg')
print(set_countries)

# Se borra todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))
