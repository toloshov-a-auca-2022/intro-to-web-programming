//lab1
let fruits = [];
fruits.push("apple");
fruits.push("banana");
fruits.push("cherry");
fruits.pop();
console.log(fruits);

//lab2
let numbers = [10, 20, 30, 40, 50];

let someNumbers = numbers.slice(1, 3);
console.log("Sliced Array: " + someNumbers);
console.log("Original Array: " + numbers);

//lab3
let nums = [1, 2, 3, 4, 5];
let squaredArray = nums.map(x => x * 2);
console.log("Squared Array: " + squaredArray);
console.log("Original Array: " + nums);

//lab4
let ages = [12, 18, 25, 30, 15];
let adults = ages.filter(x => x >= 18);
console.log(adults);

//lab5
let user = {
    name: "Adilet",
    age: 17,
    city: "New York"
};
console.log(user.name);
user.age = 26;
console.log(user);

//lab6
let car = {
    brand: "Tesla",
    model: "Model S",
    year: 2023
};

let keys = Object.keys(car);
console.log("Keys: " + keys);

let values = Object.values(car);
console.log("Values: " + values);