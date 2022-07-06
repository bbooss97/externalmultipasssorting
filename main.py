import time
import random
import sys
import os
nOfPages=10
nOfBufferFrames=3
nOfElementsInAPage=2
rangeOfValues=100

#insert nOfPages
nOfPages=int(input("insert nOfPages: "))
#insert nOfBufferFrames
nOfBufferFrames=int(input("insert nOfBufferFrames: "))
#insert nOfElementsInAPage
nOfElementsInAPage=int(input("insert nOfElementsInAPage: "))
#insert rangeOfValues
rangeOfValues=int(input("insert rangeOfValues: "))

print("number of pages: "+str(nOfPages))
print("number of buffer frames: "+str(nOfBufferFrames))
print("number of elements in a page: "+str(nOfElementsInAPage))
print("range of values: "+str(rangeOfValues))
print()

class myList(list):
    def __str__(self):
        lista=list(self)
        r="["
        for i,l in enumerate(lista):
            if(i%(nOfElementsInAPage)==0 and i!=0):
                r+="| "
            r+=str(l)+", "
        if len(r)>1:
            r=r[0:-2]        
        r+="]"
        return r

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
    print("\033[J",end="")
    print("those are the lists: ")
    for i,l in enumerate(toSort):
        print("list "+str(i)+": "+str(l))
    print("this is the newlist : ")
    print(newList)
    goBack="\033[A"*(len(toSort)+4)+"\033[F"
    print(goBack)

    # for i in range(len(toSort)+3):
    #     print ("\033[A\033[A") 
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

runs=[myList([])]
listOfNumbers=myList([])
for i in range(0,nOfPages*nOfElementsInAPage):
    listOfNumbers.append(random.randint(0,rangeOfValues))
print("this is the initial list: "+str(listOfNumbers))
input()

for i in range(0,len(listOfNumbers),nOfBufferFrames*nOfElementsInAPage):
    l=myList(listOfNumbers[i:i+nOfBufferFrames*nOfElementsInAPage])
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
    runs.append(myList([]))
    conta=0
    for i in range(0,len(runs[level]),nOfBufferFrames-1):
        sublistsToSort=runs[level][i:i+nOfBufferFrames-1]
        newList=myList([])
        print("those are the lists to sort: \n"+str(sublistsToSort))
        while True:
            res=removeMin(sublistsToSort,newList)
            if res==None:
                conta+=1
                print("this is the sorted list n "+str(conta)+" "+str(newList)+"\n\033[J")
                break
        runs[level+1].append(newList)
    level+=1
    if len(runs[level])==1:
        break


sortedList=runs[len(runs)-1]
print("\nfinal sorted list")
print(sortedList)

