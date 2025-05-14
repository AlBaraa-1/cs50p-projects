# updated fuel.py


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    # Split the input and convert to int
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    # Validate values
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    # Return percentage as integer
    return round((x / y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
