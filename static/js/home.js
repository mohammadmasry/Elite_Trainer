// app.js

document.addEventListener("DOMContentLoaded", () => {
    // Welcome alert
   

    // Add hover effect animations
    const links = document.querySelectorAll("ul li a");
    links.forEach(link => {
        link.addEventListener("mouseenter", () => {
            link.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.5)";
        });

        link.addEventListener("mouseleave", () => {
            link.style.boxShadow = "none";
        });
    });
});
