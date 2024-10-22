#IHO python
pancakes = int(input()) 
if pancakes > 3:
print("Yum!")  
else:
print("Still hungry!")


#whats your sign
number = int(input())  
print("Positive" if number > 0 else "Negative" if number < 0 else "Zero")

age = int(input())
if age >= 18:
  print("You can vote") 
elif 0 <= age <= 17:
    print("Too young to vote")  
else:

  print("You are a time traveller")



  #FIZZ BUZZ

  for f in range(1, 33):  
    if f % 15 == 0:  
        print("FizzBuzz")
    elif f % 3 == 0: 
        print("Fizz")
    elif f % 5 == 0:  
        print("Buzz")
    else:
        print(f)