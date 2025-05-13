import sys 
import pyfiglet
import random

def main():
    # Check for the number of arguments
    if len(sys.argv) == 3:

        #check if the first argument is a valid flag
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            
            # Check if the second argument is a valid font name
            if sys.argv[2] in pyfiglet.FigletFont.getFonts():
                #if valid, prompt for input
                font = sys.argv[2]
                text = input("Input: ")

                #gnerate the ouput and print it
                output = pyfiglet.Figlet(font=font)
                print(output.renderText(text))

            # invalid font
            else:
                sys.exit("Invalid usage")

        # invalid flag
        else:
                sys.exit("Invalid usage")

    #if didnt pass any arguments, choose a random font
    elif len(sys.argv) == 1:

        # If no arguments are passed, prompt for input
        text = input("Input: ")

        # Generate a random font and print the output
        font = random.choice(pyfiglet.FigletFont.getFonts())
        output = pyfiglet.Figlet(font=font)
        print(output.renderText(text))

    # If the number of arguments is not 1 or 3, exit with an error message
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()