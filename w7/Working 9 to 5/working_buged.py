import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if not match:
        raise ValueError
    
    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_period = match.group(3)
    
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_period = match.group(6)

    if not (1 <= start_hour <= 12 and 0 <= start_minute < 60):
        raise ValueError
    if not (1 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError

    # Convert to 24-hour format
    if start_period == "AM" and start_hour == 12:
        start_hour = 0
    elif start_period == "PM" and start_hour != 12:
        start_hour += 12

    if end_period == "AM" and end_hour == 12:
        end_hour = 0
    elif end_period == "PM" and end_hour != 12:
        end_hour += 12
        
    # BUG: Omit minutes in the return value (for testing purposes)
    return f"{start_hour:02}:00 to {end_hour:02}:00"


if __name__ == "__main__":
    main()