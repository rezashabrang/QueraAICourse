string = input()
subString = ""
counter = 1
ans=''
t = 0
while t <= len(string)-1:
    if t == len(string)-1:
        subString += string[t]
        number = 0
        i = 1
        for chars in subString:
            number += i * (ord(chars) - 64)
            i += 1
        ans += str(number)
        break
    if string[t] == string[t + 1].upper() or string[t] == string[t + 1].lower():
        counter += 1
        subString+=string[t]
    else:
        subString+=string[t]
        number = 0
        i = 1
        for chars in subString:
            number += i*(ord(chars)-64)
            i += 1
        ans += str(number)
        counter = 1
        subString = ''
    t += 1
print(ans)

