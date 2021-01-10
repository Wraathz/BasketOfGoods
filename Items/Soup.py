class Soup:

    def __init__(self):
        self.price = 0.65
        self.id = 'Soup'
        self.discount = False
        self.current_price = 0.65

    def __repr__(self):
        return f"{self.id} - {self.current_price}€"

