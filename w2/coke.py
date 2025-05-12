def main():
    
    #define the amount due
    amount = 50
    
    #while the amount is greater than 0
    while amount > 0:
        #print the amount due
        print(f"Amount Due: {amount}")

        #prompt the user for input
        coin = int(input("Insert Coin: "))

        #validate the coin
        if check_valid(coin):
            amount -= coin
    
    #if the amount is less than 0
    print(f"Change Owed: {abs(amount)}")
            
def check_valid(coin):
    #check if the coin is valid
    if coin in [25, 10, 5, 50]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()