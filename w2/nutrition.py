def main():
    #defin dectionary of fruits and their nutrition values
    nutrition = {"apple": 130,
                 "avocado": 50,
                 "banana": 110,
                 "cantaloupe": 50,
                 "grapefuit": 60,
                 "honeydew melon": 50,
                 "kiwifruit": 90,
                 "lemon": 15,
                 "lime": 20,
                 "nectarine": 60,
                 "orange": 80,
                 "peach": 60,
                 "pear": 100,
                 "pineapple": 50,
                 "plums": 70,
                 "strawberries": 50,
                 "sweet cherries": 100,
                 "tangerine": 50,
                 "watermelon": 80}
    
    #take input from user
    fruit = input("item: ").lower()

    #search for the fruit in the dictionary 
    if fruit in nutrition:

        #if fruit is found, print the nutrition value
        print(f"Calories: {nutrition[fruit]}")

if __name__ == "__main__":
    main()
