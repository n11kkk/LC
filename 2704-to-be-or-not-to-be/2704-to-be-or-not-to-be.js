/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const objj = {
        toBe:function(value){
            if(val === value){
                return true;
            }
            else{
                throw new Error("Not Equal");
            }
        },
        notToBe:function(value){
            if(val!==value){
                    return true;
            }
            else{
                throw new Error("Equal");
            }
        }
    }
    return objj
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */