class Shop:
    def __init__(self, menu, basket):
        self.menu = menu
        self.basket = basket

    def run(self):
        print("Welcome to our shop! Take a look at our menu.")
        while True:
            self.display_menus()
            option = self.retrieve_input()
            if option == 'q':
                print(repr(self.basket))
                print("Come back again! Poggers")
                break
            elif option == 'b':
                print(repr(self.basket))
            else:
                selected_item = self.menu.selected_item(option)
                if selected_item is None:
                    print("Select a valid option.")
                else:
                    if selected_item.id == 'Apples':
                        selected_item.current_price = selected_item.price - selected_item.apply_discount(0.10)
                    elif selected_item.id == 'Bread' or selected_item.id == 'Soup':
                        self.calc_if_applyable_discount(selected_item)

                    self.basket.add_item(selected_item)
                    print(f"{selected_item.id} was added to the basket.")

    def display_menus(self):
        self.menu.display_menu()
        self.menu2()

    def retrieve_input(self):
        return input("\nWhat will your option be? \n")

    def menu2(self):
        print("To view basket type: b ")
        print("To leave store type: q ")

    def calc_if_applyable_discount(self, selected_item):
        if selected_item.id == 'Soup':
            bread_with_discount = self.basket.count_with_discount('Bread')
            bread_with_no_discount = self.basket.count('Bread') - bread_with_discount
            soup_count = self.basket.count('Soup')
            soups_left_for_discount = soup_count - (bread_with_discount * 2)

            if bread_with_no_discount > 0:
                if soups_left_for_discount >= 1:
                    for item in self.basket.items:
                        if item.id == 'Bread' and not item.discount:
                            item.current_price = item.price - item.apply_discount(0.50)
                            break

        elif selected_item.id == 'Bread':
            soup_count = self.basket.count('Soup')
            bread_with_discount = self.basket.count_with_discount('Bread')
            soups_left_for_discount = soup_count - (bread_with_discount * 2)

            if soups_left_for_discount >= 2:
                selected_item.current_price = selected_item.price -selected_item.apply_discount(0.50)
