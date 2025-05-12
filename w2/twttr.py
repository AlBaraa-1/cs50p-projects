def main():
    #define a list of vowells
    vowells = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    #get user input and remove spaces
    userInput = input("input: ").strip()
    
    #create a empty list to store the result
    result = []

    #check if the input contains any vowells
    for char in userInput:
        if char not in vowells:
            
            #if not a vowell add it to the result list
            result.append(char)
    
    #join the result 
    result = ", ".join(result)

    #print the result   
    print(f"output: {result}")

if __name__ == "__main__":
    main()