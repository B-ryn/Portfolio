import random
from fractions import Fraction


num_input = None

reward_num = None

greeting = 'Welcome to the Dopamine Reward Program!!!\n\n' \
           'Please type in the letter correlating to the diffculity that you wish to recieve your reward by!\n\n' \
           'A) Easy\n' \
           'B) Medium\n' \
           'C) Hard\n' \

print(greeting)

easy = random.randrange(1, 6)

medium = random.randrange(1, 15)

hard = random.randrange(1, 21)


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



print(num_input)
print('pre if: ' , str(easy) , str(medium) , str(hard))


# Maybe put this in a function to make it look cleaner?
if num_input == 'A':
    num_input = easy
    reward_num = Fraction(1, 3) * 6
elif num_input == 'B':
    num_input = medium
    reward_num = Fraction(1, 3) * 15
elif num_input == 'C':
    num_input = hard
    reward_num = Fraction(1, 3) * 21


if num_input <= reward_num:
    print("Reward!")
    print("Needed under " + str(reward_num))
    print("Got " + str(num_input))
else:
    print('No Reward!')
    print("Needed equal or under " + str(reward_num))
    print("Got " + str(num_input))