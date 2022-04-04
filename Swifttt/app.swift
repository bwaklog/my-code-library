var apples = 23
apples += 1

let hello: String = "Hello World!"

var maybe: String? = nil

if (maybe == nil) {
    print("Missing value...")   
}

func whatUp(name: String, emoji: String) -> String {
    return "Hello \(name). Swift is \(emoji)"
}

var a = whatUp(name:"Aditya", emoji: "🔥")
print(a)

class Humanoid {
    var dna = "🧬"
    func speak() {
        print("I am alive!!!")
    }
}

var human = Humanoid()
human.speak()