def main():
    user_input = input("Greeting:")
    ouput = value(user_input)
    print(f"${ouput}")


def value(greeting):
    # take out spaces and convert to lower case
    greeting = greeting.strip().lower()
    
    if greeting.startswith("hello"):
        return 0
    
    # check the input if starts with h give $20
    elif greeting.startswith("h"):
        return 20
    
    # check if the input dont contain h or hello give $100
    else:
        return 100


if __name__ == "__main__":
    main()
