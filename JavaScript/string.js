let str="hello";
console.log(str);
console.log("string is immutable");
let str1=str.replace("h","H");
console.log(str1);
console.log(str);
let stre="aky";
stre[1]="t";
console.log(stre);

//method of string
console.log("length of string");
let s="hello";
console.log(s.length);

console.log("access charcter");
console.log(s[1]);

console.log("convert case");
console.log(s.toUpperCase());
console.log(s.toLowerCase());

console.log("trim used to remove spaces from start and end of string");
let s1="   hello world   ";
console.log(s1.trim());

console.log("slice method used to extract part of string");
console.log(s1.slice(3,7));

console.log("replace method used to replace part of string");
let s2="hii awadhesh";
console.log(s2.replace("awadhesh","radha"));

console.log("split method used to split string into array");
let s3="hii awadhesh";
console.log(s3.split(" "));

console.log("includes method used to check if string contains a substring");
console.log(s3.includes("awadhesh"));

console.log("indexOf method used to find the index of a substring");
console.log(s3.indexOf("awadhesh"));

console.log("lastIndexOf method used to find the last index of a substring");
console.log(s3.lastIndexOf("awadhesh"));    

console.log("charAt method used to get the character at a specific index");
console.log(s3.charAt(4));

console.log("template literals used to create strings with embedded expressions");
let a=10;
let name="awadhesh";
console.log(`my age is ${a} and and my name is ${name}`);

console.log("concatenation used to join strings");
let s4="hello";
let s5="world";
console.log(s4.concat(" ",s5));
console.log(s4+" "+s5);

