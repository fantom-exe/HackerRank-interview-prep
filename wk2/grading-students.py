#!/bin/python3


def gradingStudents(grades):
    for i in range(len(grades)):
        grade = grades[i]

        if grade > 40:
            nearest = grade % 5
            if nearest >= 3:
                grades[i] += (5 - nearest)

    return grades


grades = [84, 29, 57, 40, 58, 11, 57, 59]
print(gradingStudents(grades))
