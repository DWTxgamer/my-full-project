import os
import time


UserInfo = open('UserInfo.ciph','w')

Username = input('Username:')
Password = input('Password:')
User = (f'{Username}.{Password} ')

UserInfo.write(User)
UserInfo.close()

f = open('UserInfo.ciph','r')
lines = f.readlines()

for x in lines:
    # print(x)
    userlen = len(Username)
    pswdlen = len(Password)

userlogin = x[:userlen]
pswdlogin = x[userlen:pswdlen]
pswdlogin = int(pswdlogin)

print(pswdlogin)

usertry = input('LOGIN>>Username:')
pswdtry = input('LOGIN>>Password:')

if usertry == userlogin:
    print('username correct')
    print(pswdlogin)
    time.sleep(0.5)
    if pswdtry == pswdlogin:
        print('password correct')
    else:
        print('incorect pswd')
