def chatbot():
    print("Welcome to the PreWork Chatbot!")
    
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")
    
    print("How can I help you today?")
    
    while True:
        print("\nMenu:")
        print("1. Ask about store hours")
        print("2. Ask about location")
        print("3. Ask about available products")
        print("4. Ask about prices")
        print("5. Check store promotions")
        print("6. Track your order")
        print("7. Ask a FAQ")
        print("8. Contact support")
        print("9. Give feedback")
        print("10. Exit")
    
        choice = input("Please select an option (1-10): ")
        
        if choice == "1":
            print("Our store is open from 9 AM to 9 PM daily.")
        elif choice == "2":
            print("We are located at 123 Main Street, Anytown, USA.")
        elif choice == "3":
            print("We offer a variety of products, including electronics, clothing, and home goods.")
        elif choice == "4":
            print("Our prices are competitive and vary by product. Please visit our website for more details.")
        elif choice == "5":
            print("Currently, we have a 20% off sale on all electronics!")
        elif choice == "6":
            order_number = input("Please enter your order number: ")
            print(f"Tracking details for order #{order_number}: Your order is on its way and should arrive by tomorrow!")
        elif choice == "7":
            print("FAQs: What are your store hours? What products do you offer? How do I contact support?")
        elif choice == "8":
            print("To contact support, please call 1-800-123-4567 or email support@preworkstore.com.")
        elif choice == "9":
            feedback = input("Please rate your experience from 1 to 5: ")
            if feedback == "5":
                print("Thank you for the great feedback!")
            else:
                print("Thank you for your feedback, we will work to improve!")
        elif choice == "10":
            print("Thank you for using the PreWork Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    chatbot()
