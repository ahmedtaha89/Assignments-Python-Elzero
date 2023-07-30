# تكليفات الدروس من الدرس 056 إلى 059

# التكليف 01

# def calculate(num1,num2,operator='add'):
#     if operator.lower() == 'add' or  operator.lower() == 'a': 
#         return num1 + num2 
#     elif operator.lower() == 'subtract' or  operator.lower() == 's': 
#       return num1 - num2 
#     elif operator.lower() == 'multiply' or  operator.lower() == 'm': 
#         return num1 * num2 
# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "A")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30

# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10

# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200



# التكليف 02
def addition(*num):
    a = 0
    for i in num:
        if i == 10:
            continue
        elif i == 5:
            a-=5
        else:
            a+=i
    return a

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160



# التكليف 03
def show_skills(name,*skills):
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")
    else:    
        print(f"Hello {name} Your Skills Is")
        for s in skills:
            print(f"- {s}")

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("ahmed")


# التكليف 04

def say_hello(name='Unknown',age='Unknown',country='Unknown'):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
