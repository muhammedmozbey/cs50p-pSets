#.index() checks word's index
#.zfill() 2 -> 02

def main():
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"
              ]

    while True:
        try:
            userDate = input("Date:(MM/DD/YY or MONTH DAY, YEAR format) ")

            if checkcomma(userDate):
                cleanDate = userDate.replace(",", "").replace("  ", " ").strip()
                parts = cleanDate.split(" ")
                month = parts[0]
                day = parts[1]
                year = parts[2]
                print(f"{year}-{str((months.index(month) + 1)).zfill(2)}-{day.zfill(2)}")

            elif checksslash(userDate):
                cleanDate = userDate.replace("/", " ").strip()
                parts = cleanDate.split(" ")
                month = parts[0]
                day = parts[1]
                year = parts[2]
                print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")

            else:
                print("Invalid date format!")

        except (EOFError, KeyboardInterrupt):
            print("")
            break

def checkcomma(date):
    if "," in date:
        return True
    else:
        return False

def checksslash(date):
    if "/" in date:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
