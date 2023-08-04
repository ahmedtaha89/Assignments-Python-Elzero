# تكليفات الدروس من الدرس 072 إلى 075

# التكليف 01

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"] 
# #  بإستخدام العادية Function
# def remove_chars(frineds):
#   return frineds[1:-1]

# cleaned_list = map(remove_chars,friends_map)
# for v in cleaned_list:
#     print(v)

# # بإستخدام Lambda Function
# for v in map(lambda frineds: frineds[1:-1],friends_map) :
#     print(v)  



# التكليف 02

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
def last_char(frineds):
   return frineds.endswith('m')

# with ordinary function
for f in filter(last_char,friends_filter):
   print(f)

# With lambda Function 
for f in filter(lambda frineds: frineds.endswith('m'),friends_filter):
   print(f)



# التكليف 03

from functools import reduce
nums = [2, 4, 6, 2]
def calc_nums(num1,num2):
   return num1*num2
result = reduce(calc_nums, nums)
print(result)

# التكليف 04

