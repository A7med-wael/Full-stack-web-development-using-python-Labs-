let arr = new Array();
arr = [
  "tip1",
  "tip2",
  "tip3",
  "tip4",
  "tip5",
  "tip6",
  "tip7",
  "tip8",
  "tip9",
  "tip10",
];
let indx = Math.floor(Math.random() * arr.length);
console.log(arr[indx]);

// console.log(Math.random()*10)

function Cdate() {
  date = new Date();
  document.write("date: " + date.toLocaleString());
}

function checkMail(mail) {
  let len = mail.length;
  f = false;
  if (mail[0] != "@" || mail[len - 1] != "@") {
    for (let i = 1; i < len - 1; ++i) {
      if (mail[i] == "@") f = true;
    }
  }
  if (f == true) console.log("mail");
  else console.log("Not mail");
}

function enterMail() {
  let mail = prompt("Enter your mail");
  mail = String(mail);
  checkMail(mail);
}

let students = new Array();
students = [60, 100, 10, 15, 85];
students.sort((a, b) => a - b);

console.log(students);

let degree = students.find((d) => d >= 100);
console.log(degree);

let grade = students.filter((g) => g < 60);

let students2 = new Array();
students2 = [
  { name: "Ahmed", grade: 100 },
  { name: "mohamed", grade: 60 },
  { name: "ali", grade: 10 },
  { name: "khaled", grade: 85 },
  { name: "wael", grade: 15 },
];

let sname = students2.find((s) => s.grade >= 90 && s.grade <= 100);
console.log(sname.name);

let snames = students2.filter((s) => s.grade < 60);

for (let student of snames) {
  console.log(student.name);
}

students2.push({ name: "more", grade: 70 });

for (let student of students2) {
  console.log(student.name);
}

students2.pop();

for (let student of students2) {
  console.log(student.name);
}

students2.sort((a, b) => a.name.localeCompare(b.name));

for (let student of students2) {
  console.log(student.name);
}

students2.splice(
  2,
  0,
  { name: "Youssef", grade: 75 },
  { name: "tamer", grade: 92 }
);

for (let student of students2) {
  console.log(student.name);
}

students2.splice(4, 1);

for (let student of students2) {
  console.log(student.name);
}

// regExp
const fname = /^[A-Za-z]{3,}(?: [A-Za-z]{3,})*$/;
const emailReg = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|org|edu)\.eg$/;

function enterdata() {
  let fullName, email;

  while (true) {
    fullName = prompt("Enter your full name (e.g., Ahmed Wael)");
    if (fname.test(fullName)) {
      break;
    } else {
      alert(
        "Invalid full name!\n- Use alphabetic characters only\n- Each word must be at least 3 letters\n- No numbers or special characters\n- No leading/trailing spaces"
      );
    }
  }

  while (true) {
    email = prompt("Enter your email address (must end with .eg):");
    if (emailReg.test(email)) {
      break;
    } else {
      alert(
        "Invalid email!\n- Must be in format like: name@domain.com.eg\n- Only these endings allowed: .com.eg, .net.eg, .org.eg, .edu.eg"
      );
    }
  }
  alert("Your input is valid!\n\nFull Name: " + fullName + "\nEmail: " + email);
}
