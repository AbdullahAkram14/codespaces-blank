import random

# Function to handle order tracking
def handle_order(orders):
    order_number = input("Please enter your order number: ")
    if order_number in orders:
        print(f"Tracking details for order #{order_number}: {orders[order_number]}")
    else:
        print("Order not found. Please check your order number.")

# Function to handle return/exchange
def handle_return_exchange(orders):
    print("Return or Exchange Options:")
    print("1. Return Item")
    print("2. Exchange Item")
    print("3. Check Return Status")
    return_choice = input("Please select an option (1-3): ")

    if return_choice == "1":
        order_number = input("Please enter your order number for the item you wish to return: ")
        if order_number in orders:
            print(f"Return request for order #{order_number} has been initiated.")
            orders[order_number] = "Return initiated"
        else:
            print("Order not found.")
    elif return_choice == "2":
        order_number = input("Please enter your order number for the item you wish to exchange: ")
        if order_number in orders:
            print(f"Exchange request for order #{order_number} has been initiated.")
            orders[order_number] = "Exchange initiated"
        else:
            print("Order not found.")
    elif return_choice == "3":
        order_number = input("Please enter your order number to check return status: ")
        if order_number in orders:
            print(f"Return status for order #{order_number}: {orders[order_number]}")
        else:
            print("Order not found.")

# Function to handle food delivery status
def handle_food_delivery_status(orders):
    order_number = input("Please enter your order number to check delivery status: ")
    if order_number in orders:
        print(f"Delivery status for order #{order_number}: On the way.")
    else:
        print("Order not found.")

# Function to handle user feedback
def handle_feedback():
    feedback = input("Please rate your experience from 1 to 5: ")
    if feedback == "5":
        print("Thank you for the great feedback!")
    else:
        print("Thank you for your feedback, we will work to improve!")

# Main chatbot function
def chatbot():
    print("Welcome to the Store Chatbot!")
    
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")
    
    orders = {}
    
    while True:
        print("\nMenu:")
        print("1. Ask about store hours")
        print("2. Ask about location")
        print("3. Ask about available products")
        print("4. Ask about prices")
        print("5. Check store promotions")
        print("6. Track your order")
        print("7. Place a custom order")
        print("8. Ask a FAQ")
        print("9. Contact support")
        print("10. Give feedback")
        print("11. Return or exchange item")
        print("12. Food delivery status")
        print("13. Exit")
    
        choice = input("Please select an option (1-13): ")
        
        if choice == "1":
            print("Our store is open from 9 AM to 9 PM daily.")
        elif choice == "2":
            print("We are located at 123 Main Street, Texas, USA.")
        elif choice == "3":
            print("We offer a variety of products, including electronics, clothing, and home goods.")
        elif choice == "4":
            print("Our prices are competitive and vary by product. Please visit our website for more details.")
        elif choice == "5":
            print("Currently, we have a 20% off sale on all electronics!")
        elif choice == "6":
            handle_order(orders)
        elif choice == "7":
            order_details = input("Please describe your order: ")
            order_number = str(random.randint(1000, 9999))
            orders[order_number] = "Order placed. Processing."
            print(f"Your order has been placed successfully! Your order number is {order_number}.")
        elif choice == "8":
            print("FAQs:")
            print("Q1: How do I return an item?")
            print("A1: To return an item, visit our Returns & Exchanges page.")
            print("Q2: How can I track my order?")
            print("A2: Enter your order number to track your order status.")
        elif choice == "9":
            print("To contact support, please call 1-800-123-4567 or email support@preworkstore.com.")
        elif choice == "10":
            handle_feedback()
        elif choice == "11":
            handle_return_exchange(orders)
        elif choice == "12":
            handle_food_delivery_status(orders)
        elif choice == "13":
            print("Thank you for using the Store Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    chatbot()
