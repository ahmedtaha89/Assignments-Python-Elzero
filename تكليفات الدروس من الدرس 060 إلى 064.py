# تكليفات الدروس من الدرس 060 إلى 064

# التكليف 01
def get_score(**subjects):
    for subject , score in subjects.items():
     print(f"{subject} => {score}")
get_score(Math=90, Science=80, Language=10)     
get_score(Logic=70, Problems=60)


# التكليف 02
def get_people_scores(name,**subjects):
   if bool(name):
     print(f"Hello {name} This Is Your Score Table:")
     for sub_name , score in subjects.items():
         print(f"{sub_name} => {score}")
   else:
      print(f"Hello {name} You Have No Scores To Show") 
get_people_scores("Osama", Math=90, Science=80, Language=70)


# التكليف 03
scores_list = {
"Math" : 90,
"Science" : 80,
"Language": 70,
}
def get_the_scores(*name,**scores_list) :
         if len(scores_list) > 0:
          if bool(name):  
             print(f"Hello {name} This Is Your Score Table:")
          for subject ,score in scores_list.items():
                print(f"{subject} => {score}")
         else:
            print(f"Hello {name} You Have No Scores To Show") 
get_the_scores(**scores_list)
