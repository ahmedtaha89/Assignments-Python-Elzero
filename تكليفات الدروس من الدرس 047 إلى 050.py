# تكليفات الدروس من الدرس 047 إلى 050

# التكليف 01
# num = int(input())
# count = 0
# if num > 0 :
#     while num > 1:
#         num-=1
#         if num == 6 :
#             continue
#         print(num)
#         count+=1
#     print(f"{count} Numbers Printed Successfully.")
# else:
#     print("Number 0 Is Not Larger Than 0")


# التكليف 02
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
x = 0
count = 0
while x < len(friends) :

    if friends[x].islower():
        x+=1
        count+=1
    else:
        print(friends[x])
        x+=1    
        
print(f"Friends Printed And Ignored Names Count Is {count}")



# التكليف 03
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills[0]) ; del skills[0] 


# التكليف 04

my_friends = []
len_friends = 4
x = 0
while x < 4:
    name = str(input()).strip()
    if name.isupper():
        print('Invalid Name')

    elif name.islower():
        name.capitalize()
        my_friends.append(name)
        x+=1    
        print(f"Friend {name} Added => {x}st Letter Become Capital")