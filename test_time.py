from time import time
import requests 
from bs4 import BeautifulSoup

# 
def speedTest(func):
  def wrapper():
    start = time()
    func()
    end = time()
    print(f"Function Running Time Is: {(end - start)}")
  return wrapper

# 
# @speedTest
# def range_time():
#     for n in range (1,5000):
#      print(n)
# range_time()


# 
my_list=[]
@speedTest
def bigLoop():
 for seats in range(1459530,1459630):    
    response = requests.get(f'https://shbabbek.com/natega/{seats}')
    try:
     if response.status_code == 200:
         my_list.append(response.content)     
    except:
        break
    print(len(my_list)) 

print(len(my_list))
bigLoop()