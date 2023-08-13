import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images=[rock,paper,scissors]
user_choose=int(input("What do you choose: Type 0:Rock 1:Paper 2:Scissors\n"))
if user_choose>=3 or user_choose<0:
  print("Invalid")
else:
  print(game_images[user_choose])
  print("Computer chooses")
  computer_choose=random.randint(0,2)
  print(game_images[computer_choose])
  if(user_choose==computer_choose):
    print("Draw")
  elif(user_choose==0 and computer_choose==1):
    print("Computer Wins...")
  elif(user_choose==0 and computer_choose==2):
    print("You Wins...")
  elif(user_choose==1 and computer_choose==0):
    print("You Wins....")
  elif(user_choose==1 and computer_choose==2):
    print("Computer Wins...")
  elif(user_choose==2 and computer_choose==0):
    print("Computer Wins...")
  elif(user_choose==2 and computer_choose==1):
    print("You Wins...")