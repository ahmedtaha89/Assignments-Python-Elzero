# تكليفات الدروس من الدرس 038 إلى 040

# التكليف 01
name  = input().strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")


# التكليف 02
age = int(input())
if age < 16 :
    print(f"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You") 
elif age >= 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


# التكليف 03 
first_name = input().strip().capitalize()
second_name  = input().strip().capitalize()
print(f"Hello {first_name} {second_name[0]}.")


# التكليف 04
email = input().strip().lower()
print(f"Your Name Is {email[:email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email[email.index('@')+1:email.index('.')]}")
print(f"Top Level Domain Is {email[email.index('.')+1:].capitalize()}")