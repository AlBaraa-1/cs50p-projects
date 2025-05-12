def main():
    # Prompt the user for input
    input_string = input("camelCase: ")
    # Convert the input string from camelCase to snake_case
    print("snake_case:", camelCaseToSnakeCase(input_string))

#function to convert camelCase to snake_case
def camelCaseToSnakeCase(string):

    #empty list to store the result
    result = []

    #loop through chrs in the string
    for char in string:

        #check if the char is uppper case
        if char.isupper():

            #lower case the char and add _ before it
            char = "_" + char.lower()

        #add the char to the result list
        result.append(char)

    #join the list to form a string and return it
    return ''.join(result)
            

if __name__ == "__main__":
    main()