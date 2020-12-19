n, x, k = map(int, input().split())
channels = []
step = 0
for i in range(n):
    channels.append(input())
j = x - 1
for k in range(x - 1, n):
    step += 1
    j += 1
    if step <= k and j == n - 1:
        j = -1
    if step > k:
        print(channels[j])
        break
