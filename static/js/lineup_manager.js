document.addEventListener('DOMContentLoaded', () => {
    const positions = document.querySelectorAll('.position');
    const playersList = document.querySelector('.players-list ul');

    let draggedPlayer = null;

    // Attach drag event listeners to players
    function attachDragEvents(player) {
        player.addEventListener('dragstart', () => {
            draggedPlayer = player;
        });

        player.addEventListener('dragend', () => {
            draggedPlayer = null;
        });
    }

    // Attach drag events to all players
    document.querySelectorAll('.player').forEach(player => attachDragEvents(player));

    // Handle positions
    positions.forEach(position => {
        position.addEventListener('dragover', e => {
            e.preventDefault();
            position.classList.add('dragover');
        });

        position.addEventListener('dragleave', () => {
            position.classList.remove('dragover');
        });

        position.addEventListener('drop', () => {
            if (draggedPlayer) {
                position.textContent = draggedPlayer.textContent;
                position.dataset.playerId = draggedPlayer.dataset.playerId;
                position.classList.add('assigned');
                position.classList.remove('dragover');
                draggedPlayer.remove();
            }
        });

        position.addEventListener('click', () => {
            if (position.classList.contains('assigned')) {
                const newPlayer = document.createElement('li');
                newPlayer.textContent = position.textContent;
                newPlayer.dataset.playerId = position.dataset.playerId;
                newPlayer.classList.add('player');
                newPlayer.setAttribute('draggable', 'true');
                playersList.appendChild(newPlayer);
                attachDragEvents(newPlayer);
                position.textContent = position.dataset.position;
                position.classList.remove('assigned');
                delete position.dataset.playerId;
            }
        });
    });
});
