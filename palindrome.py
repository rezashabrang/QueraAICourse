import re
def reverse(s):
    return s[::-1]


def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False


n = input()
n = int(n)
pList = []
for lines in range(n):
    text = input()
    res = re.findall(r'\w+', text)
    for word in res:
        send = word.lower()
        if isPalindrome(send):
            pList.append(word)

if pList:
    print("Palindrome words in the text are: ", end="")
    t = 1
    for p in pList:
        if t == len(pList):
            print(p, end="")
        else:
            print(p, end=", ")
        t+=1

else:
    print("No palindrome words found :(")