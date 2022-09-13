// /* 
// Given an array of ints representing a line of people where the space between
// indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
// that space,
// return whether or not there is at least 6 feet separating every person.
// Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
// */

// const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
// const expected1 = false;

// const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected2 = true;

// const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected3 = true;

// const queue4 = [];
// const expected4 = true;

// /**
//  * Determines whether each occupied space in the line of people is separated by
//  * 6 empty spaces.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<0|1>} queue
//  * @returns {Boolean}
//  */
// function socialDistancingEnforcer(queue) {
//     //Your code here
//     let hash = {
//         'human':false,
//         'distance':0
//     }
//     for ( let index = 0; index<=queue.length; index++ ){
//         if(queue[index] == 1){
//             if(hash['human'] == true){
//                 if(hash['distance'] < 6){
//                     return false;
//                 }else{
//                     hash['distance'] = 0;
//                     hash['human'] = false;
//                 }
//             }
//             hash['human'] = true
//         }
//         if(hash['human'] == true){
//             hash['distance']++
//         }
//     }
//     return true
// }
// // for ... of ... will print out the element
// //for ... in ... will print out the index number
// //locating the '1'
// //keep track fo distance between '1'

// console.log(socialDistancingEnforcer(queue1)) // false
// console.log(socialDistancingEnforcer(queue2)) // true
// console.log(socialDistancingEnforcer(queue3)) // true
// console.log(socialDistancingEnforcer(queue4)) // true

/* 
Balance Index
Here, a balance point is ON an index, not between indices.
Return the balance index where sums are equal on either side
(exclude its own value).

Return -1 if none exist.

*/
            // 0   1  2  3  4
const numsA = [-2, 5, 7, 0, 3];
const expectedA = 2;

const numsB = [9, 9];
const expectedB = -1;

const numsC = [9,1,3,1,1,2,1,9];

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    //Your code here
    if (nums.length <= 2){
        return -1
    }
    left = nums.shift()
    right = nums.pop()
    count = 1
    for(let i =0; i<nums.length; i++){
        if(nums.length != 1 ){
            if(left>right){
                right+=nums.pop()
            }else if (right>left){
                left += nums.shift()
                count+=1
            }
        }else{
            return count
        }
    }
    return -1
}

console.log(balanceIndex(numsA)) // 2
console.log(balanceIndex(numsB)) // -1



function balanceIndex(nums) {
    if (nums.length < 3) { // less than 3 items, we can't balance
        return -1;
    }

    let left = nums[0]; // set left equal to first element
    
    let right = 0; // start right at 0
    for (let i = 2; i < nums.length; i++) { //loop starting at index 2 (skipping first balance point)
        right += nums[i]; // and add the remaining elements into right
    }
    // now left has the first element, our first balance point to check is at index one, and right has all the other elements
    // [ left, balance, right]
    //    0 ,    1     , all other indices
    for (let i = 1; i < nums.length - 1; i++) {
        if (left === right) {
            return i; // if left and right are equal, return i, location of balance index
        } 
        //otherwise, remove the next balance point from right
        right -= nums[i + 1];
        //add the current/previous balance point to left
        left += nums[i];
    }
    return -1; // if sides were never equal, return -1
}