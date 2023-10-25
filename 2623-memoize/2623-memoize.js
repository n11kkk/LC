/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const sol = {};
    return function(...args) {
        // console.log("ARGS",args,sol);
        // console.log(sol?.args)
        if(sol?.[args] != undefined)
        {
            // console.log("FOUND",sol?.[args])
            // console.log(sol)
            return sol[[args]];
        }
        // console.log("FN",fn,"CALL",fn(...args));
        sol[[args]] = fn(...args);
        return sol[[args]];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */