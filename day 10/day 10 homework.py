#დავალება:
#შექმენით ფუნქცია რომელსაც გადაეცემა 3 პარამეტრი(სამკუთხედის გვერდები) 
#და დაპრინტავს "ასეთი სამკუთხედი იარსებებს", 
#ან დაპრინტავს "ასეთი სამკუთხედი ვერ იარსებებს" )


#შექმენით ფუნქცია რომელსაც გადაეცემა სამი სახელი (სამი პარამეტრი) და დაპრინტავს ამ სახელებისგან სიას ( join ან split) გაიხსენეთ

def samkutxedis_fartobi(gverdis_sigrdze,gverdis_sigrdze2,gverdis_sigrdze3):
    print(gverdis_sigrdze * gverdis_sigrdze2 * gverdis_sigrdze3)

samkutxedis_fartobi(8,9,12)

saxeli = ",".join(["nika", "jeko", "datvit"])
print(saxeli)