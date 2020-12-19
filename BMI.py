import math


def process(path):
    athletes = []
    normal_people = []
    athpeople = 0
    athBMI = 0
    normBMI = 0
    normpeople = 0
    with open(path, "r+") as file:
        for line in file:
            line = line.rstrip()
            height, weight, athlete = line.split(" ")
            height = float(height)
            weight = float(weight)
            if athlete == "ATHLETE":
                BMI = float(weight) / math.pow(int(height) / 100, 2)
                athletes.append((height, weight, BMI))
                athpeople += 1
                athBMI += BMI
            else:
                BMI = float(weight) / math.pow(int(height) / 100, 2)
                normal_people.append((height, weight, BMI))
                normpeople += 1
                normBMI += BMI
    athletes_average_bmi = float(athBMI) / float(athpeople)
    normal_average_bmi = float(normBMI) / float(normpeople)

    return athletes, athletes_average_bmi, normal_people, normal_average_bmi


process("files.txt")