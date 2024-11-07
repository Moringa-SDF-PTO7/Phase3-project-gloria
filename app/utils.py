import click
from datetime import datetime

def prompt_date(prompt_text="Enter a date (YYYY-MM-DD)"):
    """
    Prompts the user to input a date, validating the format.
    Returns a datetime object if the date is valid, or asks again if it's invalid.
    """
    while True:
        date_str = click.prompt(prompt_text)
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date
        except ValueError:
            click.echo("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def prompt_positive_float(prompt_text="Enter a positive number"):
    """
    Prompts the user to input a positive float, validates the input.
    """
    while True:
        try:
            value = click.prompt(prompt_text, type=float)
            if value > 0:
                return value
            else:
                click.echo("Please enter a number greater than 0.")
        except ValueError:
            click.echo("Invalid input. Please enter a valid positive number.")

def prompt_non_empty_string(prompt_text="Enter a non-empty string"):
    """
    Prompts the user to input a non-empty string.
    """
    while True:
        value = click.prompt(prompt_text)
        if value.strip():  # Checks if the input is not just whitespace
            return value
        else:
            click.echo("Input cannot be empty. Please enter a valid value.")
