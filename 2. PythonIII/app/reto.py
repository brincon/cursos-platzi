import read_csv

lista = read_csv.read_csv("./data.csv")

#print(lista[2])

new_list = []

for clave in lista:
    [clave.pop(key) for key in ["Rank", "CCA3", "Capital", "Continent", 'Area (kmÂ²)', "Density (per kmÂ²)", "Growth Rate", "World Population Percentage"]]

for newClave in lista:
    newClave["Country"] = newClave.pop("Country/Territory")
    newClave["2022"] = newClave.pop('2022 Population')
    newClave["2020"] = newClave.pop('2020 Population')
    newClave["2015"] = newClave.pop('2015 Population')
    newClave["2010"] = newClave.pop('2010 Population')
    newClave["2000"] = newClave.pop('2000 Population')
    newClave["1990"] = newClave.pop('1990 Population')
    newClave["1980"] = newClave.pop('1980 Population')
    newClave["1970"] = newClave.pop('1970 Population')


print(lista[2])




