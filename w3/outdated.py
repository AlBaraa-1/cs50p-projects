def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if month in range(1, 13) and day in range(1, 32):
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            elif "," in date:
                month_string, day_year = date.split(" ", 1)
                day, year = day_year.replace(",", "").split()
                month = months.index(month_string) + 1
                day = int(day)
                year = int(year)

                if month in range(1, 13) and day in range(1, 32):
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except ValueError:
            pass

if __name__ == "__main__":
    main()
