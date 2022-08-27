// Your task is to write a function which returns the sum of following series upto nth term(parameter).

// Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...


// function series(n){
//     let result = 0;
//     for(let i =0; i<n; i++){
//         result+= 1/(3*i+1)
//     }
//     return (Math.round(result*100)/100).toFixed(2);  //to formats a number with fixed numbers of decimals
// }

// console.log(series(1))



// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
// function checkAmount(n){
//     b = n.toLowerCase()
//     let x = 0;
//     let o = 0;
    
//     for(let i=0; i<b.length;i++){
//         if(b[i]=="x"){
//             x+=1;
//             // console.log(b[i])
//         }else if(b[i]=="o"){
//             o+=1;
//             // console.log(b[i])
//         }
//         else{
//             continue;
//         }
//     }
//     // console.log(x)
//     // console.log(o)
//     if(x==o){
//         return true;
//     }else{
//         return false;
//     }
// }


// console.log(checkAmount("Xxoo"))

// // A much shorter solution
// function XO(str) {
//     return str.toLowerCase().split('x').length === str.toLowerCase().split('o').length;
// }



// Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.


function twoIntegerSum(a,b){
    let sum = 0;
    if(a==b){
        return a
    }else if( a > b){
        for( b ; b <= a; b++){
            sum +=b;
        }
    }else{
        for(a; a <=b; a++){
            sum +=a;
        }
    }
    return sum;
}

console.log(twoIntegerSum(-1,5))

//Math : sum of numbers between two points = (number of integers)(point1 + point2)/2
//Easier way using smarter Math:

function twoIntegerSum(a,b){
    let max = Math.max(a,b);
    let min = Math.min(a,b);
    return (max-min+1)*(max+min)/2;
}

// code testing
// function a(n,a){
//     return [...Array(n).keys()].map(x=> x+a)
//     // .map(i => i+a)
// } 
// console.log(a(1,2))
// console.log([...Array(5).keys()])

// function range(size:number, startAt:number = 0):ReadonlyArray<number> {
//     return [...Array(size).keys()].map(i => i + startAt);
// }


// a = [1,2,32,4,5,67,1]

// console.log(Object.keys(a))  //Object.keys(arr)  return the string iteration of indexes inside the array
// console.log([...a.keys()])  //...arr.keys()   return the number iteration of indexes inside the array
