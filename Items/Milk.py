class Milk:

    def __init__(self):
        self.current_price = 1.30
        self.id = 'Milk'
        self.discount = False
        self.price = 1.30

    def __repr__(self):
        return f"{self.id} - {self.current_price}€"
