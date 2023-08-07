# تكليفات الدروس من الدرس 081 إلى 085

# التكليف 01
# def reverse_string(my_string):
#      for letter in my_string[-1::-1]:
#          yield letter
# for c in reverse_string("Elzero"):
#   print(c)



# التكليف 02

def New_Decorator(drink):
   
    def Sugar():      
     
     print("Sugar Added From Decorators")
     drink()
     print("####################")
    return Sugar


@New_Decorator
def make_tea():
  print("Tea Created")

@New_Decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()

