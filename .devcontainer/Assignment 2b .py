# Finding the area and circumfrence of a circle.

r = float(input("Your Radius: "))

if r == 0:
    print("The radius can't be zero -error")
elif r < 0:
    print("The radius can't be in the negatives - error")
else:

    a = 3.14 * r ** 2
    print(f"Your area is {a}")
    
    c = 3.14 * 2 * r
    print(f"Your circumference is {c}")


