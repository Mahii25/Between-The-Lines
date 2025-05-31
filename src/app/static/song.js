// Handles audio playback and progress bar updates
console.log("Song page JS loaded!");

// Main player element and custom progress bar
const player = document.getElementById('main-player');
const progressBar = document.querySelector('.footer-progress');
const progressFill = document.querySelector('.progress-fill');
const progressThumb = document.querySelector('.progress-thumb');
const progressBarDiv = document.querySelector('.footer-progress-bar');

// Update bar + thumb as audio plays
player.addEventListener('timeupdate', () => {
    if (!player.duration) return;

    const percent = (player.currentTime / player.duration) * 100;
    progressFill.style.width = percent + '%';
    progressThumb.style.left = percent + '%';
});

// Seek when clicking the bar
function seekTrack(e) {
    if (!player.duration) return;

    const rect = progressBarDiv.getBoundingClientRect();
    const offsetX = e.clientX - rect.left;
    const percent = offsetX / rect.width;

    player.currentTime = percent * player.duration;
}

// // Playlist items and data
// const playlistItems = document.querySelectorAll('#playlist .playlist-item');
// let playlist = Array.from(playlistItems).map(item => item.getAttribute('data-preview'));
// let currentIndex = -1;

// // Update CSS var for played percentage
// function setProgressBackground(el, percent) {
//     el.style.setProperty('--progress', percent + '%');
// }

// Play next track in playlist
function playNext() {
    currentIndex += 1;
    if (currentIndex < playlist.length) {
        player.src = playlist[currentIndex];
        player.play();
    }
}

// Bind events if elements exist
if (player && progressBar) {
    // When track ends, go to next
    player.addEventListener('ended', playNext);

    // Update progress bar as audio plays
    player.addEventListener('timeupdate', () => {
        if (!player.duration) return;
        const pct = (player.currentTime / player.duration) * 100;
        progressBar.value = pct;
        setProgressBackground(progressBar, pct);
    });

    // Seek audio when progress bar changes
    progressBar.addEventListener('input', () => {
        if (!player.duration) return;
        const pct = progressBar.value;
        setProgressBackground(progressBar, pct);
        player.currentTime = (pct / 100) * player.duration;
    });
}

// Play/pause toggle (wired to button onclick)
function togglePlay() {
    if (player.paused) {
        player.play();
    } else {
        player.pause();
    }
}