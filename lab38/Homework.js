//lab1

function parseData(jsonInput) {
    try {
        let parsedObj = JSON.parse(jsonInput);
        console.log(parsedObj);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseData('{"name": "Alice"}');
parseData("invalid json");

//lab2
let numberList = [1, 2, 3, 4, 5, 6];
let totalEven = 0;

for (let i = 0; i < numberList.length; i++) {
    console.log(numberList[i]);
    if (numberList[i] % 2 === 0) {
        totalEven += numberList[i];
    }
}

console.log(totalEven);

//lab3
let peopleData = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 35 }
];

console.table(peopleData);


//lab4

function divideNumbers(num1, num2) {
    try {
        if (num2 === 0) {
            throw new Error("Division by zero");
        }
        return num1 / num2;
    } catch (error) {
        console.error("Cannot divide by zero");
    }
}

divideNumbers(10, 2);
divideNumbers(10, 0);


//lab5

try {
    console.log(undefinedVariable);
} catch (error) {
    console.error("Variable is not defined");
}
