from Menu import Menu
from Menu2 import Menu2
from Goods import Goods

# list of items
## goods = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples': 1.00}
## print("/////////////////////////////////////////////////////////")
## print("Welcome! Please choose from our goods: \n{}".format(goods))
## checkout = []
goods = Goods()


# initiation variables
total = 0.00
percentage = 0.10


# menu list
run = Menu().menu()


while True:

    # Soup
    if run == 'Soup':
        subtotal = goods['Soup']
        checkout.append('Soup')

        print("/////////////////////////////////////////////////////////")
        print("\nSoup added to the basket.")
        run2 = Menu2().menu2()

        if run2 == 'Yes':
            total = total + subtotal
            run = Menu().menu()
        elif run2 == 'No':
            total = "{:.2f}".format(total + subtotal)
            print("/////////////////////////////////////////////////////////")
            print("\nCheckout: " + str(checkout))
            print("Subtotal: €" + str(total))
            print("Total: €" + str(total))

            break
        else:
            print("Please enter a suitable option.")

    # Bread
    elif run == 'Bread':
        count = checkout.count('Soup')
        # if count in checkout == 2:
        if count == 2:
            subtotal = goods['Bread'] / 2

        else:
            subtotal = goods['Bread']
            checkout.append('Bread')

        print("/////////////////////////////////////////////////////////")
        print("Bread added to basket.")
        run2 = Menu2().menu2()

        if run2 == 'Yes':
            total = total + subtotal
            run = Menu().menu()
        elif run2 == 'No':
            total = "{:.2f}".format(total + subtotal)

            print("/////////////////////////////////////////////////////////")

            print("\nCheckout: " + str(checkout))
            print("Subtotal: €" + str(total))
            print("Total: €" + str(total))

            break
        else:
            print("Please enter a suitable option.")

    # Milk
    elif run == 'Milk':
        subtotal = goods['Milk']
        checkout.append('Milk')

        print("/////////////////////////////////////////////////////////")
        print("Milk added to basket.")
        run2 = Menu2().menu2()

        if run2 == 'Yes':
            total = total + subtotal
            run = Menu().menu()
        elif run2 == 'No':
            total = "{:.2f}".format(total + subtotal)

            print("/////////////////////////////////////////////////////////")
            print("\nCheckout: " + str(checkout))
            print("Subtotal: €" + str(total))
            print("Total: €" + str(total))

            break
        else:
            print("Please enter a suitable option.")

    # Apples
    elif run == 'Apples':
        subtotal = goods['Apples']
        checkout.append('Apples')

        print("/////////////////////////////////////////////////////////")
        print("Apples added to basket.")
        run2 = Menu2().menu2()

        if run2 == 'Yes':
            total = total + subtotal
            run = Menu().menu()
        elif run2 == 'No':
            total = "{:.2f}".format(total + subtotal)

            print("/////////////////////////////////////////////////////////")
            print("\nCheckout: " + str(checkout))
            print("Subtotal: €" + str(total) + " Apples 10% off: -€0.10")

            total = float(float(total) - percentage)
            total = "{:.2f}".format(total)
            print("Total: €" + str(total))

            break
        else:
            print("Please enter a suitable option.")

    # PriceBasket
    elif run == 'PriceBasket':
        print("\nCheckout: " + str(checkout))
        print("Subtotal: €" + str(total))
        run = Menu().menu()

    # Q (Quit)
    elif run == 'Q':
        count = checkout.count('Apples')
        if count == 1:
            print("\nCheckout: " + str(checkout))
            print("Subtotal: €" + str(total) + " Apples 10% off: -€0.10")
            total = float(float(total) - percentage)
            total = "{:.2f}".format(total)
            print("Your total is: €" + str(total))
            break

        else:
            print("Checkout: " + str(checkout))
            print("Your total is: " + str(total))
            break

    else:
        print("\nPlease enter a suitable option.")
        run = Menu().menu()

print("Good-bye for now!")
