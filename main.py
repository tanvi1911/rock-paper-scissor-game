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
game_elements = [rock, paper, scissors]
ref = len(game_elements) - 1

# For You
Your_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(f"Your Choice\n{game_elements[Your_Choice]}")

# For Computer

Computer_Choice = random.randint(0, ref)
print(f"Mr.Computer's Choice\n{game_elements[Computer_Choice]}")

if Computer_Choice == 0 and Your_Choice == 1:  
  print("You Win!!")                                
elif Computer_Choice == 0 and Your_Choice == 2:      
  print("You Lose.")
elif Computer_Choice == 1 and Your_Choice == 0:
  print("You Lose!!")
elif Computer_Choice == 1 and Your_Choice == 2:
  print("You Win!!")
elif Computer_Choice == 2 and Your_Choice == 0:
  print("You Win!!")
elif Computer_Choice == 2 and Your_Choice == 1:
  print("You lose")
else: 
  print("It's a draw.")
