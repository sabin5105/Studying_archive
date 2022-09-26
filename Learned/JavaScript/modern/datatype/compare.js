let str = '';

for(let i=65; i<=220; i++){
    str += String.fromCodePoint(i);
}
console.log(str);
console.log('Österreich'.localeCompare('Zealand')); // -1, Ö < Z, depending on the browser

// Upper case comes first than lower case