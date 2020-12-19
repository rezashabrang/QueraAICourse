for j in sorted(set((x for index, x in enumerate(input().split(' ')) if (int(x) % 3 == 0 and (int(index) + 1) % 3 == 0)))): print(j, end= ' ')
