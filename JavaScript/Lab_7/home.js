let textbox = document.getElementById("txt");

textbox.addEventListener("keydown", function (event) {
  alert("Key Code: " + event.keyCode);
});

textbox.addEventListener("mousedown", function (event) {
  let button;
  switch (event.button) {
    case 0:
      button = "Left Button (0)";
      break;
    case 1:
      button = "Middle Button (1)";
      break;
    case 2:
      button = "Right Button (2)";
      break;
    default:
      button = "Unknown Button (" + event.button + ")";
  }
  alert("Mouse Button: " + button);
});




let clockInterval;
let clockDisplay = document.getElementById("clockDisplay");
let startBtn = document.getElementById("startClockBtn");

startBtn.addEventListener("click", function () {
  alert("Clock Started");
  clockInterval = setInterval(() => {
    const now = new Date();
    clockDisplay.textContent = now.toLocaleTimeString();
  }, 1000);
});

document.addEventListener("keydown", function (event) {
  if (event.altKey && (event.key === "w" || event.key === "W")) {
    clearInterval(clockInterval);
    alert("Clock Stopped");
    clockDisplay.textContent = "";
  }
});



let score = 0;
let images = document.querySelectorAll("img");

function increaseScore() {
  score++;
}
function alertScore() {
  alert("Your score is: " + score);
}

images.forEach((img) => {
  img.addEventListener("click", increaseScore);
  img.addEventListener("click", alertScore);
});

setTimeout(() => {
  images.forEach((img) => {
    img.removeEventListener("click", alertScore);
    img.addEventListener("click", function () {
      alert("Game Over");
    });
  });
}, 10000);





let adWindow;
document.getElementById("openLink").addEventListener("click", function (e) {
  e.preventDefault();

  setTimeout(() => {
    adWindow = window.open("", "AdWindow", "width=500,height=400");

    if (adWindow) {
      adWindow.document.write(`
            <html>
            <head><title>Special Offer</title></head>
            <body>
              <h1 style="color: green;"> Limited-Time Offer! </h1>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium...</p>
              <p>Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.</p>
              <p>Don't miss this opportunity.
            </body>
            </html>
          `);
    }
  }, 3000);
});

document.getElementById("closeLink").addEventListener("click", function (e) {
  e.preventDefault();
  adWindow.close();
});




const firstNameInput = document.getElementById("firstName");
firstNameInput.addEventListener("keydown", function (event) {
  const key = event.key;
  const isLetter = /^[a-zA-Z]$/.test(key);
  const allowedKeys = ["Backspace", "ArrowLeft", "ArrowRight", "Tab", "Delete"];

  if (!isLetter && !allowedKeys.includes(key)) {
    event.preventDefault();
  }
});
