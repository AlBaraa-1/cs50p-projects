import sys
import csv


def main():
    input_file = get_route()
    convert(input_file, sys.argv[2])


# convert the input
def convert(input_file, output_file):
    # open the input file and output file 
    with open(input_file) as input, open(output_file, "w", newline="") as output:

        # read each row as a dictionary
        reader = csv.DictReader(input)

        # write in the ouput file
        writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])

        # define the header
        writer.writeheader()

        # iterate through each row
        for row in reader:

            # split 'name' into first and last along with 'house'
            last, first  = row["name"].split(", ")
            house = row["house"]

            # write to new file with DictWriter (first, last, house)
            writer.writerow({"first": first, "last": last, "house": house})

    # return the output file
    return output_file

#brake it down
"""
- open the input file and output file
- read each row using DictReader
- for each row:
    - split 'name' into first and last
    - get 'house'
    - write to new file with DictWriter (first, last, house)
"""


# get 2 arguments from the command line
def get_route():
    if len(sys.argv) == 3:
        pass
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    

    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

    return sys.argv[1]


if __name__ == "__main__":
    main()