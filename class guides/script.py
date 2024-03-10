############################################################################

# formating in python

############################################################################

# libraries/tockens
# input

test = []

name = input('Name:')
age = input('Age:')
region = input('Region:')
main = (f'{name} {age} {region} ')
print(main)

while True:
    text = input(f'{name}> ')
    test.append(f'{name}:{text} ')
    # print code for the test library or for loop
    print(test)