# Se abre el archivo
file = open("./text.txt")

# Lee todo el archivo
#print(file.read())

# Lee linea por linea
# print(file.readline())
# print(file.readline())

# se lee el archivo linea a linea sin ocupar mucha memoria
for line in file:
    print(line)

# Se cierra el archivo
file.close()

# para abrir y cerrar el archivo de forma automatica
with open("./text.txt") as file:
    for line in file:
        print(line)

