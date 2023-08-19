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