
def dists_diff(dist_1,dist_2):
    sumA = 0
    sumB = 0
    for i in dist_1:
        sumA+=i
    for j in dist_2:
        sumB+=j
    return sumA-sumB
