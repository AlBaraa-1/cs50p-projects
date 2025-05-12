def main():
    # Get the fraction from the user
    x, y = getInt("Fraction: ")
    
    #priint the fraction in percentage
    print(convert(x,y))

def getInt(prompt):
    #loop until a valid fraction is entered
    while True:
        try:
            #get input from user
            fraction = input(prompt)

            #split the input into two parts
            x, y = fraction.split("/")

            #convert the input into integers
            x = int(x)
            y = int(y)

            #check if the denominator is zero or if the numerator is greater than the denominator
            if y <= 0:
                raise ZeroDivisionError   
            elif x > y:
                raise ValueError

            #return the fraction as integers x and y
            return x , y
        
        #reattempt the input if the user enters a non-integer value
        except ValueError:
            pass
        
        #output and error message if the user enters a zero denominator
        except ZeroDivisionError:
            print("ZeroDivisionError")

#convert the fraction into percentage
def convert(x, y):
    percent = x / y * 100
    if percent >= 99:
        return "F"
    elif percent == 0 or percent <= 1:
        return "E"
    else: 
        return f"{percent:.0f}%"

if __name__ == "__main__":
    main()