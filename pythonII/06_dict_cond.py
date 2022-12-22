# diccionarios con condicionales
import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country : population for (country, population) in population_v2.items() if population > 40}
print(result)

# Ejemplo 2

text = "Hola, soy brenda"
unique = {i:i.upper() for i in text if i in 'aeiou'}
print(unique)

# contando la frecuencia
unique = {i:text.count(i) for i in text if i in 'aeiou'}
print(unique)

