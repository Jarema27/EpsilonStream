function playSong(songSrc) {
    var audio = $('#audioPlayer');
    audio.attr('src', songSrc);

    audio[0].pause();
    audio[0].load();
    audio[0].play();
}

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
}

window.onload = function() {
  var frm = document.getElementById('f');
  setTimeout(function() {
      frm.submit();
  }, 3000);
};