


//multipass merge sort
nOfPages=10;
nOfBufferFrames=3;
nOfElementsInAPage=4;
rangeOfValues=100

function removeMin(toSort,newList) {
    min=rangeOfValues+1;
    argmin=-1;
    for(var i=0;i<toSort.length;i++) {
        if(toSort[i].length==0) {
            continue;
        }
        if(toSort[i][0]<min) {
            min=toSort[i][0];
            argmin=i;
        }
    }
    if(argmin==-1) {
        return null;
    }
    r=toSort[argmin].shift();
    newList.push(r);
    return r
}
  

var runs=[[]];
// create a list of random elements 
var list = [];
for (var i = 0; i < nOfPages*nOfElementsInAPage; i++) {
    list.push(Math.floor(Math.random()*rangeOfValues));
}

//create runs
for (var i =0; i < list.length; i+=nOfBufferFrames) {
    l=list.slice(i,i+nOfBufferFrames);
    l.sort()
    runs[0].push(l)
}
console.log(runs)

level=0;
do{
    //take slices of size nOfBufferFrames
    runs[level+1]=[];
    for (var i =0; i < runs[level].length; i+=nOfBufferFrames-1){
        sublistsToSort=runs[level].slice(i,i+nOfBufferFrames-1);
        
        newList=[]
        do{
            res=removeMin(sublistsToSort,newList);
        }while(res!=null);
        
        runs[level+1].push(newList);

    }

    level++;
}
while(runs[level].length == 1)

sortedList=runs[runs.length-1];
console.log(sortedList)
    