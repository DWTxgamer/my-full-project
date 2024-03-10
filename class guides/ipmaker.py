import random

name = input('name>>')

x = random.randint(1000,10000)
fname = 'WinnerCredits.~ciph~'

f = open('WinnerCredits.~ciph~','w')

f.write(f'Congratulations {name} you won {x} and will recive a {fname} creddits file shortly,\n enjoy \n ###crfDarrd{x}')