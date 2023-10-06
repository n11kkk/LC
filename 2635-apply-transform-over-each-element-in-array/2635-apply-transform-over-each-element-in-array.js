/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    returnArr = new Array(arr.length);
    for(var i=0;i<arr.length;i++){
        returnArr[i] = fn(arr[i],i)
    }
    return returnArr
};