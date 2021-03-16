var song = new Audio();
var isStopped = true;
var currentSong = 0;
var playlist = [];
var playlistVisible = false;

function skip(to) {
  if (to == "prev") {
    stop();
    currentSong = --currentSong % playlist.length;
    if (currentSong < 0) {
      currentSong += playlist.length;
    }
    playpause();
  } else if (to == "next") {
    stop();
    currentSong = ++currentSong % playlist.length;
    playpause();
  }
}

function playpause() {
  if (!song.paused) {
    song.pause();
    document.getElementById("glow").classList.add("disable-animation");
  } else if (playlist.length == 0) {
    togglePlaylist();
  } else {
    if (isStopped) {
      song.src = playlist[currentSong];
    }
    song.play();
    songFile = playlist[currentSong].split("/");
    songName = document.getElementById("songName");
    songName.innerHTML = songFile[songFile.length - 1];
    document.getElementById("glow").classList.remove("disable-animation");
    isStopped = false;
  }
}

function stop() {
  song.pause();
  document.getElementById("glow").classList.add("disable-animation");
  song.currentTime = 0;
  document.getElementById("seek").value = 0;
  isStopped = true;
  document.getElementById("songName").innerHTML = "Music title";
}

function setPos(pos) {
  song.currentTime = pos;
}

function mute() {
  if (song.muted) {
    song.muted = false;
    document.getElementById("mute").className = "fa fa-volume-up";
    document.getElementById("volume").value = 1;
  } else {
    song.muted = true;
    document.getElementById("mute").className = "fa fa-volume-off";
    document.getElementById("volume").value = 0;
  }
}

function setVolume(volume) {
  song.volume = volume;
}

function togglePlaylist() {
  if (playlistVisible) {
    document.getElementById("playlist").className = "hide";
    document.getElementById("player").className = "";
    playlistVisible = false;
  } else {
    document.getElementById("player").className = "hide";
    document.getElementById("playlist").className = "";
    playlistVisible = true;
  }
}

function addList(playlist) {
  playlist.forEach((file, index) => {
    fileUrl = file.split("/")[3].split(".")[0];
    if (fileUrl != "") {
      parent = document.getElementById("list");
      listItem = document.createElement("div");
      listItem.setAttribute("class", "list-item");
      listItem.setAttribute("index", index);

      wrapper = document.createElement("div");
      wrapper.setAttribute("class", "wrap-text");

      span = document.createElement("span");
      span.innerText = fileUrl;

      wrapper.appendChild(span);
      listItem.appendChild(wrapper);

      btn1 = document.createElement("button");
      btn1.setAttribute("onclick", "removeList(this)");
      btn1.innerText = "&times;";

      btn2 = document.createElement("button");
      // btn2.setAttribute('onclick','removeList(this)');

      trashIcon = document.createElement("i");
      trashIcon.className = "fa fa-trash";

      btn2.appendChild(trashIcon);
      listItem.appendChild(btn1);
      listItem.appendChild(btn2);
      parent.appendChild(listItem);
    }
  });
  document.getElementById("sourceUrl").value = "";
}

function removeList(item) {
  index = playlist.indexOf(item.parentElement.firstChild.innerText);
  if (index != -1) {
    playlist.splice(index, 1);
    item.parentElement.remove();
  }
}

song.addEventListener("error", function () {
  stop();
  document.getElementById("songName").innerHTML = "Error Loading Audio";
});

song.addEventListener("timeupdate", function () {
  curtime = parseInt(song.currentTime, 10);
  document.getElementById("seek").max = song.duration;
  document.getElementById("seek").value = curtime;
});

song.addEventListener("ended", function () {
  song.pause();
  song.currentTime = 0;
  document.getElementById("seek").value = 0;
  if (currentSong + 1 >= playlist.length) {
    currentSong = 0;
  } else {
    currentSong++;
  }
  stop();
  song.src = playlist[currentSong];
  playpause();
});


var input = document.getElementById("sourceUrl");
input.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    // addList();
  }
});

const sources = document.getElementById("audio-src").textContent;
const parser = (sources) => {
  const obj = JSON.parse(sources);
  const cleanUrl = obj.audio.map((url) => url.audio);
  playlist = cleanUrl;
  addList(playlist);
};
parser(sources);

// document.getElementById('sourceUrl').value = "http://localhost:8000/media/music/Blake_Shelton_-_Happy_Anywhere_feat._Gwen_Stefani_Official_Music_Video.opus";
// addList();
// document.getElementById("glow").classList.remove("disable-animation");

const darkToggler = document.getElementById('dark-theme')
const fanDivs = document.querySelectorAll('.fan')
const formFields = document.querySelectorAll('.form-control')

const changeTheme = (value) =>{
    if (parseInt(value) === 0){
        fanDivs.forEach(div =>{
            div.classList.remove('bg-dark')
            div.classList.add('bg-light')
            document.body.style.backgroundColor = 'antiquewhite'
            document.body.style.color = '#000'
        })
        formFields.forEach(field =>{
            field.classList.remove('bg-dark')
            field.classList.add('text-dark')
            field.classList.remove('text-white')
        })      
        darkToggler.style.border = '1px solid antiquewhite'
    }else if (parseInt(value) === 1){
        fanDivs.forEach(div =>{
            div.classList.remove('bg-light')
            div.classList.add('bg-dark')
            document.body.style.backgroundColor = 'rgb(30, 35, 39, 0.911)'
            document.body.style.color = '#fff'
        })
        formFields.forEach(field =>{
            field.classList.add('bg-dark')
            field.classList.remove('text-dark')
            field.classList.add('text-white')
        })
    }
}

const data = localStorage.getItem('dark-theme')
if (data){
    darkToggler.value = data 
    changeTheme(darkToggler.value)
}else{
    changeTheme(1)
}

darkToggler.onchange = (e) => {
    localStorage.setItem('dark-theme', e.target.value)
    changeTheme(e.target.value)
}
