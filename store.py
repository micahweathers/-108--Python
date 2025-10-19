from catalog import catalog

cart = []

def print_header(text):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(text)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def print_menu():
    print("Menu")
    print("1.  View Catalog")
    print("2. Search Product")
    print("3. View Cart")
    print("4. Clear Cart")
    print("Q. Quit")

def print_catalog():
    print("~ Our Catalog ~")
    for prod in catalog:
        print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']:.2f} |")
    
    while True:
        answer = input("Type ID to add ('n' to close): ").lower()
        if answer == "n":
            return
        else:
            add_product_to_cart(answer)

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)
            print(f"Added: | {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']:.2f} |")
            break
    if not found:
        print("ERROR: Product not found")

def search_product():
    text = input("Search text: ")
    found = False
    for prod in catalog:
        if text in prod["title"]:
            found = True
            print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']:.2f} |")
            choice = input("Do you want to add to your cart? (y/n): ").lower()
            if choice == "y":
                add_product_to_cart(prod["id"])
    if not found:
        print("Sorry, this item doesn't exist.")
    
    input("\nPress Enter to return to main menu...")

#Main Loop
#Main Loop
options = ""
while options != "q":
    print_header("Welcome to the Store!")
    print_menu()

    options = input("Enter your menu selection here: ").lower()

    if options == "1":
        print_catalog()
    elif options == "2":
        search_product()
    elif options == "3":
        if len(cart) == 0:
            print("Your cart is empty!")
        else:
            print("~ Your Cart ~")
            total = 0 
            for item in cart:
                print(f"| {item['id']} | {item['title'].ljust(15)} | ${item['price']:.2f} |")
                total += item['price']
            
            print("~~~~~~~~~~~~~~")
            print(f"Total: ${total:.2f}")
    
        input("\nPress Enter to return to main menu...")
    elif options == "4":  # Clear Cart Option
        if len(cart) == 0:
            print("Your cart is already empty!")
        else:
            confirm = input("Are you sure you want to clear your cart? (y/n): ").lower()
            if confirm == "y":
                cart.clear()  # or cart = []
                print("Cart cleared successfully!")
            else:
                print("Cart not cleared.")
        input("\nPress Enter to return to main menu...")
    elif options == "q":
        print("Thanks for shopping!")
    else:
        print("ERROR: Invalid option!")