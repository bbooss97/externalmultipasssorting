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

if nOfBufferFrames < 3 :
    print("nOfBufferFrames must be greater than 2 i changed the nOfBufferFrames to 3")
    nOfBufferFrames = 3

os.system("cls")

print("number of pages: "+str(nOfPages))
print("number of buffer frames: "+str(nOfBufferFrames))
print("number of elements in a page: "+str(nOfElementsInAPage))
print("range of values: "+str(rangeOfValues))
print()

class myList(list):
    quanti=0
    def __str__(self):
        lista=list(self)
        r="["
        for i,l in enumerate(lista):
            if((i+self.quanti)%(nOfElementsInAPage)==0 and i!=0):
                r+="| "
            r+=str(l)+", "
        if len(r)>1:
            r=r[0:-2]        
        r+="]"
        return r
    def tolist(self):
        return self.lista[:]

def removeMin(toSort,newList,removed,originalList):
    minimum=rangeOfValues+1
    argmin=-1
    input()
    os.system("cls")            
    print("those are the current lists to sort: ")
    for i,l in enumerate(originalList):
        print("list "+str(i)+": "+str(l))
    print()
    for i,l in enumerate(toSort):
        print("buffer queue"+str(i)+": "+str(l))
    print()
    for i,l in enumerate(toSort):
        print("buffer "+str(i)+": "+str(l[0:nOfElementsInAPage-1-removed[i]%nOfElementsInAPage+1]))
    print("this is the newlist being produced: ")
    print(newList)
    conta=0
    for j in toSort:
        conta += int(len(str(j))/192)
    for i in range(len(toSort)):
        if len(toSort[i])==0:
            continue
        if toSort[i][0]<minimum:
            minimum=toSort[i][0]
            argmin=i
    if argmin==-1:
        return None
    r=toSort[argmin].pop(0)
    removed[argmin]+=1
    toSort[argmin].quanti+=1
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
    print("load in the buffer frames the  n "+str(int(i/(nOfBufferFrames*nOfElementsInAPage)))+" part of the list")
    print(l)
    l.sort()
    input()
    print("i sort the "+str(int(i/(nOfBufferFrames*nOfElementsInAPage)))+" part of the list in the buffer frames and i write it in the second storage") 
    print(l)
    print("\n")
    input()
    runs[0].append(l)

print("those are the sorted lists written in the second storage: ")
for i,l in enumerate(runs[0]):
    print("list "+str(i)+": "+str(l))

level=0
while True:
    runs.append(myList([]))
    conta=0
    for i in range(0,len(runs[level]),nOfBufferFrames-1):

        sublistsToSort=runs[level][i:i+nOfBufferFrames-1]

        newList=myList([])
        
        if len(sublistsToSort) == 1:
            input()
            os.system("cls")
            print("\nthere is one only list left to sort so we skip the sort and write it directly in secondary storage")
            runs[level+1].append(sublistsToSort[0])
            continue

        print("we are in the "+str(level)+" pass of the algorithm and those are the current lists to sort: \n"+str(sublistsToSort))
        removed=[0 for _ in sublistsToSort]
        sublistsToPrint=[t.copy() for t in sublistsToSort]
        while True:
            res=removeMin(sublistsToSort,newList,removed,sublistsToPrint)
            if res==None:
                conta+=1
                print("\nthis is the produced sorted list n "+str(conta)+" "+str(newList)+" that will be written in the second storage\033[J")
                break
        runs[level+1].append(newList)
    level+=1
    if len(runs[level])==1:
        break

input()
os.system("cls")
sortedList=runs[len(runs)-1]
print("\nfinal sorted list")
print(sortedList)