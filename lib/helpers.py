from lib.models import Restaurant, Review, session, MenuItem

def exit_program():
    print("Thank you for using Restaurant Reviews! Goodbye!")
    exit()

def list_restaurants():
    restaurants = Restaurant.get_all()
    if not restaurants:
        print("No restaurants found.")
        return
    
    print("\n--- ALL RESTAURANTS ---")
    for restaurant in restaurants:
        print(f"{restaurant.id}. {restaurant.name} - Avg Rating: {restaurant.average_rating}/5")

def find_restaurant_by_name():
    name = input("Enter restaurant name to search for: ")
    restaurants = Restaurant.find_by_name(name)
    
    if not restaurants:
        print("No restaurants found with that name.")
        return
    
    print("\n--- SEARCH RESULTS ---")
    for restaurant in restaurants:
        print(f"{restaurant.id}. {restaurant.name} - Avg Rating: {restaurant.average_rating}/5")

def view_restaurant_reviews():
    list_restaurants()
    try:
        restaurant_id = int(input("\nEnter restaurant ID to see reviews: "))
        restaurant = Restaurant.find_by_id(restaurant_id)
        
        if not restaurant:
            print("Restaurant not found.")
            return
        
        print(f"\n--- REVIEWS FOR {restaurant.name.upper()} ---")
        if not restaurant.reviews:
            print("No reviews yet.")
            return
            
        for review in restaurant.reviews:
            print(f"⭐ {review.star_rating}/5 - {review.comment}")
        print(f"\nAverage Rating: {restaurant.average_rating}/5")
        
    except ValueError:
        print("Please enter a valid number.")

def view_restaurant_menu():
    list_restaurants()
    try:
        restaurant_id = int(input("\nEnter restaurant ID to view menu: "))
        restaurant = Restaurant.find_by_id(restaurant_id)
        
        if not restaurant:
            print("Restaurant not found.")
            return
        
        menu_items = MenuItem.find_by_restaurant(restaurant_id)
        
        print(f"\n--- MENU FOR {restaurant.name.upper()} ---")
        if not menu_items:
            print("No menu items yet.")
            return
            
        for item in menu_items:
            print(f"{item.id}. {item.name} - ${item.price:.2f}")
            print(f"   Description: {item.description}")
            print()
        
    except ValueError:
        print("Please enter a valid number.")

def add_restaurant():
    name = input("Enter restaurant name: ")
    
    try:
        restaurant = Restaurant.create(name=name)
        print(f"Successfully added {restaurant.name}!")
    except Exception as e:
        print(f"Error adding restaurant: {e}")

def add_review():
    list_restaurants()
    try:
        restaurant_id = int(input("\nEnter restaurant ID to review: "))
        restaurant = Restaurant.find_by_id(restaurant_id)
        
        if not restaurant:
            print("Restaurant not found.")
            return
        
        try:
            star_rating = int(input("Enter star rating (1-5): "))
            comment = input("Enter your review comment: ")
            
            review = Review.create(star_rating=star_rating, comment=comment, restaurant_id=restaurant.id)
            print(f"Successfully added your review for {restaurant.name}!")
            
        except ValueError as e:
            print(f"Error: {e}")
            
    except ValueError:
        print("Please enter a valid number.")

def add_menu_item():
    list_restaurants()
    try:
        restaurant_id = int(input("\nEnter restaurant ID to add menu item: "))
        restaurant = Restaurant.find_by_id(restaurant_id)
        
        if not restaurant:
            print("Restaurant not found.")
            return
        
        name = input("Enter menu item name: ")
        
        try:
            price = float(input("Enter price: "))
            description = input("Enter description: ")
            
            menu_item = MenuItem.create(
                name=name, 
                price=price, 
                description=description, 
                restaurant_id=restaurant.id
            )
            print(f"Successfully added {menu_item.name} to {restaurant.name}'s menu!")
            
        except ValueError as e:
            print(f"Error: {e}")
            
    except ValueError:
        print("Please enter a valid number.")

def delete_restaurant():
    list_restaurants()
    try:
        restaurant_id = int(input("\nEnter restaurant ID to delete: "))
        restaurant = Restaurant.find_by_id(restaurant_id)
        
        if not restaurant:
            print("Restaurant not found.")
            return
        
        confirm = input(f"Are you sure you want to delete {restaurant.name} and all its reviews? (y/n): ")
        if confirm.lower() == 'y':
            restaurant.delete()
            print(f"Successfully deleted {restaurant.name}!")
        else:
            print("Deletion cancelled.")
            
    except ValueError:
        print("Please enter a valid number.")

def delete_menu_item():
    list_restaurants()
    try:
        restaurant_id = int(input("\nEnter restaurant ID to delete menu item from: "))
        restaurant = Restaurant.find_by_id(restaurant_id)
        
        if not restaurant:
            print("Restaurant not found.")
            return
        
        menu_items = MenuItem.find_by_restaurant(restaurant_id)
        if not menu_items:
            print("No menu items found for this restaurant.")
            return
        
        print(f"\n--- MENU ITEMS FOR {restaurant.name.upper()} ---")
        for item in menu_items:
            print(f"{item.id}. {item.name} - ${item.price:.2f}")
        
        try:
            item_id = int(input("\nEnter menu item ID to delete: "))
            menu_item = MenuItem.find_by_id(item_id)
            
            if not menu_item or menu_item.restaurant_id != restaurant_id:
                print("Menu item not found.")
                return
            
            confirm = input(f"Are you sure you want to delete {menu_item.name}? (y/n): ")
            if confirm.lower() == 'y':
                menu_item.delete()
                print(f"Successfully deleted {menu_item.name}!")
            else:
                print("Deletion cancelled.")
                
        except ValueError:
            print("Please enter a valid number.")
            
    except ValueError:
        print("Please enter a valid number.")