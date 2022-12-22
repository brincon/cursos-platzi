dict1 = {}
for i in range(1, 5):
    dict1[i] = i * 2

print(dict1)

dic_v2 = {i: i * 2 for i in range(1, 5)}
print(dic_v2)

# Dividir la iteración a partir de una lista
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)

print(population)

population_v2 = {country: random.randint(1, 100) for country in countries}

print(population_v2)

# iterar dos listas y a partir de esa el diccionario

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))
print(dict(zip(names, ages)))
# el zip da una lista con tuplas, por eso el for se hace con tuplas
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

# forma clásica
new_dict= {}
for i in range(len(names)):
  new_dict[names[i]] = ages[i]

print(new_dict)

# Forma clásica con dictionary comprehension
new_dict = {names[i]: ages[i] for i in range(len(names))}
print(new_dict)
