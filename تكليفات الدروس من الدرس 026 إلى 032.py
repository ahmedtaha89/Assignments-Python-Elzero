# تكليفات الدروس من الدرس 026 إلى 032 

# التكليف 01
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[0:-1])


# التكليف 02
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)


# التكليف 03
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)

letters.discard("C")
print(letters)

my_set.clear()
print(my_set)

my_set.update('A','B')
print(my_set)


# التكليف 04
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))


# التكليف 05
Skills = {
"HTML" : "90%",
"CSS" : "80%",
"Python" : "30%"
}

print(f"HTML Progress Is {Skills['HTML']}")
print(f"CSS Progress Is {Skills['CSS']}")
print(f"Python Progress Is {Skills['Python']}")
Skills.update({"AI":"20%"})
print(f"AI Progress Is {Skills['AI']}")

