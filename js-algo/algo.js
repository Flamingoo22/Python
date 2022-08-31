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


// function twoIntegerSum(a,b){
//     let sum = 0;
//     if(a==b){
//         return a
//     }else if( a > b){
//         for( b ; b <= a; b++){
//             sum +=b;
//         }
//     }else{
//         for(a; a <=b; a++){
//             sum +=a;
//         }
//     }
//     return sum;
// }

// console.log(twoIntegerSum(-1,5))

// //Math : sum of numbers between two points = (number of integers)(point1 + point2)/2
// //Easier way using smarter Math:

// function twoIntegerSum(a,b){
//     let max = Math.max(a,b);
//     let min = Math.min(a,b);
//     return (max-min+1)*(max+min)/2;
// }

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

// You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
// function getMiddle(s)
// {
//   //Code goes here!
//     let a = s.length/2
//     if (Number.isInteger(a)){
//         return s[a-1]+s[a]
//     }else{
//     let b = Math.floor(a)
//         return s[b]
//     }
// }


// console.log(getMiddle("fkdsajhsfdk"))

// // shorter answers
// function getMiddle(s)
// {
//     return s.substr(Math.ceil(s.length / 2 - 1), s.length % 2 === 0 ? 2 : 1);     // string.substring(a,b) returns a portion of string, takes up to 2 parameters, a=starting index, b=ending index. When only 1 paramter, slice all string starting at that index(inclusive)
// }

// function getMiddle(s)
// {
//     return s.slice((s.length-1)/2, s.length/2+1);  //string.slice is similar to string.substring
// }

// // Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".
// function evenChars(string) {
// //keep coding!
//     if(string.length < 2 || string.length > 100){
//         return "invalid string";
//     }else{
//         let result = [];
//         let x = 1;
//         while(x < string.length){
//             result.push(string[x]);
//             x+=2;
//     }
//     return result;
//     }
// }

// console.log(evenChars("dsajdsald"))

// //short answers:
// function evenChars(string) {
//     return (string.length < 2 || string.length > 100) ? "invalid string" : 
//     [...string].filter((x, i) => i % 2);
// }

// Convert number to binary
// function binary(x,y){
//     let sum = x+y
//     let binarr=[]
//     for(sum;sum!=0 ;sum = Math.floor(sum/2)){
//         if(sum%2 == 0){
//             binarr.push(0);
//             console.log(binarr);
//             console.log(sum);
//         }else{
//             binarr.push(1);
//             console.log(binarr);
//             console.log(sum)
//         }
//     }
//     z = binarr.reverse().join("")
//     console.log(z)
// }


// binary(1,2)

// //shorter answer
// function addBinary(a,b){
//     return (a+b).toString(2)
// }

// console.log(addBinary(3,4))


// function removeDups(a,b){

//     let x = a +b;
//     let z = Array.from(new Set(x.split(','))).toString();
//     // document.write(x);
//     console.log(z)
// }

// removeDups("dada","dfdfaaa")

// function toString(x){
//     y=""
//     z = x.split("")
//     console.log(z)

// }

// toString(213223)




// function reverse(x){
//     return x.split("").reverse().join("")
// }

// console.log(reverse("ABCDEFG"))

// x = "ABCDEFG"

// y = sorted(x , reverse=true)

// console.log(x.sort().reverse())

// let x = "HALO"

//       // 0123
// let y = ""

// for(let j = x.length-1; j>=0; j--){
//     y += x[j];
//     // console.log(x[j])
// }

// console.log(y)


// // newStrin = "dlkasdlsal"

// // console.log(newStrin.length)


// ``` language

// ```





// }

// arr = "aabcdedf"
// sep = ","

// console.log(join(arr,sep))

/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
// //  * @param {Array<string|number|boolean>} arr The items to be joined as a string.
// //  * @param {string} separator To separate each item of the given arr.
// //  * @returns {string} The given array items as a string separated by the given separator.
//  */
function join(arr,sep){
    let newStr = ""
    for(let i =0; i < arr.length; i++){
        if(i == arr.length-1){
            newStr += arr[i]
        }else{
            newStr += arr[i];
            newStr += sep;
        }
    }
    return newStr
}
//     //Your code here
// console.log(join(arr3,separator1))
// console.log(join(arr3,separator2))
// console.log(join(arr5,separator5))


// console.log(join(arr1, separator1)) // Expected: "1, 2, 3"
// console.log(join(arr2, separator2)) // Expected: "1-2-3"
// console.log(join(arr3, separator3)) // Expected: "1 - 2 - 3"
// console.log(join(arr4, separator4)) // Expected: "1"

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const str3 = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expectedD = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
//  * @param {string} wordsStr A string to be turned into an acronym.
//  * @returns {string} The acronym.
 */
// function acronymize(str) {
//     //Your code here
//     let newStr = ""
//     if(str[0] != " "){
//         newStr += str[0]
//     }
//     for(let j =0; j <str.length; j++){
//         if(str[j-1]==" " && str[j] != " "){
//             // console.log(str[j+1])
//             newStr += str[j]
//             // console.log(newStr)
//             // console.log(str[j-1])
//         // }
//         }
//     // 
//     }
//     return newStr.toUpperCase()
// }
// function acronymize(str) {
//     //Your code here
//     let acronym = "";
//     let currentWord = "";
//     for (let i = 0; i < str.length; i++) {
//         if (str[i] !== " ") {
//             currentWord += str[i];
//         } else if (currentWord.length > 0) {
//             acronym += currentWord[0];
//             currentWord = "";
//         }
//     }
//     if (currentWord.length > 0) {
//         acronym += currentWord[0];
//     }
//     return acronym.toUpperCase();
// }
function acronymize(str) {
    //Your code here
    let acronym = "";
    let words = str.split(" ");
    console.log(words)
    for (let i = 0; i < words.length; i++) {
        if (words[i] !== "") {
            acronym += words[i][0].toUpperCase();
        }
    }
    return acronym;
}

console.log(acronymize(str1)); // Expected: "OOP"
// console.log(acronymize(str2)); // Expected: "APIE"
// console.log(acronymize(str3)); // Expected: "SDLC"
// console.log(acronymize(str4)); // Expected: "GIT"