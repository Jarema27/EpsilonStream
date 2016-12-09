function playSong(songSrc) {
    var audio = $('#audioPlayer');
    audio.attr('src', songSrc);

    audio[0].pause();
    audio[0].load();
    audio[0].play();
}