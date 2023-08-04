import my_mod
print(my_mod.say_hello("ahmed"))

from my_mod import say_welcome 
print(say_welcome('ahmed'))


from my_mod import say_welcome as new_welcome
print(new_welcome('ahmed'))