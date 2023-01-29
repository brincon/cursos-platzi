from car import Car
from account import Account
from uberX import UberX
from uberVan import UberVan

if __name__ == "__main__":
    print("Hola mundo")
    # car = Car("AMS123", Account("Andres Herrera", "ANDA876"))
    # #car.license = "AMS234"
    # #car.driver = "Andres Herrera"
    # print(vars(car))
    # print(vars(car.driver))

    #car2 = Car()
    #car2.license = "QWE567"
    #car2.driver = "Marta"
    #print(vars(car2))

    car2 = UberX("ASC123", "Andres H", "Chevrolet", "Spark")
    car2.setPassenger(2)
    print(vars(car2))

    car3 = UberVan("ASC123", "Andres G", "Chevrolet", "Spark")
    car3.setPassenger(5)
    print(vars(car3))