bill=int(input())

tip=bill*20/100
print(tip)

#in todays lesson we learned
#boolean values = Truth and False 1 0
#if =

open=False
print(open)

x=7

print(x != 8)
print(x > 5)
print('a' > 'b')
print("bob" > "dave")

user_num = int(input("enter any nuber: "))

if user_num >10:
    print("მეტია ათზე")
elif user_num==10:
    print("უდრის ათს!")
else:
    print("ნაკლებია ათზე!")

user_score1 = float(input("შენი სასკოლო ნიშნები"))
user_score2 = float(input("კიდევ ერთთი ნიშანი"))
user_score3 = float(input("დევ ერთიც"))
user_score4 = float(input("კიდევ ერთიც"))
final_score = (user_score1+user_score2+user_score3+user_score4) / 4
if final_score >9:
   print("გილოცავ მატრიცელო. შენი ქულაა "+ str(final_score) + " შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი, რასაც შეალიე შენი ცხოვრების წლები")
elif final_score <5:
   print("გილოცავ გაექეცი მატრიცას")
elif final_score >5:
   print("YOU ARE MID")
elif final_score <9:
   print("there is something wrong with you")