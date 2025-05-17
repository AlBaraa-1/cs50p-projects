import sys
import csv
from tabulate import tabulate


def main():
    # validate command line arguments
    file = get_route()

    # read csv file and create table
    table = create_table(file)

    # save the table to a variable
    output = format_csv(table)

    # print the table
    print(output)


# read csv file and return a lists in the table
def create_table(file):
    with open(file) as f:
        reader = csv.reader(f)
        table = list(reader)
    return table


# print the table in a grid format
def format_csv(table):
    return tabulate(table, headers="firstrow", tablefmt="grid")


def get_route():
    # expecting one command line argument
    if len(sys.argv) == 2:
        pass
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

    # check ends with .csv
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # check if file exists
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

    return sys.argv[1]


if __name__ == "__main__":
    main()
