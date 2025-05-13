import random
    
def main():
    # Prompt the user for a level
    lvl = get_level()
    
    #initialize score and attempts
    score = 0
    attempts = 0

    # iterate 10 times
    for i in range(10):

        # Generate two random integers based on the level
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        while True:
            try:
                # Prompt the user for an answer
                answer = int(input("{} + {} = ".format(x, y)))

                # Check if the answer is correct and update score
                if answer == x + y:
                    score += 1
                    break
                else:
                    # If the answer is incorrect, increment attempts
                    attempts += 1
                    print("EEE")
                
                # If attempts reach 3, show the correct answer
                if attempts == 3:
                    print(f"{x} + {y} = {x + y}")
                    attempts = 0
                    break     

            # If the input is not a valid positive integer, prompt again 
            except ValueError:
                pass
    
    # Print the final score
    print(f"Score: {score}")

def get_level():
    # Initialize level 
    lvl = -1
    while True:
        try:
            # Prompt the user for a level
            lvl = int(input("Level: "))

            # Check if the level is between 1 and 3 and return it
            if lvl in range(1, 4):
                return lvl
        # If the input is invalid level, prompt again
        except ValueError:
            pass

def generate_integer(level):
    # Generate a random integer based on the level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        return None

if __name__ == "__main__":
    main()