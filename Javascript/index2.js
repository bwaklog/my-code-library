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
console.log(Person.getStatus())