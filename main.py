import random

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
        print("11. Exit")
    
        choice = input("Please select an option (1-11): ")
        
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
            order_number = input("Please enter your order number: ")
            if order_number in orders:
                print(f"Tracking details for order #{order_number}: {orders[order_number]}")
            else:
                print("Order not found. Please check your order number.")
        elif choice == "7":
            order_details = input("Please describe your order: ")
            order_number = str(random.randint(1000, 9999))
            orders[order_number] = "Order placed. Processing."
            print(f"Your order has been placed successfully! Your order number is {order_number}.")
        elif choice == "8":
            print("FAQs: What are your store hours? What products do you offer? How do I contact support?")
        elif choice == "9":
            print("To contact support, please call 1-800-123-4567 or email support@preworkstore.com.")
        elif choice == "10":
            feedback = input("Please rate your experience from 1 to 5: ")
            if feedback == "5":
                print("Thank you for the great feedback!")
            else:
                print("Thank you for your feedback, we will work to improve!")
        elif choice == "11":
            print("Thank you for using the Store Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    chatbot()
