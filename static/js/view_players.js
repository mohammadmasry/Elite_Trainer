// view_players.js

document.addEventListener("DOMContentLoaded", () => {
    // Add hover effects to player items
    const playerItems = document.querySelectorAll(".player-item");
    playerItems.forEach(item => {
        item.addEventListener("mouseenter", () => {
            item.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.5)";
        });

        item.addEventListener("mouseleave", () => {
            item.style.boxShadow = "none";
        });
    });

    // Confirmation before deleting a player
    const deleteButtons = document.querySelectorAll(".button.delete");
    deleteButtons.forEach(button => {
        button.addEventListener("click", (event) => {
            const confirmation = confirm("Are you sure you want to delete this player?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });
});
