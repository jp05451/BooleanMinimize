# from pyeda.inter import *
import logicmin
import sys


def dontCareVar(inputList, outputList):
    if(inputList[0].find("-") == -1):
        outputList.append(inputList)
        # print(inputList)
        return

    pos = inputList[0].find("-")

    t = list(inputList[0])
    t1 = list(inputList[0])
    t[pos] = "0"
    t1[pos] = "1"

    inputList[0] = "".join(t)
    dontCareVar(inputList, outputList)

    inputList[0] = "".join(t1)
    dontCareVar(inputList, outputList)


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
        dontCareVar(temp, commandList)


# print(commandList)
print()

# insert the truth table to the mininizer
t = logicmin.TT(inputVar, outputVar)
for i in range(commandNumber):
    t.add(commandList[i][0], commandList[i][1])
sol = t.solve()

print(sol.printN(xnames=["a", "b", "c", "d"], ynames=["y"], info=True))


inputFile.close()
