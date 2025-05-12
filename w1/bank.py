def main():
    #take input from the user all lower case
    # and strip the input to remove any leading or trailing spaces
    userInput = input("greeting:").strip().lower()

    #check the input if hello give $0
    if userInput.startswith ("hello"):
        print("$0")
    #check the input if starts with h give $20
    elif userInput.startswith("h"):
        print("$20")
    #check if the input dont contain h or hello give $100
    else:
        print("$100")

if __name__ == "__main__":
    main()

