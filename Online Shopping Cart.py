# Online Shopping Cart

#Class and Object
#__init__() constructor
#Methods
#Lists
#Dictionaries
#for and while loops
#if-elif-else
#Exception handling
#Adding/removing items
#Total calculation
#Checkout process

class Shoppingcart:

    def __init__(self):
        self.products = []

    # Add product tp cart
    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")

        try:
            price = float(input("Enter Product Price: $:"))
            quantity = int(input("Enter Quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be greater than 0.")
                return

        except ValueError:
            print("Please enter valid price and quantity.")
            return

        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.products.append(product)

        print("Product Added Successfully.")

    # Display cart
    def display_cart(self):
        if not self.products:
            print("Your Cart is empty.")
            return

        print("\n ============= SOPPING CART ===============")

        total = 0

        for product in self.products:
            amount = product["price"] * product["quantity"]
            total += amount

            print("Product ID       :", product["id"])
            print("Product Name     :", product["name"])
            print("Product Price    :", product["price"])
            print("Product Quantity :", product["quantity"])
            print("Product Amount   :", amount)
            print("---------------------------------------------")

        print("Total Amount: $",total)

    # Remove product
    def remove_product(self):
        product_id = input("Enter Your Product ID to Remove: ")

        for product in self.products:
            if product["id"] == product_id:
                self.products.remove(product)
                print("Product removed successfuly.")
                return

        print("Product Not Found.")

    # Calculate Total
    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product["price"] * product["quantity"]

        return total

    # Checkout
    def checkout(self):
        if not self.products:
            print("Your cart is empty.")
            return

        total = self.calculate_total()

        print("\n ============ CHECKOUT ============")
        print("Total Amount: $", total)

        confirm = input("Conform order? (yes/no): ").lower()

        if confirm == yes:
            print("Order place successfully!")
            print("Amount to pay: $", total)

            self.products.clear()

        else:
            print("Order cancelled.")

# Create shopping Cart
cart = Shoppingcart()

# Main Menu
while True:

    print("\n ============= ONLINE SHOPPING CART ===============")
    print("1. Add Product")
    print("2. Display Cart")
    print("3. Remove Product")
    print("4. Checkout")
    print("5. Exit")
    print("===========================================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cart.add_product()
    elif choice == 2:
        cart.display_cart()
    elif choice == 3:
        cart.remove_product()
    elif choice == 4:
        cart.checkout()
    elif choice == 5:
        print("Thank You for Using Online Sopping Cart.")

    else:
        print("Invalid Choice. Please try again.")

