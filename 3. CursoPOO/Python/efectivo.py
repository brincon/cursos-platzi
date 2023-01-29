from payment import Payment

class Efectivo():
    id = int
    number = int
    cvv = str
    date = str

    def __init__(self, id, number):
        self.id = id
        self.number = number

