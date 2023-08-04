# تكليفات الدروس من الدرس 076 إلى 078

# التكليف 01

import random 
print(f"Random Number Between 10 And 50 => {random.randint(1,50)}")
print(f"Random Even Number Between 2 And 10 => {random.randrange(2,10,2)}")
print(f"Random Odd Number Between 1 And 9 => {random.randrange(1,9,2)}")


# التكليف 02
import my_mod
print(my_mod.say_hello("ahmed"))
print(my_mod.say_welcome("ahmed"))


# التكليف 03
from my_mod import say_welcome 
print(say_welcome('ahmed'))


# التكليف 04
from my_mod import say_welcome as new_welcome
print(new_welcome('ahmed'))