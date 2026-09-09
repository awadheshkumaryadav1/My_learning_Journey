let person = {
  name: "Awadhesh",
  age: 22,
  isStudent: true
};
console.log(person);
console.log(person.name); // Accessing property using dot notation
console.log(person.age); // Accessing property using dot notation
console.log(person["age"]); // Accessing property using bracket notation

let key = "name";
console.log(person[key]); // Awadhesh
console.log(person.key); // undefined

person.cityy = "Chennai"; // Adding new property to object
console.log(person.cityy); // Chennai
person.age = 25; // Updating property value
console.log(person.age); // 25
delete person.age; // Deleting property from object
console.log(person.age); // undefined


//object with methods

let person1 = {
  name: "Awadhesh",
  greet: function() {
    console.log("Hello!");
  }
};

person1.greet();

//object with methods using ES6 syntax
//this keyword in object method refers to the current object
let student={
    name:"aky",
    // greet:function(){ //old way of defining method
    //     console.log("Hello "+this.name);
    // }
        greet(){ //new way of defining method ES6
        console.log("Hello "+this.name);
    }

};
student.greet(); // Hello aky

//object with nested object
let college={
    name:"awadhesh",
    Btech:{
        name:"btech",
        age:22
    }
};
console.log(college.Btech.name); // btech


//array of objects
let objects={
  name:"awadhesh",
    arr:[80,90,100],
    students:[
        {name:"awadhesh",age:22}]
};
console.log(objects.students[0].name); // awadhesh
console.log(objects.students[0].age); // 22
console.log(objects.students.name); // undefined
// console.log(objects.keys(objects)); // [ 'name', 'arr', 'students' ]
// console.log(objects.values(objects)); // [ 'awadhesh', [ 80, 90, 100 ], [ { name: 'awadhesh', age: 22 } ] ]
// console.log(objects.entries(objects)); // [ [ 'name', 'awadhesh' ], [ 'arr', [ 80, 90, 100 ] ], [ 'students', [ { name: 'awadhesh', age: 22 } ] ] ]


//loop through object properties
for(let key in objects){
    console.log(key,objects[key]);
}


//refernce concept in object
let obj22={
    name:"awadheshkumar",

}
let obj23=obj22;
obj23.name="aky";
console.log(obj22.name); 


//object creation
let obj={};
//using new object()
let obj1=new Object();


let person2 = {
  name: "A",
  greet() {
    console.log(this.name);
  }
};

let person3 = {
  name: "B",
  greet: person2.greet
};

person2.greet();
person3.greet(); // B