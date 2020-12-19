string = input()
ans = ""
counter = 1
t = 0
while t <= len(string)-1:
    if t == len(string)-1:
        ans+=string[t]+str(counter)
        break
    if string[t] == string[t + 1]:
        counter += 1
    else:
        ans += string[t] + str(counter)
        counter = 1
    t += 1
print(ans)
