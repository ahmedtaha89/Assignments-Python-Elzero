# تكليفات الدروس من الدرس 041 إلى 046

# التكليف 01
num1 = int(input().strip())
operation = str(input('Choose the operation "+" Or "-" Or "*" Or "/" Or "%" : ').strip())
num2 = int(input().strip())
if operation == '+':
    print(num1+num2)

elif operation == '-':
    print(num1-num2)

elif operation == '*':
    print(num1*num2)

elif operation == '/':
    print(num1/num2)

elif operation == '%':
    print(num1%num2)


# #التكليف 02 
age = 17
print("App Is Suitable For You" if  age > 16 else "App Is Not Suitable For You")


# التكليف 03
age = int(input())
if age > 10 and age < 100:

    months = age * 12 
    weeks = months * 4
    days = weeks * 7
    hours = days * 24
    mintues = hours * 60
    seconds = mintues * 60

    print(f"Your Age In Months Is {months} Months")
    print(f"Your Age In Weeks Is {weeks} Weeks")
    print(f"Your Age In Days Is {days} Days")
    print(f"Your Age In Hours Is {hours} Hours")
    print(f"Your Age In Mintues Is {mintues} Mintues")
    print(f"Your Age In Seconds Is {seconds} Seconds")

else:
    print("Not Available")



# التكليف 04
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")    