
name = input('Name:')
a = input(f'Hello {name},When were you born:')
b = input(f'{name},We would like to know your address:')
c = input("Do you attend School?(Y/N):")
d = input("Do you go to church?(Y/N):")
age = int(input(f'{name},We would like to know your age:'))

if age >= 18:
    print(f'Thanks for your time {name} you were born in {a} \n you live in {b}, Attending schol {c} Fellowship in church {d} ')
    print(f'according to you age {age},You are an adult')

elif age < 0:
    print(f'Thanks for your time {name} you were born in {a} \n you live in {b}, Attending schol {c} Fellowship in church {d} ')
    print(f'according to you age {age},You are not born yet')

else:
    print(f'Thanks for your time {name} you were born in {a} \n you live in {b}, Attending schol {c} Fellowship in church {d} ')
    print(f'according to you age {age},You are a child')

f = open('UserInfo.txt','w')
f.write(f'{name} {a} {b} {c} {d} {age} ')
f.close()
