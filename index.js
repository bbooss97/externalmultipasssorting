//multipass merge sort
nOfPages=100;
nOfBufferFrames=6;
nOfElementsInAPage=10;
rangeOfValues=100

function removeMin(toSort,newList) {
    min=rangeOfValues+1;
    argmin=-1;
    for(var i=0;i<toSort.length;i++) {
        if(toSort[i].length==0) {
            continue;
        }
        if(toSort[i][0]<=min) {
            min=toSort[i][0];
            argmin=i;
        }
    }
    if(argmin==-1) {
        return null;
    }
    r=toSort[argmin].shift();
    newList.push(r);
    // console.log(newList);
    return r
}
  
var runs=[[]];
// create a list of random elements 
var list = [];
for (var i = 0; i < nOfPages*nOfElementsInAPage; i++) {
    list.push(Math.floor(Math.random()*rangeOfValues));
}
console.log("this is the initial list: " + list);

//create first runs
for (var i =0; i < list.length; i+=nOfBufferFrames) {
    l=list.slice(i,i+nOfBufferFrames);
    l.sort(function(a, b) {
        return a - b;
    });
    runs[0].push(l)
}
console.log("those are the sortedlists"+runs[0])
console.log(runs)


//multipass merge 
level=0;
do{
    //take slices of size nOfBufferFrames
    runs[level+1]=[];
    for (var i =0; i < runs[level].length; i+=(nOfBufferFrames-1)){
        sublistsToSort=runs[level].slice(i,i+nOfBufferFrames-1);   
        newList=[]
        //copy the sublist to preserve the datastructure 
        copyOfSublist=[];
        for (var j = 0; j < sublistsToSort.length; j++) {
            copyOfSublist.push(Array.from(sublistsToSort[j]));
        }
        //linear merge using output 
        do{
            res=removeMin(copyOfSublist,newList);
        }while(res!=null);
        runs[level+1].push(newList);
    }
    //go onto the next level
    level++;
}
while(runs[level].length != 1)

sortedList=runs[runs.length-1];
console.log("final sortedList" + sortedList);
console.log(sortedList)
    