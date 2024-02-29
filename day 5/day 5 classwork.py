age= int(input("how old are you? "))
limit = 18
height = int(input("whats your height? "))

if age > limit or height > 180:
    print("welcome")
elif age < limit and height < 180:
    print("you're just a kid")
elif age < limit and height > 180:
    print:("perferct height but age is not there yet ")
else:
    print("BYEE YOU DONR MEET THE REQUIREMENTS")