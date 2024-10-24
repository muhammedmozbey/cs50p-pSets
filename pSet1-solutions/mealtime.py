def main():
    randomInput = input("What time is it? ")
    time = convert(randomInput)
    if 7 <= time <= 8:
        print("breakfast time!")
    elif 12 <= time <= 13:
        print("lunch time!")
    elif 18 <= time <= 19:
        print("dinner time!")
    else:
        print("not meal time!")

def convert(time):
    hours, minutes = time.split(":")
    new_minutes = int(minutes) / 60
    return new_minutes + float(hours)

if __name__ == "__main__":
    main()