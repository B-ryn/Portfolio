"""
A neuroscientist by the name of Andrew Huberman declared that the best way to reinforce a behavior is to reward an action 1/3rd of the time. 
This is called random intermittent reinforcement and it is one of the most effective ways to reinforce a behavior. 
Even casinos know this as they let the user win 1/3rd of the time with their gambles.

This program is designed to mimicate that random intermittent reinforcement so that the user can use it to their advantage. 
"""

# Importing libraries
import random
from fractions import Fraction

# Declaring the varibles
num_input = None

reward_num = None

# The paragraph indicating the title and instructions
greeting = 'Welcome to the Dopamine Reward Program!!!\n\n' \
           'Please type in the letter correlating to the diffculity that you wish to recieve your reward by!\n\n' \
           'A) Easy\n' \
           'B) Medium\n' \
           'C) Hard\n' \

print(greeting)


# The varibles that determine the difficulty of the reward
easy = random.randrange(1, 6)

medium = random.randrange(1, 15)

hard = random.randrange(1, 21)


# While loop that verifys if the user is implementing the right choices
while True:
    num_input = input('Your choice: ')
    num_input = num_input.upper()
    if num_input in ('A', 'B', 'C'):
        break
    else:
        print('\nPlease choose one of the following:\n'
              'A) Easy\n'
              'B) Medium\n'
              'C) Hard\n')
        continue


# If statement that figures the input and correlates the input to the difficulty and creates the reward
# by multiplying the max number with 1/3rd
if num_input == 'A':
    num_input = easy
    reward_num = Fraction(1, 3) * 6
elif num_input == 'B':
    num_input = medium
    reward_num = Fraction(1, 3) * 15
elif num_input == 'C':
    num_input = hard
    reward_num = Fraction(1, 3) * 21


# The end statment where it declares if you got the reward or not and indicates what you need and what you recieved
if num_input <= reward_num:
    print("Reward!")
    print("Needed under " + str(reward_num))
    print("You got " + str(num_input))
else:
    print('No Reward!')
    print("Needed equal or under " + str(reward_num))
    print("You got " + str(num_input))