import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few CLA")
    elif len(sys.argv) > 2:
        sys.exit("Too many CLA")
    elif not sys.argv[1].endswith(".py"):
        sys.exit(f"Not a Python file: {sys.argv[1]}")

    try:
        with open(sys.argv[1], "r") as file:
            count1 = 0
            lines = file.readlines()
            for line in lines:
                if line.startswith("#") or line == "\n":
                    count1 = count1
                else:
                    count1 += 1
    except FileNotFoundError:
        sys.exit(f"File not found: {sys.argv[1]}")

    print(count1)

if __name__ == "__main__":
    main()


