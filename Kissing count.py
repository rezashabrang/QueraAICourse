def addn(num):
    sum = 0
    i = 1

    while i <= num:
        sum = sum + i
        i = i + 1
    return sum
n = input()
roomlist = {}
ans = []
for i in range(int(n)):
    room = input()
    if room not in roomlist:
        roomlist[room] = 0
        ans.append(0)
    else:
        roomlist[room] += 1
        sum = 0
        for i in range(1,roomlist[room]+1):
            sum += addn(i)
        ans.append(sum)
for answers in ans:
    print(answers)
