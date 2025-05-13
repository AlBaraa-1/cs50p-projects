import random

def main():
    # Prompt the user for input
    lvl = -1

    #lvl shoudl be a positive integer
    while lvl <= 0:
        try:
            # Prompt the user for a level
            lvl = int(input("Level: "))

        # if the input is not a positive integer, prompt again
        except ValueError:
            pass

    # Generate a random number between 1 and the level
    RNumber = random.randint(1 , lvl)

    # Prompt the user for a guess
    while True:
        
        try:
            # Prompt the user for a guess
            guess = int(input("Guess: "))

            # Check if the guess is a positive integer
            if guess < 1:
                pass

            # Check if the guess is too small, too large
            elif guess < RNumber:
                print("Too small!")
            elif guess > RNumber:
                print("Too large!")

            # If the guess is correct, print a message and exit the loop
            else:
                print("Just right!")
                break

        # If the input is not a positive integer, prompt again
        except ValueError:
            pass
     
if __name__ == "__main__":
    main()