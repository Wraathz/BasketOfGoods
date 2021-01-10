class Apples:

    def __init__(self):
        self.current_price = 1.00
        self.id = 'Apples'
        self.discount = False
        self.price = 1.00

    def apply_discount(self, discount):
        self.discount = True
        return self.price * discount

    def __repr__(self):
        return f"{self.id} - {self.current_price}€"

