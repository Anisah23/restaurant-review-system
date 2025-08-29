from .helpers import (
    exit_program,
    list_restaurants,
    find_restaurant_by_name,
    view_restaurant_reviews,
    view_restaurant_menu,
    add_restaurant,
    add_review,
    add_menu_item,
    delete_restaurant,
    delete_menu_item
)

def main():

    
    while True:
        menu()
        choice = input("> ")
        handle_choice(choice)

def menu():
    print("\n" + "="*50)
    print("        RESTAURANT REVIEW SYSTEM ")
    print("="*50)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all restaurants")
    print("2. Find restaurant by name")
    print("3. View reviews for a restaurant")
    print("4. View menu for a restaurant")
    print("5. Add a new restaurant")
    print("6. Add a review for a restaurant")
    print("7. Add menu item to restaurant")
    print("8. Delete a restaurant")
    print("9. Delete menu item from restaurant")
    print("="*50)

def handle_choice(choice):
    if choice == "0":
        exit_program()
    elif choice == "1":
        list_restaurants()
    elif choice == "2":
        find_restaurant_by_name()
    elif choice == "3":
        view_restaurant_reviews()
    elif choice == "4":
        view_restaurant_menu()
    elif choice == "5":
        add_restaurant()
    elif choice == "6":
        add_review()
    elif choice == "7":
        add_menu_item()
    elif choice == "8":
        delete_restaurant()
    elif choice == "9":
        delete_menu_item()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()