LO = input().split(" ")
order = LO[0]
type = LO[1]

if order == "food" and type == "water":
    print(0.5)
elif order == "food" and type == "dinner":
    print(1.0)
elif order == "promote" and type == "judge":
    print(50.0)
elif order == "promote" and type == "minister":
    print(80.0)
elif order == "promote" and type == "governor":
    print(100.0)
elif order == "travel" and type == "ground":
    print(45.0)
elif order == "travel" and type == "sea":
    print(58.0)
else:
    print(10.0)


