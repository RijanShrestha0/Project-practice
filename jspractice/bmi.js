var height = prompt("Enter Your Height");
var h_m = height * 0.3048
var weight = prompt("Enter Your Weight");
bmi = weight/(h_m*h_m);
if (bmi <=18.4999){
  console.log("under-weight");
} else if (bmi>=18.5, bmi <=25.0){
  console.log("normal");
} else if(bmi>=25.1){
  console.log("over-weight");
}