/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

// const str1 = "Y(3(p)p(3)r)s"; // ( () () )
// const expected1 = true;

// const str2 = "N(0(p)3"; // ( ( ) 
// const expected2 = false;
// // Explanation: not every parenthesis is closed.

// const str3 = "N(0)t ) 0(k"; // ( ) ) (
// const expected3 = false;
// // Explanation: because the second ")" is premature: there is nothing open for it to close.


// /**
//  * Determines whether the parenthesis in the given string are valid.
//  * Each opening parenthesis must have exactly one closing parenthesis.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {boolean} Whether the parenthesis are valid.
//  */
function parensValid(str) {
    //Your code here
    check = {
        '(_count':0
    }
    for(let i =0; i<str.length;i++){
        // console.log(check['(_count'])
        if(str[i]=='('){
            check['(_count'] += 1
        }else if(str[i]==')'){
            check['(_count'] -= 1
        } 
        if(check['(_count'] < 0 ){
            return false
        }
    }
    if (check['(_count'] != 0){
        return false
    }
    return true
}

// console.log(parensValid(str1)) // expected: true
// console.log(parensValid(str2)) // expected: false
// console.log(parensValid(str3)) // expected: false


// /* 
// Braces Valid
// Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
// */

const strA = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expectedA = true;

const strB = "D(i{a}l[ t]o)n{e";
const expectedB = false;

const strC = "A(1)s[O (n]0{t) 0}k";
const expectedC = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    //Your code here
    arr = []
    for(let i = 0; i<str.length; i++){
        last = arr.length - 1
        if(str[i]=="(" || str[i]=='[' || str[i]=="{"){
            arr.push(str[i])
        }
        else if(str[i]==")"){
            if (arr[last] = "("){
                continue
            }else{
                return false
            }
        }
        else if(str[i]=="]"){
            if (arr[last] = "["){

                continue
            }else{
                return false
            }
        }
        else if(str[i]=="}"){
            if (arr[last] = "{"){
                continue
            }else{
                return false
            }
        }
    }
    return true
}
console.log(bracesValid(strA)) // expected: true
console.log(bracesValid(strB)) // expected: false
console.log(bracesValid(strC)) // expected: false



function bracesValid(str) {
    const stack = [];
    const opens = "[({"
    const closesToOpens = { ")": "(", "}": "{", "]": "[" };
    
    for (let i = 0; i < str.length; i++) {
        char = str[i]
        if (opens.includes(char)) {
        stack.push(char);
        } else if (closesToOpens[char]) {
        if (closesToOpens[char] === stack[stack.length - 1]) {
            stack.pop();
        } else {
            return false;
        }
        }
    }
    return stack.length === 0;
    }












function bracesValid(str) {
    const stack = [];
    const isOpen = { "(": true, "{": true, "[": true }
    const closesToOpens = { ")": "(", "}": "{", "]": "[" };
    
    for (let char of str) {
        if (isOpen[char]) {
        stack.push(char);
        } else if (closesToOpens[char]) {
        if (closesToOpens[char] === stack[stack.length - 1]) {
            stack.pop();
        } else {
            return false;
        }
        }
    }
    return stack.length === 0;
    }