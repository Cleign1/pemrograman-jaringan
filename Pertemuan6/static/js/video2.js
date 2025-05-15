$(document).ready(function () {
    var video = document.getElementById("videoPlayer2");
    var playBtn = document.getElementById("playBtn2");
    var pauseBtn = document.getElementById("pauseBtn2");
    var fullScreenBtn = document.getElementById("fullScreenBtn2");
    var muteBtn = document.getElementById("muteBtn2");

    video.muted = false;
    video.volume = 0.5;
    var lastVolume = video.volume;

    playBtn.addEventListener("click", function () {
        video.play();
    });

    pauseBtn.addEventListener("click", function () {
        video.pause();
    });

    fullScreenBtn.addEventListener("click", function () {
        if (video.requestFullscreen) {
            video.requestFullscreen();
        } else if (video.mozRequestFullScreen) {
            video.mozRequestFullScreen();
        } else if (video.webkitRequestFullscreen) {
            video.webkitRequestFullscreen();
        }
    });
    muteBtn.addEventListener("click", function () {
        if (video.muted) {
            video.muted = false;
            video.volume = lastVolume;
            muteBtn.innerHTML = "Mute";
        } else {
            lastVolume = video.volume;
            video.muted = true;
            video.volume = 0;
            muteBtn.innerHTML = "Unmute";
        }
    })
});