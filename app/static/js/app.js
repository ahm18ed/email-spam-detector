const emailInput = document.getElementById("email-input");
const characterCount = document.getElementById("character-count");
const analyzeButton = document.getElementById("analyze-button");

const resultSection = document.getElementById("result");
const resultTitle = document.getElementById("result-title");
const resultDescription = document.getElementById("result-description");
const spamProbability = document.getElementById("spam-probability");
const probabilityFill = document.getElementById("probability-fill");
const resetButton = document.getElementById("reset-button");

if (
    !emailInput ||
    !characterCount ||
    !analyzeButton ||
    !resultSection ||
    !resultTitle ||
    !resultDescription ||
    !spamProbability ||
    !probabilityFill ||
    !resetButton
) {
    throw new Error("MailGuard UI elements are missing from index.html");
}

emailInput.addEventListener("input", () => {
    const length = emailInput.value.length;

    characterCount.textContent =
        `${length.toLocaleString()} / 10,000`;
});


analyzeButton.addEventListener("click", analyzeEmail);


emailInput.addEventListener("keydown", (event) => {
    if (
        (event.ctrlKey || event.metaKey) &&
        event.key === "Enter"
    ) {
        analyzeEmail();
    }
});


resetButton.addEventListener("click", () => {
    emailInput.value = "";

    characterCount.textContent = "0 / 10,000";

    resultSection.hidden = true;

    emailInput.focus();
});


async function analyzeEmail() {
    const email = emailInput.value.trim();

    if (!email) {
        emailInput.focus();
        return;
    }

    analyzeButton.disabled = true;
    analyzeButton.classList.add("loading");

    const buttonText = analyzeButton.querySelector("span");

    buttonText.textContent = "Analyzing...";


    try {

        const response = await fetch("/predict", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email: email
            })
        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(
                data.error || "Unable to analyze email."
            );
        }


        showResult(data);

    } catch (error) {

        console.error(error);

        alert(error.message);

    } finally {

        analyzeButton.disabled = false;

        analyzeButton.classList.remove("loading");

        buttonText.textContent = "Analyze email";
    }
}


function showResult(data) {

    const isSpam = data.prediction === 1;

    const percentage =
        data.spam_probability * 100;


    resultTitle.textContent = isSpam
        ? "Likely spam"
        : "Looks legitimate";


    resultDescription.textContent = isSpam
        ? "This email contains patterns commonly associated with spam."
        : "This email doesn't strongly resemble spam based on the model's learned patterns.";


    spamProbability.textContent =
        `${percentage.toFixed(1)}%`;


    probabilityFill.style.width =
        `${percentage}%`;


    resultSection.hidden = false;
}