import Foundation

func greet(){
    print("Hello World!")
}
greet()

func addNumbers(num1: Int, num2: Int) -> Int {
    let sum = num1 + num2
    return sum
}
var sumResult = addNumbers(num1:2, num2:3)
print(sumResult)


func findSquare (num: Int) -> Int {
  let result = num * num
  return result
}
var square = findSquare(num: 4)
print(square)

var sqRoot = sqrt(25)
print(sqRoot)

var power = pow(2, 3)
print(power)

for i in 1...3{
    let result = findSquare(num: i)
    print("Square of \(i) : \(result)")
}


