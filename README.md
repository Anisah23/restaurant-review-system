## restaurant-review-system
A comprehensive Command-Line Interface (CLI) application for managing restaurant reviews and menus, built with Python and SQLAlchemy ORM.


## Features
1. Restaurant Management: Create, view, and delete restaurants
2. Review System: Add and view star ratings (1-5) and comments for restaurants
3. Menu Management: Create and manage menu items with prices and descriptions
4. Search Functionality: Find restaurants by name with case-insensitive search
5. Data Validation: Input validation for ratings, prices, and user inputs
6. Data Persistence: SQLite database with proper ORM modeling and Alembic migrations


## Menu Options
0. Exit the Program
     - Gracefully exits the application
1. View All Restaurants
     - Displays all restaurants with average ratings
     - Shows: ID, Name, Average Rating
2. Find Restaurant by Name
     - Searches restaurants by name (case-insensitive)
     - Workflow: Enter search term → View matching results
3. View Restaurant Reviews
     - Shows all reviews for a specific restaurant
     - Workflow: Select restaurant → View star ratings and comments
4. View Restaurant Menu
     - Displays menu items for a specific restaurant
     - Shows: Item name, price, description
5. Add New Restaurant
     - Creates a new restaurant entry
     - Input: Restaurant name
     - Validation: Prevents duplicate names
6. Add Restaurant Review
     - Adds a customer review with rating and comment
     - Workflow: Select restaurant → Enter rating (1-5) → Add comment
     - Validation: Rating must be 1-5 stars
7. Add Menu Item
     - Adds new item to restaurant menu
     - Input: Item name, price, description
     - Validation: Price must be positive
8. Delete Restaurant
     - Removes restaurant and all associated data
     - Workflow: Select restaurant → Confirm deletion
     - Safety: Confirmation prompt prevents accidents
9. Delete Menu Item
     - Removes specific menu item from restaurant
     - Workflow: Select restaurant → Select item → Confirm


## Dependencies
1. Python 3.12: Core programming language
2. SQLAlchemy: ORM and database management
3. Alembic: Database migrations and version control


## Setup Instructions
1. Clone or download the project files
2. Navigate to the project directory
    - cd restaurant-review-system
3. Install dependencies
    - pipenv install
4. Activate the virtual environment
    - pipenv shell
5. Initialize the database
    -python lib/debug.py


## Usage
1. Start the application using the command
    -python -m lib.cli
2. Follow the on-screen menu prompts to interact with the system
3. Input data as requested, ensuring to follow validation rules
4. Exit the application using option 0 when done


## Author
- Anisah Hussein
- Github : Anisah23 
- Project repository: https://github.com/Anisah23/restaurant-review-system


## License
This project is licensed under the MIT License. See the LICENSE file for details.