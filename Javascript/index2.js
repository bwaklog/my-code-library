let baseSalery = 30_000;
let overtime = 10;
let rate = 20;

function getWage(baseSalery, overtime, rate) {
    return baseSalery + (overtime * rate);
}

let employee = {
    baseSalery: 30_000,
    overtime: 10,
    rate: 20,
    getWage: function () {
        return this.baseSalery + (this.overtime * this.rate);
    }
};
console.log(employee.getWage());

let Person = {
    name: 'Aditya',
    status: 2,

    getStatus: function () {
        if (status = 0) {
            return 'Asleep'; 
        }
        else {
            return 'Awake'
        };
    }

}

let Car = {
    carModel: "AE86", 
    carPrice: 30000,
    carMileage: 1200,
}

//  this is a test message 

console.log(Car.carMileage)
console.log(Person.getStatus())

