def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    #check if length of the string is between 2 and 6
    if len(s) > 6 or len(s) < 2:
        return False
    
    #check if the first two characters are degits
    for i in range(2):
        if not s[i].isalpha():
            return False
    
    F0 = []
    for char in s:
        if char.isdigit():
            F0.append(char)
    
    F0 = "".join(F0)
    if F0 and F0[0] == "0":
        return False
    else: pass
   
    for char in s:
        if not char.isalnum():
            return False
        
    found_digit = False
    for char in s:
        if char.isdigit():
            found_digit = True
        if found_digit and s[-1].isalpha():
            return False
        
    found_digit = False
    for char in s:
        if char.isdigit():
            found_digit = True
        elif found_digit:  # found a letter after a digit
            return False

    return True
if __name__ == "__main__":
    main()