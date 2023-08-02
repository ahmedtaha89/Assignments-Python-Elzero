# تكليفات الدروس من الدرس 069 إلى 071

# التكليف 01

values = (0, 1, 2)
# if any value in value equal true return true
if any(values):
  my_var = 0 


my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
# if all values in my list equal true return true so all values in all(my_list[:4]) = true that print good 
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
  print("Good")
else:
  print("Bad")
# Good  



# التكليف 02
v = 40
my_range = list(range(v))
print(sum(my_range, v) + pow(v, v, v))  # 820




# التكليف 03

n = 21
l = list(range(n))
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
  print("Good")


# التكليف 04 


def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

def my_min(iterable):
    min_value = None
    for element in iterable:
        if min_value is None or element < min_value:
            min_value = element
    return min_value

def my_max(iterable):
    max_value = None
    for element in iterable:
        if max_value is None or element > max_value:
            max_value = element
    return max_value


# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700 