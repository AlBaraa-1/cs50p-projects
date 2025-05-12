def main():
    #ask the user for the time in hours and minutes
    time = input("What time is it? ")

    #call the convert function to convert the format of the time
    total = convert(time)
    
    #check what time it is and print the meal time
    if 7 <= total < 8:
        print("Breakfast time")
    elif 12 <= total < 13:
        print("Lunch time")
    elif  18 <= total < 19:
        print("Dinner time")
    
def convert(time):
    #split the time into hours and minutes
    hours, minutes = time.split(":")

    #convert hours to an int value and minutes to a float value
    hours = int(hours)
    minutes = float(minutes) / 60
    
    
    #sum the hours and minutes to get the total time in hours
    converted = hours + minutes
    
    return converted

if __name__ == "__main__":
    main()