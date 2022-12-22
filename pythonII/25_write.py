# r+ permisos de lectura y escritura
# w+ sobreescribe el archivo
with open("./text.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("nuevas cosas en este archivo\n")
    file.write("otra linea\n")
    file.write("otra\n")

