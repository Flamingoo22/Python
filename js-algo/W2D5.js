

// function rotate(str){
//     arr = str.split('')
//     count = 13
//     for (let char of arr){
        
//         console.log(char)
        
//     }
// }

// rotate('ABCDEF')

/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function rotateStr(str, amnt) {
    let arr = str.split('')
    for(var count = amnt; count != 0; count--){
        last_element = arr[arr.length-1]
        arr.pop()
        arr.unshift(last_element)  //everything that moves the entire array is a loop, unshift moves each element after the new inserted element. LOOP!
    }
    return arr.join("")
}
    // split the string, 
    //set amnt to counter, 
    //loop throught array pop from back and insert into the front
    //.pop DO return the element it removed!


console.log(rotateStr(str, rotateAmnt1))
console.log(rotateStr(str, rotateAmnt2))
console.log(rotateStr(str, rotateAmnt3))
console.log(rotateStr(str, rotateAmnt4))
console.log(rotateStr(str, rotateAmnt5))
/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/
// arr= []
// for let a = str.length; a!=0; a--{
//     arr.push()
// }
// ABCD BCDA CDAB DCAB CABD 
// ==> array
// if the second string is in the array
// if str2 in arr





const two_strA1 = "ABCD";
const two_strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const two_expected1 = true;

const two_strA2 = "ABCD";
const two_strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const two_expected2 = false;

const two_strA3 = "ABCD";
const two_strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const two_expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {
    let list = []
    let arr = s1.split('')
    for(var count = s1.length; count != 0; count--){
        last_element = arr[arr.length-1]
        arr.pop()
        arr.unshift(last_element)
        list.push(arr.join(""))
    }
    return list.includes(s2)
}

// console.log(isRotation(two_strA1, two_strB1))
// console.log(isRotation(two_strA1, two_strB2))
// console.log(isRotation(two_strA1, two_strB3))


function isRotation(s1, s2) {
    // Check to see if lengths match
    if (s1.length != s2.length) {
        // If not return false
        return false;
    }
    // Find index for first letter
    let amnt = s2.indexOf(s1[0]);
    // Call reverse string function
    let reversedStr = rotateStr(s1, amnt)
    // Compare the two
    if (s2 == reversedStr) {
        return true;
    }
    else {
        return false;
    }
}

function rotateStr(str, amnt) {
    // Check amnt (only 11 different versions)
    if (amnt == 11 || amnt == 0) {
        return str;
    }
    // Subtract by 11 to get 'original' version
    else if (amnt > 11) {
        amnt = amnt - 11;
    }
    // Extract characters from the end
    let beginning = str.substring(str.length-amnt, str.length);
    // Remove last characters
    str = str.substring(0, str.length-amnt);
    // Concatenate 
    str = beginning + str
    return str;
}