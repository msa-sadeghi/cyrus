// let age = Number(prompt("enter your age: "))
// if(age < 18){
//     console.log("you are teenager")
// }else if(age >= 18 && age < 60){
//     console.log("old")
// }else{
//     console.log("blalala")
// }

// let day = prompt("enter a number between 1 - 7")
// switch(day){
//     case "1":
//         console.log("Mon")
//         break
//     case "2":
//         console.log("Tue")
//         break
//     case "3":
//         console.log("Wed")
//         break
//     case "4":
//         console.log("Thur")
//         break
//     case "5":
//         console.log("Fri")
//         break
//     case "6":
//         console.log("Sat")
//         break
//     case "7":
//         console.log("Sun")
//         break
//     default:
//         console.log("wrong number")
//         break
// }

// for(let i = 1; i <= 10; i++){
//     console.log(`2 * ${i} = ${ 2 * i}`)
// }

// let secretNumber = 7
// let guess

// while(guess != secretNumber){
//     guess = Number(prompt("enter a number:"))
//     if(guess === secretNumber){
//         alert("correct ans")
//     }
//     else{
//         alert("try again")
//     }
// }





// let input;

// do{
//     input = prompt("enter a number between 1 - 10")
// }while(input < 1 || input >  10)

// console.log(input)

function add(a,b){
    return a + b
}

const sub = function(a,b){
    return a - b
}

const mul = (a, b) =>  a * b

const div = (a, b) => {
    if(b === 0) return
    return a / b
}

div(1,2)
const greet = name => `hello ${name}`
let numbers = [1,2,3,4,5,6]
numbers.forEach(n => console.log(n * 2))
let newNumbers = numbers.map(x => x * 2)
console.log(newNumbers)
let evenNumber = numbers.filter(x => x % 2 === 0)
console.log(evenNumber)
let sum = numbers.reduce((s, x) => s + x, 0)
console.log(sum)