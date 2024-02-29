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
else final_score <9:
   print("there is something wrong with you")