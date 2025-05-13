import emoji

def main():
    # Prompt the user for input
    text  = input("Input: ")

    # Convert the text to emoji
    Emo = emoji.emojize(text, language='alias')

    # Print the output
    print("Output: "+ Emo)
    


if __name__ == "__main__":
    main()