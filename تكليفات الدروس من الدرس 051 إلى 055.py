# تكليفات الدروس من الدرس 051 إلى 055

# التكليف 01
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# x = 0
# for i in my_nums:
#     if i % 5 == 0:
#         x+=1
#         print(f"{x} => {i}")
# print("All Numbers Printed")


# التكليف 02
# for i in range(1,21):
#     if i in [6,8,12]:
#      continue
#     if i < 10:
#         print(f"0{i}")
#     else:
#         print(f"{i}")  
# print("All Numbers Printed")    


# التكليف 03
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }

# total = 0
# rank = {
# "A" : 100,
# "B" : 80,
# "C" : 40
# }

# for key , value in my_ranks.items():
#     print(f"My Rank in {key} Is {value} And This Equal {rank[value]} Points")
#     total += rank[value]
# print(f"Total Points Is {total}")



# التكليف 04

# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

total = 0
ranks = {
"A" : 100,
"B" : 80,
"C" : 40,
"D" : 20
}

for name , data in students.items():
    print('-'*20)
    print(f"-- Student Name => {name}")
    print('-'*20)
    for subject , rank in data.items():
        print(f"- {subject} => {ranks[rank]} Points")
        total += ranks[rank]
    print(f"Total Points Is {total}")



"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"

