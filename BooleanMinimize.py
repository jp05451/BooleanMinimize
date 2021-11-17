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
#***********************************************
# print(sys.argv)


inputFile = open(sys.argv[1], "r", encoding="utf8")
# inputFile = open("input.pla", "r", encoding="utf8")
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

# read the follow truthtable**************
commandList = []
for item in range(commandNumber):
    temp = inputFile.readline().split(" ")
    temp[1] = temp[1].replace("\n", "")
    if(temp[0].find("-") != -1):
        dontCareVar(deepcopy(temp), commandList)
    else:
        commandList.append(temp)
inputFile.close()
#***********************************************************
# insert the truth table to the mininizer
t = logicmin.TT(inputVar, outputVar)
for item in commandList:
    t.add(item[0], item[1])
sol = t.solve()

# for item in commandList:
#     print(item)
out = sol.printN(xnames=[i for i in inputVarList],
                 ynames=[j for j in outputVarList], info=False)

#*********************************************************************
# rebuild pla
# outputFile = open("output.pla", "w+", encoding="utf8")
outputFile = open(sys.argv[2], "w+", encoding="utf8")
temp = out.split("<=")
temp.pop(0)
out = temp[0]
VarOfInput = set(out.replace("'", "").replace(
    " ", "").replace(".", "").replace("+", ""))

# .i inputVar
outputFile.write(f".i {str(len(VarOfInput))}\n")

# .o outputVar
outputFile.write(f".o {str(outputVar)}\n")

# .lib VarOfInput
outputFile.write('.lib ')
VarOfInput = sorted(VarOfInput)
for item in VarOfInput:
    outputFile.write(f'{str(item)} ')
outputFile.write("\n")

# .ob OutputVar
outputFile.write(".ob ")
for item in outputVarList:
    outputFile.write(f'{str(item)} ')
outputFile.write("\n")

# .p command times
outCommand = out.split("+")
outputFile.write(f".p {str(len(outCommand))} \n")

# for item in outCommand:
#     print(item)

# script
for i in range(len(outCommand)):
    outCommand[i] = outCommand[i].replace(" ", "").split(".")
for i in range(len(outCommand)):
    boolean = [None]*len(VarOfInput)

    for j in range(len(outCommand[i])):
        boolean[VarOfInput.index(outCommand[i][j][0])]=outCommand[i][j]
    for item in boolean:
        if(item == None):
            outputFile.write("-")
        elif("'" in item):
            outputFile.write("0")
        else:
            outputFile.write("1")
    outputFile.write(" 1\n")
    
outputFile.write(".e")
outputFile.close()
