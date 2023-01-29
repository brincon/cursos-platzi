from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMateral = []

    def __init__(self, license, driver, typeCarAccepted, seatsMateral):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMateral = seatsMateral

    def setPassenger(self, passegengerNum):
        super().setPassenger(passegengerNum)
        if passegengerNum >=6:
            self.__passegenger = int(passegengerNum)
        else:
            print("Necesita asignar 6 pasajeros")