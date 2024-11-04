# Phase3-project-gloria

 Habit Tracker CLI Application
Welcome to the Personal Tracker CLI Application! This command-line tool is designed to help you effortlessly manage and track personal habits. Using a straightforward and user-friendly CLI, you can create, view, and categorize habits, and track your habits. Ideal for individuals, households, or small teams, this tool makes tracking easy and effective .

# Table of Contents
# Features
1. Getting Started
2. Installation
3. Running the Program
4. Usage
5. Main Menu
6. Manage Owners and categories 
7. Database Structure
8. Example Workflow
9. Requirements
10. Contributing
11. License

Features
Owner Management: Create, view, and delete habits .
Category Management: Organize habits into categories how you want them eg physical, spiritual etc .
Habit  Management: Add, view, delete, and categorize habits.
Simple Navigation: User-friendly menu-driven CLI interface.

# Getting Started
Installation
To get started, clone this repository and set up your environment. Here’s how:

Clone the Repository:

git clone https://github.com/Moringa-SDF-PTO7/Phase3-project-gloria
cd Phase3-project-gloria
Set Up the Virtual Environment:

If you’re using pipenv (recommended):

pip install pipenv
pipenv install
pipenv shell
Running the Program
Initialize the Database:

Before using the application, initialize the database with:

python3 app/init_db.py
This script will create the necessary tables for owners, categories, and expenses.

Start the CLI Application:

Run the main application file:

pipenv run python3 app/cli.py


# Usage
Once the CLI is running, you’ll be presented with the main menu. Each option has a corresponding number, so simply type the number to select an action.

Main Menu
Option	Description
1	Manage Users
2	Manage Habits
3	Manage Categories
4	Exit


Manage Users
Users represent individuals tracking their habits. This menu lets you create, delete, and view users, along with tracking habits associated with each user.

Option	Description
1	Create User
2	Delete User
3	Display Users
4	View User Habits and Progress
5	Back to Main Menu
Example Commands

Create User: Enter the user’s name, and they’ll be added to the database.
View User Habits and Progress: Select a user by their ID to see all related habits and their progress.
Manage Habits
Habits are actions or behaviors that users want to track over time. This menu allows you to add, delete, and view habits.

Option	Description
1	Create Habit
2	Delete Habit
3	Display Habits
4	Find Habit
5	View Habit Progress
6	Back to Main Menu
Example Commands

Create Habit: Enter details such as name, frequency, and goal.
View Habit Progress: See statistics on how well you’re adhering to a specific habit.
Manage Categories
Categories help organize habits by grouping them (e.g., Health, Productivity, etc.). Each category can help users focus on specific areas of improvement.

Option	Description
1	Create Category
2	Delete Category
3	Display Categories
4	Find Category
5	View Habits in Category
6	Back to Main Menu
Example Commands

Create Category: Enter the category name.
View Habits in Category: See all habits related to a specific category.
Database Structure
The application uses an SQLite database with the following tables:

Users: Holds user details with a unique ID and name.
Categories: Stores category information.
Habits: Records individual habits, linked to both a user and a category.
Relationships:
One-to-Many between Users and Habits: Each user can have multiple habits.
One-to-Many between Categories and Habits: Each category can include multiple habits.
Example Workflow
Here’s a quick example of how you might use the application:

Create Users:

Select Manage Users -> Create User and enter names like "Alice" or "Bob".
Set Up Categories:

Select Manage Categories -> Create Category.
Enter categories like "Health" and "Productivity".
Add Habits:

Select Manage Habits -> Create Habit.
Enter details like "Exercise" with a daily frequency and a goal of 30 minutes.
Track Progress:

Check a user’s habit discipline by selecting View User Habits and Progress under Manage Users.

Requirements
The application requires Python 3.7+ and the following packages:

SQLAlchemy: Database ORM for handling data.
Click: Simplifies the creation of command-line interfaces.
These are installed automatically if you follow the Installation steps above.

License
This project is licensed under the MIT License. See the LICENSE file for details.

This Personal Expense Tracker CLI Application is a straightforward yet powerful tool for managing expenses, tracking budgets, and organizing financial data. It’s perfect for anyone looking to keep a closer eye on their spending in a simple, no-fuss environment. Enjoy tracking your habits!