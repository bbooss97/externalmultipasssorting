import time
import random
import sys
import os
nOfPages=10
nOfBufferFrames=3
nOfElementsInAPage=2
rangeOfValues=100
print("number of pages: "+str(nOfPages))
print("number of buffer frames: "+str(nOfBufferFrames))
print("number of elements in a page: "+str(nOfElementsInAPage))
print("range of values: "+str(rangeOfValues))
print()

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sleep():
    time.sleep(3)

def removeMin(toSort,newList):
    minimum=rangeOfValues+1
    argmin=-1
    input()
    print("those are the lists: ")
    for i,l in enumerate(toSort):
        print("list "+str(i)+": "+str(l))
    print("this is the newlist : ")
    print(newList)
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
print("\n")
input()

for i in range(0,len(listOfNumbers),nOfBufferFrames*nOfElementsInAPage):
    l=listOfNumbers[i:i+nOfBufferFrames*nOfElementsInAPage]
    print("elements in list n "+str(int(i/(nOfBufferFrames*nOfElementsInAPage))))
    print(l)
    l.sort()
    input()
    print("sorted list n "+str(int(i/(nOfBufferFrames*nOfElementsInAPage))))
    print(l)
    print("\n")
    input()
    runs[0].append(l)
#print("those are the sorted lists: "+str(runs[0]))

print("those are the sorted lists: ")
for i,l in enumerate(runs[0]):
    print("list "+str(i)+": "+str(l))


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
print("\nfinal sorted list")
print(sortedList)

