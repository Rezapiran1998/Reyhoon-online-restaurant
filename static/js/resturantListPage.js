function playPause(elem) {
    myVideo = elem.getElementsByClassName('video')[0];

    if (myVideo.paused) {

        myVideo.play();
        myVideo.classList.remove("paused");
    }
    else {

        myVideo.pause();
        myVideo.classList.add("paused");
    }
} 