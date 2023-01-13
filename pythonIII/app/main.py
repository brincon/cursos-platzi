import utils
import read_csv
import charts
import pandas as pd

# data = [
#         {
#             "Country": "Colombia",
#             "population": 500
#         },
#         {
#             "Country": "Bolivia",
#             "population": 300
#         }
#     ]

def run():
    '''
    # opción del profesor
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    
    '''

    df = pd.read_csv("data.csv")
    df = df[df['Continent'] == 'Africa']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pi_chart(countries, percentages)

    data = read_csv.read_csv("./data.csv")
    country = input("Type Country ==> ")
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country["Country/Territory"], labels, values)
    

    # labels, values = utils.get_percentil(data)
    # charts.generate_pi_chart(labels, values)



# le dice al archivo que si se ejecuta desde la terminar ejecute la función
# pero si es ejecutado desde otro archivo no se va a ejecutar
if __name__ == "__main__":
    run()