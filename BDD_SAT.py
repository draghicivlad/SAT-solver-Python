import datetime

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        
def evaluateLevel(tree, level, variables):

    if level == len(variables):
        return False

    actEquation = tree.data

    newEquationT = []
    newEquationF = []
    for i in range(0, len(actEquation)):
        newEquationT.append(actEquation[i].copy())
        newEquationF.append(actEquation[i].copy())

    variableToEval = variables[level]

    tree.right = Tree()

    i = -1
    while i < len(newEquationT) - 1:
        i = i + 1

        literalValue = newEquationT[i].get(variableToEval)
        if literalValue == None:
            continue

        if literalValue == 1:
            del newEquationT[i]
            i = i - 1
            continue
        else:
            newEquationT[i].pop(variableToEval)

        if len(newEquationT[i]) == 0:
            tree.right.data = False

    if len(newEquationT) == 0:
        tree.right.data = True
        return True

    if(tree.right.data == None):
        tree.right.data = newEquationT
        if evaluateLevel(tree.right, level + 1, variables) == True:
            return True

    tree.left = Tree()
    i = -1
    while i < len(newEquationF) - 1:
        i = i + 1

        literalValue = newEquationF[i].get(variableToEval)
        if literalValue == None:
            continue

        if literalValue == -1:
            del newEquationF[i]
            i = i - 1
            continue
        else:
            newEquationF[i].pop(variableToEval)

        if len(newEquationF[i]) == 0:
            tree.left.data = False

    if len(newEquationF) == 0:
        tree.left.data = True
        return True
    
    if(tree.left.data == None):
        tree.left.data = newEquationF
        if evaluateLevel(tree.left, level + 1, variables) == True:
            return True

    return False

def BDD_SAT(equation):
    clauses = equation.split("^")
    variables = []
    equationFormated = []

    for i in range(0, len(clauses)):
        equationFormated.append({})
        actClause = clauses[i]
        actClause = actClause.split("(")[1]
        actClause = actClause.split(")")[0]

        literals = actClause.split("V")
        literals = list(filter(None, literals))

        for j in range(0, len(literals)):
            actLiteral = literals[j]
            if(actLiteral[0] == "~"):
                actVariable = actLiteral[1:]
                value = -1
            else:
                actVariable = actLiteral
                value = 1

            index = -1
            for k in range(0, len(variables)):
                if(actVariable == variables[k]):
                    index = k
                    break

            if(index == -1):
                index = len(variables)
                variables.append(actVariable)

            equationFormated[i].update({actVariable : value})

    nrVar = len(variables)
    print(str(nrVar) + "\t", end = "")

    root = Tree()
    root.data = equationFormated
    ans = evaluateLevel(root, 0, variables)
    return ans

def printTree(tree, level):
    if tree == None:
        return

    print("level", end ="") 
    for _ in range(0, level):
        print("\t", end ="") 
    print(tree.data)

    printTree(tree.left, level + 1)
    printTree(tree.right, level + 1)

equation = input()

start_time = datetime.datetime.now()

ans = BDD_SAT(equation)

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)

print(time_diff.total_seconds())