from pyeda.inter import *
from copy import deepcopy
import logicmin
import sys


def dontCareVar(inputList, outputList):
    # no "-" in the string
    if(inputList[0].find("-") == -1):
        if(inputList not in outputList):
            outputList.append(inputList)
        return

    pos = inputList[0].find("-")

    # switch the "-" to 0 or 1
    t = list(inputList[0])
    t1 = list(inputList[0])
    t[pos] = "0"
    t1[pos] = "1"

    # put it in back to the inputList
    inputList[0] = "".join(t)
    # recursive to swich string
    dontCareVar(deepcopy(inputList), outputList)
    
    # put it in back to the inputList
    inputList[0] = "".join(t1)
    # recursive to swich string
    dontCareVar(deepcopy(inputList), outputList)


# inputFile = open(sys.argv[0], "r", encoding="utf8")
inputFile = open("input.pla", "r", encoding="utf8")
inputVar = int(inputFile.readline().split(" ")[1])
outputVar = int(inputFile.readline().split(" ")[1])

# read input variable
inputVarList = list(inputFile.readline().split(" "))
inputVarList.pop(0)
inputVarList[-1] = inputVarList[-1].replace("\n", "")

# read output variable
outputVarList = list(inputFile.readline().split(" "))
outputVarList.pop(0)
outputVarList[-1] = outputVarList[-1].replace("\n", "")

# read command
commandNumber = int(inputFile.readline().split(" ")[1])
# print(inputVar, "\n", outputVar, "\n", inputVarList, "\n", outputVarList, "\n",commandLine)

# read the follow truthtable**************
commandList = []
for i in range(commandNumber):
    temp = inputFile.readline().split(" ")
    temp[1] = temp[1].replace("\n", "")
    if(temp[0].find("-") != -1):
        dontCareVar(deepcopy(temp), commandList)
    else:
        commandList.append(temp)


# insert the truth table to the mininizer
t = logicmin.TT(inputVar, outputVar)
for i in range(commandNumber):
    t.add(commandList[i][0], commandList[i][1])
sol = t.solve()

for i in commandList:
    print(i)

print(sol.printN(xnames=[i for i in inputVarList],
      ynames=[j for j in outputVarList], info=False))

# X = exprvars('x', 4)
# f1 = truthtable(X, "0000011111------")
# print(X)


inputFile.close()
