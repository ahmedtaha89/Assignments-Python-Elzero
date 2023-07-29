# تكليفات الدروس من الدرس 011 إلى 018

# التكليف 01
Name = 'Ahmed'
Age = 21 
Country = 'Egypt'

print(f"\"Hello \'{Name}\', How You Doing \ \"\"\" Your Age Is \"{Age}\"\" + And Your Country Is: {Country}")


# التكليف 02
print(f"""\"Hello \'{Name}\', How You Doing \\
\"\"\" Your Age Is \"{Age}\"\" +
And Your Country Is: {Country}""")


# التكليف 03
Name = 'Elzero'

print(Name[1])
print(Name[2])
print(Name[-1])


# التكليف 04
Name = 'Elzero'

print(Name[1:4])
print(Name[0::2])
print(Name[4::-2])


# التكليف 05
Name = "#@#@Elzero#@#@"
print(Name.strip("#@"))


# التكليف 06
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))


# التكليف 07
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20,'@'))
print(name_two.rjust(20,'@'))


# التكليف 08
name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())


# التكليف 09
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))


# التكليف 10
name = "Elzero"
print(name.index('z'))


# التكليف 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3','Love',1))


# التكليف 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3','Love'))


# التكليف 13
name = "Osama"
age = 38
country = "Egypt"

print(f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}')