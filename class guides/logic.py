Userinfo = []

Username = input('Username>>')
Pswd = input('Password>>')
Userinfo.append(f'{Username} {Pswd}')

username_len = len(Username)
pswd_len = len(Pswd)
main = f'{username_len} {pswd_len} '

for x in Userinfo:
    print(len(x))
    zlen = len(x)
    xlen = pswd_len
    minlen = zlen-xlen
    ylen = username_len

print(Userinfo[:ylen+1])
print(minlen)
print(Userinfo)