#დავპრინტოთ 1-30ამდე რიცხვები, while loop-ის გამოყენებით, კონსოლში ყოველი რიცხვის შემდეგ დაეწეროს ლუწია თუ კენტი.

number = 1
while number <= 30:
    number = (number)+ 1
    if number % 2 == 0 :
        print(str(number) + "Luwi")
    else:
        print(str(number) + "Kenti")