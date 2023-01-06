import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        #print(header) #Se obtiene el encabezado
        data = []
        for row in reader:
            iterable = zip(header, row)
            #print(list(iterable)) # lista de los encabezados y cada fila
            # country_dict = {key: value for key, value in iterable}
            country_dict = dict(iterable) # otra forma de convertir a un diccionario
            data.append(country_dict) # se agrega a una lista el diccionario
            #print(country_dict)
        return data

            # print("***" * 5)
            # print(row)

if __name__ == "__main__":
    data = read_csv("./app/data.csv")
    print(data[0])