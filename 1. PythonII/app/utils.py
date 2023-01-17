def get_population(country_dic):
    population_dict = {
    "2022" : int(country_dic['2022 Population']),
    "2020" : int(country_dic['2020 Population']),
    "2015" : int(country_dic['2015 Population']),
    "2010" : int(country_dic['2010 Population']),
    "2000" : int(country_dic['2000 Population']),
    "1990" : int(country_dic['1990 Population']),
    "1980" : int(country_dic['1980 Population']),
    "1970" : int(country_dic['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    
    return labels, values

#A = "Hola"

def population_by_country(data, country):
    result = list(filter(lambda item: item["Country/Territory"] == country, data))
    return result

def get_percentil(country_dic):
    perc_population = {}
    for pais in country_dic:
        perc_population[pais["Country/Territory"]] = pais["World Population Percentage"] 

    # otra forma con comprehension
    # percentages_dict = {
    #     item["Country/Territory"]: item["World Population Percentage"] for item in country_dic}
    # labels = percentages_dict.keys()
    # values = percentages_dict.values()
    
    labels = perc_population.keys()
    values = perc_population.values()
    print(perc_population)
    return labels, values

# import read_csv
# data = read_csv.read_csv("./data.csv")
# get_percentil(data)