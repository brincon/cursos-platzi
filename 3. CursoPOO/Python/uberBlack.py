from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMateral = []

    def __init__(self, license, driver, typeCarAccepted, seatsMateral):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMateral = seatsMateral