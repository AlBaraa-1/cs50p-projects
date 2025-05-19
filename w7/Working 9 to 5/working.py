import re
import sys

def main():
    # Prompt user for input and print the converted time
    print(convert(input("Hours: ")))

def convert(s):
    # Match the input string against the expected time format using regex
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if not match:
        # Raise ValueError if input doesn't match the required format
        raise ValueError
    
    # Extract start time components
    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_period = match.group(3)
    
    # Extract end time components
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_period = match.group(6)

    # Validate hour and minute ranges
    if not (1 <= start_hour <= 12 and 0 <= start_minute < 60):
        raise ValueError
    if not (1 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError

    # Convert start time to 24-hour format
    if start_period == "AM" and start_hour == 12:
        start_hour = 0
    elif start_period == "PM" and start_hour != 12:
        start_hour += 12

    # Convert end time to 24-hour format
    if end_period == "AM" and end_hour == 12:
        end_hour = 0
    elif end_period == "PM" and end_hour != 12:
        end_hour += 12

    # Return the formatted 24-hour time range
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()