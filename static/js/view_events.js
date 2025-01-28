// view_events.js

document.addEventListener("DOMContentLoaded", () => {
    // Add hover effects to event items
    const eventItems = document.querySelectorAll(".event-item");
    eventItems.forEach(item => {
        item.addEventListener("mouseenter", () => {
            item.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.5)";
        });

        item.addEventListener("mouseleave", () => {
            item.style.boxShadow = "none";
        });
    });

    // Add confirmation before submitting an RSVP
    const rsvpButtons = document.querySelectorAll(".button.rsvp");
    rsvpButtons.forEach(button => {
        /*button.addEventListener("click", (event) => {
            const confirmation = confirm("Are you sure you want to RSVP for this event?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
*/  });
});
