from datetime import datetime, date
import inflect

p = inflect.engine()
userBirth = input("Date of Birth(YYYY-MM-DD): ")
today = date(2000, 1, 1)

try:
    birthyear, birthmonth, birthday = userBirth.split("-")

    birthyear = int(birthyear)
    birthmonth = int(birthmonth)
    birthday = int(birthday)

    userBirth = date(birthyear, birthmonth, birthday)

    birthyear_to_minute = birthyear * 365 * 24 * 60
    birthmonth_to_minute = birthmonth * 30 * 24 * 60
    birthday_to_minute = birthday * 24 * 60

    year_to_minute = today.year * 365 * 24 * 60
    month_to_minute = today.month * 30 * 24 * 60
    day_to_minute = today.day * 24 * 60

    sum = (year_to_minute - birthyear_to_minute) + (month_to_minute - birthmonth_to_minute) + (day_to_minute - birthday_to_minute)
    sumword = p.number_to_words(sum).title()

    if sum < 0:
        print("Unknown date: Future date")
    elif sum == 0:
        print("It's today's date")
    else:
        print(f"Gap is: {sumword} minutes")

except ValueError:
    print("Invalid date format!")

