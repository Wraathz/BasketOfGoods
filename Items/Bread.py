class Bread:

    def __init__(self):
        self.current_price = 0.80
        self.id = 'Bread'
        self.discount = False
        self.price = 0.80

    def apply_discount(self, discount):
        self.discount = True
        return self.price * discount

    def __repr__(self):
        return f"{self.id} - {self.current_price}€"
