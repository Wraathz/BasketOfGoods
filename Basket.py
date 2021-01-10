class Basket:

    def __init__(self):
        self.items = []

    def __repr__(self):
        basket_string_repr = ""

        basket_string_repr += "-------------------------------\n"
        basket_string_repr += "Basket has the following items:\n"
        for item in self.items:
            basket_string_repr += f"{repr(item)}\n"
        basket_string_repr += f"Subtotal: €{'{:.2f}'.format(self.subtotal())}\n"
        basket_string_repr += f"Total: €{'{:.2f}'.format(self.total())}\n"
        return basket_string_repr

    def add_item(self, item):
        self.items.append(item)

    def get_first_item(self, item):
        curr_item = None
        for item in self.items:
            if item.id == item:
                curr_item = item
        return curr_item


    def total(self):
        total = 0
        for i in self.items:
            total += i.current_price
        return total

    def subtotal(self):
        subtotal = 0
        for i in self.items:
            subtotal += i.price
        return subtotal

    def count(self, item):
        count = 0
        for k in self.items:
            if k.id == item:
                count += 1
        return count

    def count_with_discount(self, item):
        count = 0
        for k in self.items:
            if k.id == item and k.discount:
                count += 1
        return count

