# ------------------------------------------
# Store Data
# ------------------------------------------

products = []
cart = []
orders = []

# ------------------------------------------
# Add Product Function
# ------------------------------------------
def add_product():
      product_name = input("enter product_name: ")
      product_price = float(input("enter product_price: "))
      product_quantity= int(input("enter product_quantity: "))
    
      products.append({
                    "product_name": product_name,
                    "price": product_price,
                    "quantity": product_quantity
                })
      print("success")


#  ------------------------------------------
# Show Products Function
# ------------------------------------------

def show_products():
    for product in products:
   
       print("product_name:",product["product_name"])
       print("price:",product["price"])
       print("quantity:",product["quantity"])

# ------------------------------------------
# Search Product Function
# ------------------------------------------

def search_product():

    product_name = input("enter product_name: ")

    found = False

    for product in products:

        if product_name == product["product_name"]:

            print("Product found")
            print("Product name:", product["product_name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

            found = True
            break

    if found == False:
        print("Product not found")


# ------------------------------------------
# Update Product Function
# ------------------------------------------
def update_product():

    product_name = input("enter product_name: ")

    found = False

    for product in products:

        if product_name == product["product_name"]:

            product_price = float(input("enter product_price: "))

            product_quantity = int(input("enter product_quantity: "))
            product["price"] =  product_price
            
            product["quantity"] = product_quantity
           

            found = True
            print("success")
        
            break

    if found == False:
            print("Product not found")
         

# ------------------------------------------
# Delete Product Function
# ------------------------------------------

def delete_product():

    product_name = input("enter product_name: ")

    found = False
    
    for product in products:

        if product_name == product["product_name"]:

            products.remove(product)

            found = True

            print("success")

            break

    if found == False:
        print("Product not found")

# ------------------------------------------
# Add To Cart Function
# ------------------------------------------

def add_to_cart():

    product_name = input("enter product name: ")
    product_quantity = int(input("enter quantity: "))

    found = False

    for product in products:

        if product_name == product["product_name"]:

            found = True

            if product_quantity <= product["quantity"]:

                cart.append({
                    "product_name": product_name,
                    "price": product["price"],
                    "quantity": product_quantity
                })
                product["quantity"] = product["quantity"] - product_quantity
                print("Added to cart")

            else:
                print("Out of stock")

            break

    if found == False:
        print("Product not found")

# ------------------------------------------
# show Cart Function
# ------------------------------------------

def show_cart():

    total = 0

    for item in cart:

        
        print("Product Name:", item["product_name"])

       
        print("Price:", item["price"])

       
        print("Quantity:", item["quantity"])

       
        item_total = item["price"] * item["quantity"]

        total = total + item_total

    print("Total Cart Price:", total)


# ------------------------------------------
# Remove From Cart Function
# ------------------------------------------

def remove_from_cart():

    product_name = input("enter product name: ")

    found = False

    for item in cart:

        if product_name == item["product_name"]:

           
            for product in products:

                if product_name == product["product_name"]:

                  
                    product["quantity"] = product["quantity"] + item["quantity"]

                    break

        
            cart.remove(item)

            found = True

            print("Removed from cart")

            break

    if found == False:

        print("Product not found in cart")
# ------------------------------------------
# Place Order Function
# ------------------------------------------

def place_order():

    if len(cart) == 0:

        print("Cart is empty")

    else:

        total = 0

        for item in cart:

            item_total = item["price"] * item["quantity"]

            total = total + item_total

            orders.append({
                "product_name": item["product_name"],
                "price": item["price"],
                "quantity": item["quantity"],
                "total": item_total
            })

        cart.clear()
        print("Order placed successfully")
        print("Total:", total)
# ------------------------------------------
# Show Orders Function
# ------------------------------------------

def show_orders():

    if len(orders) == 0:

        print("No orders found")

    else:

        for order in orders:

         
            print("Product Name:", order["product_name"])

           
            print("Price:", order["price"])

            
            print("Quantity:", order["quantity"])

        
            print("Total:", order["total"])

# ------------------------------------------
# Cancel Order Function
# ------------------------------------------

def cancel_order():

    product_name = input("enter product name: ")

    found = False

    for order in orders:

        if product_name == order["product_name"]:

            for product in products:

                if product_name == product["product_name"]:

                  
                    product["quantity"] = product["quantity"] + order["quantity"]

                    break

          
            orders.remove(order)

            found = True

            print("Order cancelled successfully")

            break

    if found == False:

        print("Order not found")


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n===== ONLINE STORE MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Add To Cart")
    print("7. Show Cart")
    print("8. Remove From Cart")
    print("9. Place Order")
    print("10. Show Orders")
    print("11. Cancel Order")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        show_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        add_to_cart()

    elif choice == "7":
        show_cart()

    elif choice == "8":
        remove_from_cart()

    elif choice == "9":
        place_order()

    elif choice == "10":
        show_orders()

    elif choice == "11":
        cancel_order()

    elif choice == "12":
        print("Thank you for using Online Store Management System!")
        break

    else:
        print("Invalid choice")