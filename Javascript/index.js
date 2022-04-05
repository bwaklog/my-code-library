
let selectedColors = ['red', 'blue'];
selectedColors[2] = 1;
console.log(selectedColors);
console.log(selectedColors.length);


// function types
// Performing a task
function greet(name, lastName) {
    console.log('Well Hello ' + name + ' ' + lastName + ':D');
}
greet('Aditya', 'Hegde')
greet('Aditya') // default value for a variable is undefined

// Calculating a value
function square(number) {
    return number * number;
}
let number = square(2);
console.log(number);


