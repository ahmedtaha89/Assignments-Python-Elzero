# تكليفات الدروس من الدرس 021 إلى 023

# التكليف 01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])


# التكليف 02
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0::2])
print(friends[1::2])


# التكليف 03
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[3:5])


# التكليف 04
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends.remove('Mahmoud')
friends.remove('Ali')
friends.append('Elzero')
friends.append('Elzero')
print(friends)


# التكليف 05
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,'Nasser')
print(friends)
friends.append('Salem')
print(friends)


# التكليف 06
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.pop(0)
friends.pop(1)
print(friends)

friends.pop(-1)
print(friends)


# التكليف 07
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)


# التكليف 08
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort(reverse=False)
print(friends)
friends.sort(reverse=True)
print(friends)


# التكليف 09
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))


# التكليف 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])