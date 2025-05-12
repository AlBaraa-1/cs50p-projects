def main():
    #take input from the user
    input_string = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n" ).strip().lower()
    
    #check if  the input is 42 or forty two by letters
    if input_string == "42":
        print("Yes")
    elif input_string == "forty two":
        print("Yes")
    elif input_string == "forty-two":
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    main()

