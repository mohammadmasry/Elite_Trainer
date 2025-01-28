document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('edit-player-form');
    const statisticsField = document.getElementById('statistics');

    // Validate JSON in the statistics field
    form.addEventListener('submit', (e) => {
        const statisticsValue = statisticsField.value.trim();
        if (statisticsValue) {
            try {
                JSON.parse(statisticsValue);
            } catch (err) {
                e.preventDefault();
                alert('Invalid JSON in the Statistics field. Please correct it.');
            }
        }
    });
});
