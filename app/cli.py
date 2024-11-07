import click
from app.models import User, Habit
from database import SessionLocal
from app.utils import prompt_non_empty_string, prompt_positive_float, prompt_date

def get_session():
    session = SessionLocal()
    return session

# User Management Menu
def manage_users():
    while True:
        click.echo("\n--- Manage Users ---")
        click.echo("1. Create User")
        click.echo("2. Delete User")
        click.echo("3. Display Users")
        click.echo("4. Find User by Name")
        click.echo("5. Back to Main Menu")

        choice = click.prompt("Select an option", type=int)

        if choice == 1:
            create_user()
        elif choice == 2:
            delete_user()
        elif choice == 3:
            display_users()
        elif choice == 4:
            find_user_by_name()
        elif choice == 5:
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

def create_user():
    name = prompt_non_empty_string("Enter user name")
    session = get_session()
    try:
        user = User.create(session, name=name)
        click.echo(f"User created: {user}")
    except Exception as e:
        click.echo(f"Error creating user: {e}")
    finally:
        session.close()

def delete_user():
    user_id = click.prompt("Enter user ID to delete", type=int)
    session = get_session()
    success = User.delete(session, user_id)
    if success:
        click.echo("User deleted successfully.")
    else:
        click.echo("User not found.")
    session.close()

def display_users():
    session = get_session()
    users = User.get_all(session)
    if not users:
        click.echo("No users found.")
    else:
        click.echo("Users:")
        for user in users:
            click.echo(f"ID: {user.id} | Name: {user.name}")
    session.close()

def find_user_by_name():
    name = click.prompt("Enter user name to search")
    session = get_session()
    user = User.find_by_name(session, name)
    if user:
        click.echo(f"Found User: ID: {user.id} | Name: {user.name}")
    else:
        click.echo("User not found.")
    session.close()

# Habit Management Menu
def manage_habits():
    while True:
        click.echo("\n--- Manage Habits ---")
        click.echo("1. Create Habit")
        click.echo("2. Delete Habit")
        click.echo("3. Display Habits")
        click.echo("4. Back to Main Menu")

        choice = click.prompt("Select an option", type=int)

        if choice == 1:
            create_habit()
        elif choice == 2:
            delete_habit()
        elif choice == 3:
            display_habits()
        elif choice == 4:
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

def create_habit():
    name = prompt_non_empty_string("Enter habit name")
    frequency = prompt_positive_float("Enter habit frequency (days per week)")
    user_id = click.prompt("Enter user ID to assign this habit to", type=int)
    session = get_session()
    try:
        habit = Habit.create(session, name=name, frequency=frequency, user_id=user_id)
        click.echo(f"Habit created: {habit}")
    except Exception as e:
        click.echo(f"Error creating habit: {e}")
    finally:
        session.close()

def delete_habit():
    habit_id = click.prompt("Enter habit ID to delete", type=int)
    session = get_session()
    success = Habit.delete(session, habit_id)
    if success:
        click.echo("Habit deleted successfully.")
    else:
        click.echo("Habit not found.")
    session.close()

def display_habits():
    session = get_session()
    habits = Habit.get_all(session)
    if not habits:
        click.echo("No habits found.")
    else:
        click.echo("Habits:")
        for habit in habits:
            click.echo(f"ID: {habit.id} | Name: {habit.name} | Frequency: {habit.frequency} | Progress: {habit.progress}")
    session.close()

# Main CLI Menu
@click.group()
def cli():
    pass

@cli.command()
def start():
    while True:
        click.echo("\n--- Main Menu ---")
        click.echo("1. Manage Users")
        click.echo("2. Manage Habits")
        click.echo("3. Exit")
        
        choice = click.prompt("Select an option", type=int)

        if choice == 1:
            manage_users()
        elif choice == 2:
            manage_habits()
        elif choice == 3:
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    cli()
