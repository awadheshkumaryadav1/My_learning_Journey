//primitives data types in js
//number include integer and decimal
let a=10;
let b=20.4;
console.log(a);

//string
let name="akshay";
console.log(name);

//boolean
let istrue=true;
let isfalse=false;
let isloggedin=true;
console.log(istrue);
console.log(isfalse);
console.log(isloggedin);

//undefined
let x;
console.log(x);

//null
let y=null;
console.log(y);

//symbol
let sym=Symbol("akshay");

let dd = 10;
let e = dd;
e= 20;
console.log(dd); // 10
console.log(e); // 20
//non-primitives data types in js

//object
let obj={
    name:"akshay",
    age:25,
    city:"pune"
}
console.log(obj);

// Array
let arr=[10,20,30,40,50];
console.log(arr);

// check datatype of variable
let c=10;
console.log(typeof c);
console.log(typeof name);
console.log(typeof istrue);
console.log(typeof 10);
console.log(typeof "name");

//js is dynamically typed language, we can change the datatype of variable at runtime
let d=10;
console.log(typeof d);
d="akshay";
console.log(typeof d);

//function
function add(a,b){
    return a+b;
}
let sum=add(10,20);
console.log(typeof add);
console.log(sum);
console.log(add(10,20));

let obj1={
    name:"akshay",
}
let obj2=obj1;
obj2.name="akkk";
console.log(obj1.name); // akkk
console.log(obj2.name); // akkk


