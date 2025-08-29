#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models import session
from lib.models.restaurant import Restaurant
from lib.models.review import Review
from lib.models.menu import MenuItem

def seed_database():
    """Add sample data for testing"""
    print("Seeding sample data...")
    
    # Clear existing data
    session.query(MenuItem).delete()
    session.query(Review).delete()
    session.query(Restaurant).delete()
    session.commit()
    
    # Create sample restaurants
    r1 = Restaurant(name="Joe's Pizza")
    r2 = Restaurant(name="Sushi Palace")
    r3 = Restaurant(name="Steak House")
    
    session.add_all([r1, r2, r3])
    session.commit()
    
    # Create sample reviews
    reviews = [
        Review(star_rating=5, comment="Best pizza in town!", restaurant_id=r1.id),
        Review(star_rating=4, comment="Great value", restaurant_id=r1.id),
        Review(star_rating=5, comment="Amazing sushi", restaurant_id=r2.id),
        Review(star_rating=3, comment="Overpriced but good", restaurant_id=r3.id)
    ]
    
    # Create sample menu items
    menu_items = [
        MenuItem(name="Margherita Pizza", price=12.99, description="Classic tomato and mozzarella", restaurant_id=r1.id),
        MenuItem(name="Pepperoni Pizza", price=14.99, description="Pepperoni and cheese", restaurant_id=r1.id),
        MenuItem(name="California Roll", price=8.99, description="Crab, avocado, cucumber", restaurant_id=r2.id),
        MenuItem(name="Salmon Nigiri", price=5.99, description="Fresh salmon on rice", restaurant_id=r2.id),
        MenuItem(name="Ribeye Steak", price=29.99, description="12oz ribeye with sides", restaurant_id=r3.id)
    ]
    
    session.add_all(reviews + menu_items)
    session.commit()
    
    print("Sample data added successfully!")
    print(f" Added {session.query(Restaurant).count()} restaurants")
    print(f" Added {session.query(Review).count()} reviews")
    print(f" Added {session.query(MenuItem).count()} menu items")

if __name__ == "__main__":
    seed_database()