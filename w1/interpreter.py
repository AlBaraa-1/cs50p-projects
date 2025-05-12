def main():
    # take input from user
    expression = input("Enter an expression: ")

    #split to x y z 
    x, y, z = expression.split(" ")

    #assign x and z to float

    ex = [float(x), float(z)]

    #assign y to be the operator
    operator = y
    if operator == "+":
        print(round(ex[0] + ex[1], 1))
    # round to 1 decimal place
    elif operator == "-":
        print(round(ex[0] - ex[1], 1))
    elif operator == "*":
        print(round(ex[0] * ex[1], 1))
    elif operator == "/":
        print(round(ex[0] / ex[1], 1))
    else:
        print("Invalid operator")


if __name__ == "__main__":
    main()