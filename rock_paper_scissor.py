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
game_image=[rock,paper,scissors]
user_choice=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissor \n"))
if user_choice >=3 or user_choice < 0:
  print("you type an invalid number, you loose")
else:
 print(game_image[user_choice])
computer_choice=random.randint(0,1)
print("computer choose ")
print(game_image[computer_choice])

if user_choice ==0 and computer_choice==2:
  print("you win")
elif computer_choice==0 and user_choice==2:
  print("you lose")
elif computer_choice > user_choice:
  print("you lose")
elif user_choice > computer_choice:
  print("you win")
elif computer_choice == user_choice:
  print("its draw")


