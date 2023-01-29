from account import Account

class Car:
    id = int
    license = str
    driver = Account("", "")
    passegenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver

    def setPassenger(self, passegengerNum):
        if passegengerNum >=4:
            self.__passegenger = int(passegengerNum)
        else:
            print("Necesita asignar 4 pasajeros")

    def getPassenger(self):
        if self.__passegenger != int:
            print(self.__passegenger)

