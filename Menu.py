from Items.Apples import Apples
from Items.Bread import Bread
from Items.Milk import Milk
from Items.Soup import Soup


class Menu:

    # menu list
    def display_menu(self):
        print("/////////////////////////////////////////////////////////")
        print("\nTo add soup type: Soup.")
        print("To add bread type: Bread.")
        print("To add milk type: Milk.")
        print("To add apples type: Apples.")

    def selected_item(self, item):
        if item == 'Soup':
            return Soup()
        elif item == 'Bread':
            return Bread()
        elif item == 'Milk':
            return Milk()
        elif item == 'Apples':
            return Apples()
        else:
            return None

