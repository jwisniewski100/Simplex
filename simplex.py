import numpy as np
import matplotlib.pyplot as plt
import re

def drawChart(A):
    x1 = np.arange(0, 30, 0.1)
    dimension = np.shape(A)[0]

    fmin = (A[0][2] - A[0][0] * x1) / A[0][1]
    for iter in range(1, dimension-1):
        f = (A[1][2] - A[1][0] * x1) / A[1][1]
        fmin = np.minimum(fmin, f)
    fig, ax = plt.subplots(1)
    ax.fill_between(x1, fmin, 0, where=fmin >= 0, facecolor='blue', alpha=0.5)

    ax.grid()
    fig.savefig('SimplexChart.png')

def initialTableau():
    tableau = []
    objective = []

    objectivePattern = re.compile("(min|max) [0-9]+[a-z]+[0-9]+( ((\+)|(\-))[0-9]+[a-z]+[0-9]+)*$")
    constraintsPattern = re.compile("[0-9]*[a-z]+[0-9]+( (\+|\-)[0-9]*[a-z]+[0-9]+)* (<=|>=) [0-9]+$")

    objectiveCorrect = False
    while not objectiveCorrect:
        print("Objective function: eg. max 60x1 +30x2 +20x3")
        data = input("Enter function: ")
        if objectivePattern.match(data):
            objectiveCorrect = True

    data = data.split(" ")
    if data[0] == 'min' or data[0] == 'MIN':
        minFlag = True
    else:
        minFlag = False

    for i in range(1, len(data)):
        objective.append(float(re.sub('[a-z]\d*', '', data[i])))
    if minFlag:
        for j in range(0, len(c)):
            objective[j] *= -1
            # max 60x1 +30x2 +20x3
    objective.append(0)

    while True:
        print("Constraints: eg. 8x1 +6x2 +x3 <= 960")
        data = input("Enter function: ")
        if data=="stop":
            break
        if not constraintsPattern.match(data):
            print("Wrong format")
            continue
        data = data.split(" ")
        temp = []
        for i in range(0, len(data)):
            valueSubstring = re.sub('[a-z]\d*', '', data[i])
            if valueSubstring=="+":
                temp.append(1.0)
            elif valueSubstring=="-":
                temp.append(-1.0)
            elif valueSubstring=="<=":
                temp.append(float(data[i+1]))
                break
            elif valueSubstring==">=":
                temp.append(float(data[i+1]))
                for j in range(0, len(temp)):
                    temp[j] *= -1
                break
            else:
                temp.append(float(valueSubstring))
        tableau.append(temp)
        print("Type: 'stop' to end data input")

    tableau.append(objective)
    return tableau

def isLastRowNegative(tab):
    lastRow = tab[-1]
    for i in range(len(lastRow)):
        if lastRow[i] > 0:
            return True
    return False


def findPivotIndex(tableau):
    for i in range(len(tableau[-1])):
        if tableau[-1][i] > 0:
            column = i
            break

    if all(row[column] <= 0 for row in tableau):
        raise Exception('Problem is unbounded.')

    quotients = []
    for i, r in enumerate(tableau[:-1]):
        if r[column] > 0:
            value = (i, r[-1] / r[column])
            quotients.append(value)

    minElem = quotients[0]
    for i in range(len(quotients)-1):
        if quotients[i+1][1] < minElem[1]:
            minElem = quotients[i+1]
        elif quotients[i + 1][1] == minElem[1]:
            raise Exception('Linear program is degenerate.')

    row = minElem[0]
    return row, column


def calculateTableau(tableau, pivot):
    i, j = pivot
    pivotValue = tableau[i][j]

    for iter in range(len(tableau[i])):
        tableau[i][iter] = tableau[i][iter] / pivotValue

    for k, row in enumerate(tableau):
        pivotRowMultiple = []
        if k != i:
            for iter in range(len(tableau[k])):
                pivotRowMultiple.append(tableau[i][iter] * tableau[k][j])

            for iter in range(len(tableau[k])):
                tableau[k][iter] -= pivotRowMultiple[iter]


def simplex():
    tableau = initialTableau()

    if np.shape(tableau)[1]==3:
        drawChart(tableau)

    for data_slice in tableau:
        f.write(str(data_slice)+"\n")
    f.write("\n")

    while isLastRowNegative(tableau):
        pivot = findPivotIndex(tableau)
        calculateTableau(tableau, pivot)
        for data_slice in tableau:
            f.write(str(data_slice) + "\n")
        f.write("\n")
    return tableau


if __name__ == "__main__":
    c = [60, 30, 20]  # max
    A = [[8, 6, 1], [8, 4, 3], [4, 3, 1]]
    b = [960, 800, 320]
    '''c = [8, 5]  # max
    A = [[6, 10], [9, 5]]
    b = [45, 45]'''

    # add slack variables by hand
    # A[0] += [1,0]
    # A[1] += [0,1]
    # c += [0,0]

    f = open('result.txt', 'w')
    t = simplex()
    f.close()

    print("\n")
    print(t)
