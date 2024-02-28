m = int(input("What month are we in? (Enter the number from 1-12):"))
if m >= 4 and m <= 6:
    print("Boston is in Spring")
elif m >= 7 and m <= 9:
    print("Boston is in Summer")
elif m >= 10 and m <= 11:
    print("Boston is in Autumn")
elif m == 12 or m >= 1 and m < 3:
    print("Boston is in Winter")
else:
    print("There are only 12 months in a year.")