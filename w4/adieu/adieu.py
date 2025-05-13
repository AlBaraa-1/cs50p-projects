import inflect

def main():

    # array to store names
    names = []

    # infinit loop to take input
    while True:
        try:
            # prompt for input
            text = input("Name: ")

            # add the input to the names array
            names.append(text)

        # exit the loop with EOFError (Ctrl+D) or (Ctrl+Z)
        except EOFError:
            break

    # print the names in a formatted string
    print("Adieu, adieu, to " + inflect.engine().join(names))

if __name__ == "__main__":
    main()