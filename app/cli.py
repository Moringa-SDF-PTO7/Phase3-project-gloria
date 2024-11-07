import click
from database import SessionLocal
from app.models import User, Category, Habit
from app.utils import prompt_date, prompt_positive_float, prompt_non_empty_string
from datetime import datetime

# ------------------- Database Session Management -------------------
def get_session():
    """Create and return a new session."""
    session = SessionLocal()
    return session

# ------------------- User Management -------------------
def manage_users():
    """
    Menu for managing users: allows creating, deleting, displaying users, viewing user habits, or returning to the main menu.
    """
    while True:
        click.echo("\n--- Manage Users ---")
        click.echo("1. Create User")
        click.echo("2. Delete User")
        click.echo("3. Display Users")
        click.echo("4. View User Habits and Progress")
        click.echo("5. Back to Main Menu")
        
        choice = click.prompt("Select an option", type=int)

        if choice == 1:
            create_user()
        elif choice == 2:
            delete_user()
        elif choice == 3:
            display_users()
        elif choice == 4:
            view_user_habits()
        elif choice == 5:
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

def create_user():
    """
    Handles the creation of a new user.
    """
    name = prompt_non_empty_string("Enter user name")
    session = get_session()  # Start a new session
    try:
        user = User.create(session, name=name)
        click.echo(f"User created: {user}")
    except Exception as e:
        click.echo(f"Error creating user: {e}")
    finally:
        session.close()  # Ensure session is closed after operation

def delete_user():
    """
    Handles the deletion of an existing user.
    """
    user_id = click.prompt("Enter user ID to delete", type=int)
    session = get_session()  # Start a new session
    success = User.delete(session, user_id)
    if success:
        click.echo("User deleted successfully.")
    else:
        click.echo("User not found.")
    session.close()

def display_users():
    """
    Displays all users currently stored in the database.
    """
    session = get_session()
    users = User.get_all(session)
    if not users:
        click.echo("No users found.")
        session.close()
        return
    click.echo("Users:")
    for user in users:
        click.echo(f"ID: {user.id} | Name: {user.name}")
    session.close()

def view_user_habits():
    """
    Displays all habits for a specified user, along with their progress.
    """
    user_id = click.prompt("Enter user ID to view their habits", type=int)
    session = get_session()
    user = User.find_by_id(session, user_id)

    if not user:
        click.echo("User not found.")
        session.close()
        return

    habits = user.habits
    if not habits:
        click.echo(f"No habits found for user: {user.name}")
    else:
        click.echo(f"Habits for User '{user.name}':")
        for habit in habits:
            click.echo(f"ID: {habit.id} | Name: {habit.name} | Frequency: {habit.frequency} | Progress: {habit.progress}")

    session.close()

# ------------------- Category Management -------------------
def manage_categories():
    """
    Menu for managing categories: allows creating, deleting, displaying categories, 
    viewing category details, or returning to the main menu.
    """
    while True:
        click.echo("\n--- Manage Categories ---")
        click.echo("1. Create Category")
        click.echo("2. Delete Category")
        click.echo("3. Display Categories")
        click.echo("4. Find Category")
        click.echo("5. View Category Habits")
        click.echo("6. Back to Main Menu")
        
        choice = click.prompt("Select an option", type=int)

        if choice == 1:
            create_category()
        elif choice == 2:
            delete_category()
        elif choice == 3:
            display_categories()
        elif choice == 4:
            find_category()
        elif choice == 5:
            view_category_habits()
        elif choice == 6:
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

def create_category():
    """
    Handles the creation of a new category.
    """
    name = prompt_non_empty_string("Enter category name")
    session = get_session()
    try:
        category = Category.create(session, name=name)
        click.echo(f"Category created: {category}")
    except Exception as e:
        click.echo(f"Error creating category: {e}")
    finally:
        session.close()

def delete_category():
    """
    Handles the deletion of an existing category.
    """
    category_id = click.prompt("Enter category ID to delete", type=int)
    session = get_session()
    success = Category.delete(session, category_id)
    if success:
        click.echo("Category deleted successfully.")
    else:
        click.echo("Category not found.")
    session.close()

def display_categories():
    """
    Displays all categories currently stored in the database.
    """
    session = get_session()
    categories = Category.get_all(session)
    if not categories:
        click.echo("No categories found.")
        session.close()
        return
    click.echo("Categories:")
    for cat in categories:
        click.echo(f"ID: {cat.id} | Name: {cat.name}")
    session.close()

def find_category():
    """
    Finds a category by its ID or name.
    """
    find_id = click.prompt("Enter category ID to search (or press Enter to skip)", default='', show_default=False)
    name = click.prompt("Enter category name to search (or press Enter to skip)", default='', show_default=False)

    session = get_session()

    if find_id:
        category = Category.find_by_id(session, int(find_id))
    elif name:
        category = Category.find_by_name(session, name)
    else:
        click.echo("Please provide either ID or name to search.")
        session.close()
        return

    if category:
        click.echo(f"Found Category: ID: {category.id} | Name: {category.name}")
    else:
        click.echo("Category not found.")

    session.close()

def view_category_habits():
    """
    Displays all habits associated with a specific category.
    """
    
