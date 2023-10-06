/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    returnArr = []
    for(let i=0;i<arr.length;i++){
        if(fn(arr[i],i)){
            returnArr.push(arr[i])
        } 
    }
    return returnArr
};