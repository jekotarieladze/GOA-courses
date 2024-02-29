
price_for_adults = 25
total_cost = 0
people = 13 
adults = 0
children = 0 
while people > 0:
    age = int(input("how old are you: "))
    if age < 18:
        children += 1
        print("since this person is under 18 you get a free ticket")
    else:
        adults += 1
        total_cost += price_for_adults
        print("That would be 25 GEL.")

    people -= 1