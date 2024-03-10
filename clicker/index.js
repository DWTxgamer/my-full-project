const timerDisplay = document.getElementById("timer");
const clickCountDisplay = document.getElementById("clicks");
const clickBox = document.querySelector(".click-box");

let timeLeft = 60; // Timer in seconds
let clickCount = 0;
let timerRunning = false;

clickBox.addEventListener("click", () => {
    if (!timerRunning) {
        startTimer();
        timerRunning = true;
    }
    if (timeLeft > 0) {
        clickCount++;
        clickCountDisplay.textContent = clickCount;
    }
});

function updateTimerDisplay() {
    const minutes = Math.floor(timeLeft / 60).toString().padStart(2, "0");
    const seconds = (timeLeft % 60).toString().padStart(2, "0");
    timerDisplay.textContent = `${minutes}:${seconds}`;
}

function startTimer() {
    const countdownInterval = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateTimerDisplay();
        } else {
            clearInterval(countdownInterval);
            clickBox.removeEventListener("click", () => {});
            clickBox.style.cursor = "not-allowed";
            alert(`Time's up! You clicked ${clickCount} times.`);
        }
    }, 1000);
}

updateTimerDisplay();
