# take a cla from user
# if its isalpha.csv pass, if not print an error message
# read before.csv file and write it into <cla>.csv file
import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few CLA")
    elif len(sys.argv) > 3:
        sys.exit("Too many CLA")

    try:
        if sys.argv[1].endswith(".csv"):
            filename1 = sys.argv[1].rsplit(".")
            if is_number(filename1[0]):
                sys.exit(f"File {sys.argv[1]} does not exist")
        if sys.argv[2].endswith(".csv"):
            filename2 = sys.argv[2].rsplit(".")
            if is_number(filename2[0]):
                sys.exit("The file you're create to create has invalid name")

        try:
            with open(sys.argv[1], "r") as file:
                read = csv.DictReader(file)
                data = list(read)
            #newline="" for preventing whitespaces between written lines
            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["firstname", "lastname", "house"])
                writer.writeheader()
#written filewriting before cuz if i wrote before it doesn't see writer variable and i can't  write all csv file with writerow() without looping
                for row in data:
                    name = row['name'].strip()
                    house = row['house'].strip()
                    delete_quote = name.replace('"', "")
                    firstname, lastname = delete_quote.split(", ")
                    writer.writerow({"firstname": firstname, "lastname": lastname, "house": house})

        except Exception as e:

            sys.exit(f"Error occured: {e}")

    except Exception as e:
        sys.exit(f"Error occured: {e}")

#checks if file name number
def is_number(s):
    if s in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()


