'use strict';

function hexToBinary(s) {
    const lookupTable = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    };

    var ret = "";
    for (var i = 0; i < s.length; i++) {
        if (lookupTable[s[i]]) { ret += lookupTable[s[i]]; }
        else { return null; }
    }
    return ret;
}

function toHexString(byteArray) {
    var ret = "";
    byteArray.forEach(function (byte) {
        ret += ('0' + (byte & 0xFF).toString(16)).slice(-2);
    });
    return ret.toUpperCase();

    /**
     * The Array.from() method creates a new, shallow-copied Array instance
     * from an array-like or iterable object.
     * 
     * The join() method creates and returns a new string
     * by concatenating all of the elements in an array (or an array-like object),
     * separated by commas or a specified separator string.
     */
    // return Array.from(byteArray, (byte) => {
    //     return ('0' + (byte & 0xFF).toString(16)).slice(-2);
    // }).join('');
}

module.exports = {
    hexToBinary,
    toHexString
};
