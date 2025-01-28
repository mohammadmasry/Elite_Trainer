// create_player.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("create-player-form");

    // Validate form data before submitting
    form.addEventListener("submit", (event) => {
        const name = document.getElementById("name").value.trim();
        const age = document.getElementById("age").value.trim();
        const position = document.getElementById("position").value;
        const statistics = document.getElementById("statistics").value.trim();

        if (!name || !age || !position) {
            alert("Please fill out all required fields.");
            event.preventDefault();
            return;
        }

        try {
            JSON.parse(statistics || "{}"); // Validate JSON format
        } catch (e) {
            alert("Statistics must be in valid JSON format.");
            event.preventDefault();
        }
    });
});
