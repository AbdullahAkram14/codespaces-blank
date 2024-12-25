
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
        print("5. Exit")
    
        choice = input("Please select an option (1-5): ")
        
        if choice == "1":
            print("Our store is open from 9 AM to 9 PM daily.")
        elif choice == "2":
            print("We are located at 123 Main Street, Anytown, USA.")
        elif choice == "3":
            print("We offer a variety of products, including electronics, clothing, and home goods.")
        elif choice == "4":
            print("Our prices are competitive and vary by product. Please visit our website for more details.")
        elif choice == "5":
            print("Thank you for using the PreWork Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    chatbot()
