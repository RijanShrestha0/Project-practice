// let nam = "Rijan Shrestha"
// let age = "19"
// let education = "Neosphere"
// console.log(`My Name Is ${nam}. I am ${age} years. I'm Currently Studing At ${education}.`)
// typeof(nam)
// typeof(age)

const body = document.querySelector("body");
const container = document.createElement("div");
container.setAttribute("class", "container");
container.style.cssText=`
display:flex;
justify-content: center;
align-items: center;
margin-top: 40%;
flex-direction: column;
`
body.appendChild(container);
const el = document.createElement("div");
el.textContent=`Minor / Adult Condition`
el.style.cssText=`
font-size: 50px;
`
body.appendChild(el);
const Minor = document.createElement("h1");
const Adult = document.createElement("h1");
const Old = document.createElement("h1");
const age1 = prompt("age");
if (age1 <= 17 ){
    Minor.textContent=`You are minor`
    container.appendChild(Minor);
} else if(age1>=18, age1 <=70){
    Adult.textContent=`You are adult`
    container.appendChild(Adult);
} else if(age1 >=71){
    Old.textContent=`You are Old`
    container.appendChild(Old);
}

// If Else Conditions
height = 6
him = height * 0.3048
weight = 78
bmi=weight / (him*him)
if (bmi <=18.4999){
  console.log("under-weight")
} else if (bmi>=18.5, bmi <=25.0){
  console.log("normal")
} else if(bmi>=25.1){
  console.log("over-weight")
}
// 
let number = 0
if (number<0){
  console.log("It's Negative");
}else if (number>0){
  console.log("It's Positive");
}else if (number==0){
  console.log("It's Zero");
}
// 
let age = 20
if(age<=0){
  console.log("Your Input Is In-Appropriate");
}else if (age>105){
  console.log("Your Input Is In-Appropriate");
}
else if (age<18){
  console.log("You Are Not Eligible For Voting");
}else if(age<105, age>17){
  console.log("You Are Eligible For Voting");
}
// 
let char = "Neosphere"
let a = char.length
if (char.length<11){
  console.log(`A given string is not longer than 10 characters as It has ${a} characters...`);
}else{
  console.log(`A given string is longer than 10 characters as It has ${a} characters...`);
}
// 
let baar = 5;
switch (baar) {
    case 1:
        baar = "Sunday";
        break;
    case 2:
        baar = "Monday";
        break;
    case 3:
       baar = "Tuesday";
        break;
    case 4:
        baar = "Wednesday";
        break;
    case 5:
        baar = "Thursday";
        break;
    case 6:
        baar = "Friday";
        break;
    case 7:
        baar = "Saturday";
    }
//For Loop
// question 1
let i = 1
for (i; i<=5; i++){
  console.log(i);
}
//
// question 2
let num = 2
while (num<=10){
  console.log(num);
  num += 2
}
//
// question 3
let sum = 0
for (i = 1; i<=10; i++){
  sum += i
}
console.log(`The sum of the given number with Loop is ${sum}.`);

// question 4
let factorial = 1
let fnumber = 5
while (fnumber>1){
  factorial *= fnumber
  fnumber--
}
console.log(`The factorial of given Number is ${factorial}`)

// question 5
for (index = 1; index<=5; index++){
  console.log(index*index)
}


// question 6
for (index = 1; index<=5; index++){
  console.log(index*index*index)
}

// question 7
const name = ["Roman", "Charlie", "Tony", "Peter"]
for (i = 0; i<name.length; i++){
  console.log(name[i]);
}

// question 8
let sum1 =0
const innum = [1, 2, 3, 4, 5]
for (i = 0; i<innum.length; i++){
  sum1 = sum1 + innum[i]
  console.log(sum1)
}


// question 9
const shoe = ["jordan", "airmax", "bandana", "blazer", "AF1"]
for (let i = shoe.length-1; i>=0 ;i--){
  console.log(shoe[i])
}

// question 10
const index_num = [5, 12, 3, 45, 8]
let l_num = 0
let index2 = 1
while (index2 < index_num.length){
  if (index_num[index2] > l_num){
    l_num = index_num[index2]
  }
  index2++
}
console.log(`The largest Number in assigned Value is ${l_num}`)

// question 11
for (i=1; i<=1; i++){
  for (j=1; j<=10; j++){
    a = i*j
    console.log(`${i} x ${j} = ${a}`)
  }
}






// question 14
let index1 = 10
while(index1 >= 1){
  console.log(index1)
  index1--
}

// print 
// *
// **
// ***
// ****
// *****

  let row = ''
  let row1 = '*'
for (indexl=1; indexl<=5; indexl++){
  for (indexm=1; indexm<=indexl; indexm++){
    row += row1
  }
  console.log(row)
}


let n = 5;
let string = "";
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    string += "*";
  }
  string += "\n";
}
// console.log(string);
// print 
//     *
//    **
//   ***
//  ****
// *****

// print 
//      *
//     **
//    ****
//   ******
//  ********
// **********