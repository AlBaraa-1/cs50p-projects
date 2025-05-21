import inflect
from datetime import datetime, date
import sys
import os

def main():
    # Prompt the user for their date of birth
    input_date = input("Date of Birth: ")
    
    # Parse the string into a date object
    dob = parse_date(input_date)

    # Use a fixed date during testing if specified
    if os.getenv("CS50_SEASONS_TEST") == "true":
        today = get_fixed_test_date()
    else:
        today = date.today()

    # Calculate total minutes alive
    minutes = calculate_minutes_alive(dob, today)

    # Print result in words
    print(format_minutes(minutes))


def parse_date(input_str: str) -> date:
    """Parse a string in YYYY-MM-DD format to a date object."""
    try:
        return datetime.strptime(input_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")


def calculate_minutes_alive(birth_date: date, today: date) -> int:
    """Calculate total minutes between birth_date and today."""
    delta_days = (today - birth_date).days
    return delta_days * 1440  # 1440 minutes in a day


def format_minutes(minutes: int) -> str:
    """Convert minutes to English words."""
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


def get_fixed_test_date() -> date:
    """Return fixed date (2000-01-01) for testing purposes."""
    return date(2000, 1, 1)


if __name__ == "__main__":
    main()
