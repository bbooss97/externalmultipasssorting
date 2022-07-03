import time
import random
import sys
import os
nOfPages=10
nOfBufferFrames=3
nOfElementsInAPage=10
rangeOfValues=100

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sleep():
    time.sleep(1)

def removeMin(toSort,newList):
    minimum=rangeOfValues+1
    argmin=-1
    for i in range(len(toSort)):
        if len(toSort[i])==0:
            continue
        if toSort[i][0]<minimum:
            minimum=toSort[i][0]
            argmin=i
    if argmin==-1:
        return None
    r=toSort[argmin].pop(0)
    newList.append(r)
    return r

runs=[[]]
listOfNumbers=[]
for i in range(0,nOfPages*nOfElementsInAPage):
    listOfNumbers.append(random.randint(0,rangeOfValues))
print("this is the initial list: "+str(listOfNumbers))

for i in range(0,len(listOfNumbers),nOfBufferFrames):
    l=listOfNumbers[i:i+nOfBufferFrames]
    l.sort()
    runs[0].append(l)
#print("those are the sorted lists: "+str(runs[0]))

#clear console


level=0
while True:
    runs.append([])
    for i in range(0,len(runs[level]),nOfBufferFrames-1):
        sublistsToSort=runs[level][i:i+nOfBufferFrames-1]
        newList=[]
        while True:
            res=removeMin(sublistsToSort,newList)
            if res==None:
                break
        runs[level+1].append(newList)
    level+=1
    if len(runs[level])==1:
        break


sortedList=runs[len(runs)-1]
print("final sorted list")
print(sortedList)

