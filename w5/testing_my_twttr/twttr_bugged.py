def main():
    # take input from the user and print the output
    user_input = input("Input: ")
    print("Output:", shorten(user_input))


def shorten(word):
    #the bugged version checks for lowercase vowels only (AEIOU is not included) 
    vowels = "aeiou" 

    # define the result variable to store the shortened word
    result = ""

    # iterate through each character in the word
    for char in word:
        
        # if the character is not a vowel, add it to the result
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()
