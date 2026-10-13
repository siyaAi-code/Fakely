import the random module
import random

# create subjects
Subjects  =(
     "Shahrukh khan" ,
     "Virat Kohli",#
     "Nirmala Sitharman",
     "A Mumbai cat",
     "A groups of Monkeys,"
     "Prime Minister Modi,"
     "Auto Ricshaw Driver from Delhi"
     "Rahul gandhi"
)

actions =(
    "Cake cutting",
    "Dances with",
     "banana",
     "Celebrates",
     "launches a protest,"
    "playing in cricket"

)

Places_or_things =(
    "Red Fort",
    "trees in Banana",
     "plate in Samosa",
      "Gangha ghat",
       "monkeys stealing its vada pav",
       "World Cup"
)
while True:
   chosen_subjects = random.choice(list(Subjects))
   chosen_actions=  random.choice(list(actions)) 
   chosen_Places_or_things = random.choice(list( Places_or_things))   

   headline =f" BREAKING NEWS: { chosen_subjects} {chosen_actions} {chosen_Places_or_things} "
   print("\n"+ headline)
   input_user =input("\nDo you  want another headline?(yes/no)").strip()
   if input_user =="no":
        break
print("\nThanks for using the Fake News headline Generator.have a fun day")
