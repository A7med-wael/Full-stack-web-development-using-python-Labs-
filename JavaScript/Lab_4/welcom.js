alert("Welcome to my site");
var name = prompt("please enter your name: ");
document.write("welcome " + name);

function enter_nums() {
  var num1 = prompt("enter num1: ");
  var num2 = prompt("enter num2: ");
  num1 = Number(num1);
  num2 = Number(num2);
  console.log(sum(num1, num2));
}

function sum(num1, num2) {
  return num1 + num2;
}
function enter_tempANDfeel() {
  var temp = prompt("enter today temperature: ");
  var feel = prompt("enter actual feel: ");
  temp = Number(temp);
  temp = Number(feel);
  todayWeather(temp, feel);
}

function todayWeather(temp, feel) {
  if (temp >= 25 && temp <= 30 && feel >= 25 && feel <= 30)
    console.log("normal");
  else if (temp < 25 && feel < 25) console.log("Cold");
  else if (temp > 30 && feel > 30) console.log("Hot");
  else console.log("Ambiguous, can’t detect");
}

function enter_faculty() {
  var fac = prompt("enter your faculty: ");
  fac = String(fac);
  faculty(fac);
}

function faculty(fac) {
  switch (fac) {
    case "fci":
      console.log("You’re eligible to Programing tracks");
      break;
    case "Engineering":
      console.log("You’re eligible to Network and Embedded tracks");
      break;
    case "Commerce":
      console.log("You’re eligible to ERP and Social media tracks");
      break;
    default:
      console.log("You’re eligible to SW fundamentals track");
  }
}

function odd_num(num1, num2) {
  if (num1 % 2 == 1) console.log(num1);
  else if (num2 % 2 == 1) console.log(num2);
  else console.log("no odd");
}
odd_num(2, 4);
