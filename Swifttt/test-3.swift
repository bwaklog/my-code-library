let fruits = ["Apple", "Peach", "Mango"]

for fruit in fruits {
    print("\(fruit)")
}
print(fruits.count)
print(fruits.isEmpty)

var employeeId: Set = [22, 23, 24, 25]
print(employeeId)
employeeId.insert(32)
print(employeeId)

var setA: Set = [1, 3, 5]
var setB: Set = [1, 2, 3]
print(setA.intersection(setB))
print(setA.subtracting(setB))
print(setA.symmetricDifference(setB))
setA = [1, 2, 3, 4 , 5]
setB = [1, 2]
print(setB.isSubset(of: setA))

var empSet = Set<Int>()
print(empSet)

var numbers = [1:1, 2:2, 3:3]
print(numbers)
numbers[4] = 4
print(numbers[3]!)

for (key, value) in numbers {
    print(key, value)
    
}


