// create_event.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("create-event-form");

    // Validate form data before submission
    form.addEventListener("submit", (event) => {
        const title = document.getElementById("title").value.trim();
        const description = document.getElementById("description").value.trim();
        const date = document.getElementById("date").value.trim();
        const time = document.getElementById("time").value.trim();
        const location = document.getElementById("location").value.trim();

        if (!title || !date || !time || !location) {
            alert("Please fill out all required fields.");
            event.preventDefault();
            return;
        }

        const eventDate = new Date(`${date}T${time}`);
        if (eventDate < new Date()) {
            alert("The event date and time must be in the future.");
            event.preventDefault();
        }
    });
});
