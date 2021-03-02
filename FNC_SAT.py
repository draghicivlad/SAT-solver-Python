import sys
import datetime

def FNC_SAT(equation):
    clauses = equation.split("^")
    varibles = []
    matrix = []

    for i in range(0, len(clauses)):
        matrix.append([])

        actClause = clauses[i]
        actClause = actClause.split("(")[1]
        actClause = actClause.split(")")[0]

        literals = actClause.split("V")

        for j in range(0, len(literals)):
            actLiteral = literals[j]
            if(actLiteral[0] == "~"):
                actVariable = actLiteral[1:]
                value = -1
            else:
                actVariable = actLiteral
                value = 1

            index = -1
            for k in range(0, len(varibles)):
                if(actVariable == varibles[k]):
                    index = k
                    break

            if(index == -1):
                index = len(varibles)
                varibles.append(actVariable)

            if index >= len(matrix[i]):
                while(index > len(matrix[i])):
                    matrix[i].append(0)
                matrix[i].append(value)
            else:
                del matrix[i][index]
                matrix[i].insert(index, value)
        
        while(len(matrix[i]) < len(varibles)):
            matrix[i].append(0)

    nrVar = len(varibles)

    print(str(nrVar) + "\t", end = "")

    queue = []
    queue.append([])

    while(len(queue) != 0):
        currentList = queue.pop()

        if(len(currentList) == nrVar):
            okMatrix = True
            for i in range(0, len(matrix)):
                okRow = False
                currentRow = matrix[i]

                for j in range(0, len(currentRow)):
                    if(currentList[j] * currentRow[j] == 1):
                        okRow = True
                        break
                
                if(okRow == False):
                    okMatrix = False
                    break
            if(okMatrix == True):
                return 1
        else:
            newListT = currentList.copy()
            newListF = currentList.copy()
            newListT.append(1)
            newListF.append(-1)
            queue.append(newListT)
            queue.append(newListF)
    return 0

equation = input()

start_time = datetime.datetime.now()

FNC_SAT(equation)

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)

print(time_diff.total_seconds())