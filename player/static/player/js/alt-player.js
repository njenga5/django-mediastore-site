const _ = (query) => {
  return document.querySelector(query);
};
const _all = (query) => {
  return document.querySelectorAll(query);
};
let songList = JSON.parse(document.getElementById("audio-src").textContent).audio;

let currentSongIndex = 0;

let player = _(".player"),
  toggleSongList = _(".player .toggle-list");

let main = {
  audio: _(".player .main audio"),
  thumbnail: _(".player .main img"),
  seekbar: _(".player .main input"),
  songname: _(".player .main .details h2"),
  artistname: _(".player .main .details p"),
  prevControl: _(".player .main .controls .prev-control"),
  playPauseControl: _(".player .main .controls .play-pause-control"),
  nextControl: _(".player .main .controls .next-control"),
  currTime: _("#currTime"),
  duration: _("#duration"),
};

toggleSongList.addEventListener("click", () => {
  toggleSongList.classList.toggle("active");
  if (toggleSongList.classList.contains("active")) {
    toggleSongList.children[0].classList.toggle("fa-angle-down");
  } else {
    toggleSongList.children[0].classList.toggle("fa-angle-up");
  }

  player.classList.toggle("activeSongList");
});

_(".player .player-list .list").innerHTML = songList
  .map((song, songIndex) => {
    return `
		<div class="item" songIndex="${songIndex}">
			<div class="thumbnail">
				<img src="${song.thumbnail}">
			</div>
			<div class="details">
				<h2>${song.songname}</h2>
			 	<p>${song.artistname}</p>
			</div>
			<div class="download-btn">
				<button>
					<a href="${song.audio}" download="${song.songname}">
					<i class="fa fa-download"></i></a>
				</button>
				<button>
					<a href="/edit/find/music/${song.id}"><i class="fa fa-trash"></i></a>
				</button>
			</div>
		</div>
	`;
  })
  .join("");

let songListItems = _all(".player .player-list .list .item");
for (let i = 0; i < songListItems.length; i++) {
  songListItems[i].addEventListener("click", () => {
    currentSongIndex = parseInt(songListItems[i].getAttribute("songIndex"));
    loadSong(currentSongIndex);
    // player.classList.remove("activeSongList");
  });
}

const calcTime = (timeNow, node) => {
  if (timeNow >= 60) {
    let seconds = parseInt(Math.round(timeNow % 60));
    let minutes = parseInt(timeNow / 60);
    let hours = 0;
    if (minutes >= 60) {
      hours = parseInt(minutes / 60);
      if (hours < 10) {
        hours = "0" + hours;
      }
      minutes = parseInt(minutes % 60);
    }
    if (minutes < 10) {
      minutes = "0" + minutes;
    }
    if (seconds < 10) {
      seconds = "0" + seconds;
    }
    node.innerText = hours > 0 ? hours + ":" + minutes + ":" + seconds : minutes + ":" + seconds;
  } else {
    node.innerText =
      timeNow < 10
        ? "00" + ":" + "0" + parseInt(Math.round(timeNow))
        : "00" + ":" + parseInt(Math.round(timeNow));
  }
};

const loadSong = (songIndex) => {
  if (songList.length > 0) {
    let song = songList[songIndex];
    main.thumbnail.setAttribute("src", song.thumbnail);
    document.body.style.background = `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.8)), url("${song.thumbnail}") center no-repeat`;
    document.body.style.backgroundSize = "cover";
    main.songname.innerText = song.songname;
    main.artistname.innerText = song.artistname;
    main.audio.setAttribute("src", song.audio);
    main.seekbar.setAttribute("value", 0);
    main.seekbar.setAttribute("min", 0);
    main.seekbar.setAttribute("max", 0);
    main.currTime.innerText = "__:__";
    main.audio.addEventListener("canplay", () => {
      main.audio.play();
      if (!main.audio.paused) {
        main.playPauseControl.children[0].classList.add("fa-pause");
      }
      main.currTime.innerText = "00:00";
      let timeNow2 = main.audio.duration;
      main.seekbar.setAttribute("max", parseInt(timeNow2));
      calcTime(timeNow2, main.duration);
      main.audio.onended = () => {
        main.nextControl.click();
      };
    });
  } else {
    main.thumbnail.setAttribute("src", "/static/player/images/default-art.jpg");
  }
};
setInterval(() => {
  let timeNow1 = main.audio.currentTime;
  main.seekbar.value = parseInt(timeNow1);
  calcTime(timeNow1, main.currTime);
}, 1000);

main.prevControl.addEventListener("click", () => {
  currentSongIndex--;
  if (currentSongIndex < 0) {
    currentSongIndex = songList.length + currentSongIndex;
  }
  loadSong(currentSongIndex);
});
main.nextControl.addEventListener("click", () => {
  currentSongIndex = (currentSongIndex + 1) % songList.length;
  loadSong(currentSongIndex);
});
main.playPauseControl.addEventListener("click", () => {
  if (main.audio.paused) {
    main.playPauseControl.children[0].classList.add("fa-pause");
    main.audio.play();
  } else {
    main.playPauseControl.children[0].classList.add("fa-play");
    main.audio.pause();
  }
});
main.seekbar.addEventListener("change", () => {
  let timeNow = main.seekbar.value;
  main.audio.currentTime = timeNow;

  calcTime(timeNow, main.currTime);
});

main.seekbar.onmouseover = () => {
  main.seekbar.title = main.currTime.innerText;
};

loadSong(currentSongIndex);
