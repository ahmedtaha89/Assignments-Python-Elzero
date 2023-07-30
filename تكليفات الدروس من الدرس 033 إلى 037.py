# تكليفات الدروس من الدرس 033 إلى 037

# التكليف 01
print(bool(100))
print(bool("ahmed"))
print(bool(True))
print(bool((1,2,3)))

print(bool(0))
print(bool(""))
print(bool(False))
print(bool(()))


# التكليف 02
html = 80
css = 60
javascript = 70
print(bool(html >  50 and css > 50 and javascript > 50))


# التكليف 03
num_one = 10
num_two = 20
num = 20
print(bool(num > num_one or num > num_two))
print(bool(num > num_one and num > num_two))


# التكليف 04
num_one = 10
num_two = 20

result  = num_one + num_two
print(result)
Exponent = result**3
print(Exponent)
mod = Exponent % 26000
print(mod)
divion = mod/5
print(divion)
print(type(str(divion)))
