const cells = document.querySelectorAll(".cell");
const blueScore = document.getElementById("blue-score");
const redScore = document.getElementById("red-score");

let currentPlayer = "X";
let gameEnded = false;
let blueWins = 0;
let redWins = 0;

// Define the moveLibrary
const moveLibrary = {
    "cell-1": ["cell-8","cell-3","cell-2","cell-4","cell-1","cell-6","cell-5","cell-9","cell-7","cell-4","cell-7","cell-9","cell-2","cell-3","cell-8","cell-1","cell-6","cell-5"],

    "cell-2": ["cell-1","cell-2","cell-5","cell-6","cell-7","cell-9","cell-8","cell-4","cell-3","cell-4","cell-7","cell-9","cell-2","cell-3","cell-8","cell-1","cell-6","cell-5"],

    "cell-3": ["cell-4","cell-7","cell-9","cell-2","cell-3","cell-8","cell-1","cell-6","cell-5","cell-5","cell-6","cell-8","cell-7","cell-9","cell-3","cell-2","cell-1","cell-4"],

    "cell-4": ["cell-9","cell-5","cell-4","cell-8","cell-2","cell-1","cell-3","cell-7","cell-6","cell-5","cell-6","cell-8","cell-7","cell-9","cell-3","cell-2","cell-1","cell-4"],

    "cell-5": ["cell-6","cell-1","cell-7","cell-3","cell-5","cell-4","cell-9","cell-8","cell-2","cell-4","cell-7","cell-9","cell-2","cell-3","cell-8","cell-1","cell-6","cell-5"],

    "cell-6": ["cell-2","cell-8","cell-3","cell-9","cell-6","cell-7","cell-4","cell-5","cell-1","cell-5","cell-6","cell-8","cell-7","cell-9","cell-3","cell-2","cell-1","cell-4"],

    "cell-7": ["cell-5","cell-6","cell-8","cell-7","cell-9","cell-3","cell-2","cell-1","cell-4","cell-5","cell-6","cell-8","cell-7","cell-9","cell-3","cell-2","cell-1","cell-4"],

    "cell-8": ["cell-7","cell-9","cell-1","cell-5","cell-4","cell-2","cell-6","cell-3","cell-8","cell-5","cell-6","cell-8","cell-7","cell-9","cell-3","cell-2","cell-1","cell-4"],

    "cell-9": ["cell-3","cell-4","cell-6","cell-1","cell-8","cell-5","cell-7","cell-2","cell-9","cell-1","cell-2","cell-5","cell-6","cell-7","cell-9","cell-8","cell-4","cell-3"]
};

cells.forEach((cell) => {
    cell.addEventListener("click", () => {
        if (cell.textContent === "" && !gameEnded) {
            cell.textContent = currentPlayer;
            cell.classList.add(`selected-${currentPlayer.toLowerCase()}`);
            if (checkWin(currentPlayer)) {
                if (currentPlayer === "X") {
                    blueWins++;
                    blueScore.textContent = ` ${blueWins}`;
                } else {
                    redWins++;
                    redScore.textContent = ` ${redWins}`;
                }
                alert(`${currentPlayer} wins!`);
                gameEnded = true;
                setTimeout(resetBoard, 1000);
            } else if (checkDraw()) {
                alert("It's a draw!");
                gameEnded = true;
                setTimeout(resetBoard, 1000);
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
                if (currentPlayer === "O" && !gameEnded) {
                    setTimeout(makeAIMove, 500);
                }
            }
        }
    });
});

function checkWin(player) {
    const winCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];

    return winCombos.some(combo => {
        return combo.every(index => cells[index].textContent === player);
    });
}

function checkDraw() {
    return Array.from(cells).every(cell => cell.textContent !== "");
}

function resetBoard() {
    cells.forEach(cell => {
        cell.textContent = "";
        cell.classList.remove("selected-x", "selected-o");
    });
    currentPlayer = "X";
    gameEnded = false;
    if (currentPlayer === "O" && !gameEnded) {
        setTimeout(makeAIMove, 500);
    }
}

const aiPlayer = "O";

function makeAIMove() {
    const playerMoveId = Array.from(cells).find(cell => cell.classList.contains("selected-x")).id;
    const aiMoveIds = moveLibrary[playerMoveId];
    if (aiMoveIds) {
        for (const aiMoveId of aiMoveIds) {
            const aiMoveIndex = parseInt(aiMoveId.split("-")[1]) - 1;
            if (cells[aiMoveIndex].textContent === "") {
                cells[aiMoveIndex].textContent = aiPlayer;
                cells[aiMoveIndex].classList.add("selected-o");
                currentPlayer = "X";
                if (checkWin(aiPlayer)) {
                    redWins++;
                    redScore.textContent = `Red Score: ${redWins}`;
                    alert("O wins!");
                    gameEnded = true;
                    setTimeout(resetBoard, 1000);
                } else if (checkDraw()) {
                    alert("It's a draw!");
                    gameEnded = true;
                    setTimeout(resetBoard, 1000);
                }
                return;
            }
        }
        // Fallback strategy: Select a random empty cell
        makeRandomMove();
    } else {
        // Fallback strategy: Select a random empty cell
        makeRandomMove();
    }
}

// Reset the scoreboard
document.getElementById("reset-button").addEventListener("click", () => {
    blueWins = 0;
    redWins = 0;
    blueScore.textContent = " 0";
    redScore.textContent = " 0";
    resetBoard();
});
