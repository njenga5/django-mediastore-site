const video = videojs("video", {
  controls: true,
  playbackRates: [0.25, 0.5, 1, 2],
  preload: "auto",
  responsive: true,
  controls: true,
  breakpoints: {
    tiny: 300,
    xsmall: 400,
    small: 500,
    medium: 600,
    large: 700,
    xlarge: 800,
    huge: 900,
  },
});

const title = document.getElementById("title");
const artist = document.getElementById("artist");
const playBtns = document.querySelectorAll(".play-btn");
const sources = document.getElementById("vid-sources").textContent;

const initialState = (playBtns) => {
  playBtns.forEach((element) => {
    element.removeAttribute("disabled");
    element.children[0].classList.add("btn-outline-primary");
    element.children[0].classList.remove("disabled");
    element.children[0].classList.remove("btn-outline-secondary");
    element.children[0].textContent = "Play";
  });
};

const dynamicState = (event) => {
  event.target.parentNode.setAttribute("disabled", "true");
  event.target.classList.remove("btn-outline-primary");
  event.target.classList.add("disabled");
  event.target.classList.add("btn-outline-secondary");
  event.target.textContent = "Playing";
};
const autoState = (playBtns, counter) => {
  playBtns[counter].setAttribute("disabled", "true");
  playBtns[counter].children[0].classList.remove("btn-outline-primary");
  playBtns[counter].children[0].classList.add("disabled");
  playBtns[counter].children[0].classList.add("btn-outline-secondary");
  playBtns[counter].children[0].textContent = "Playing";
};

const parser = (src) => {
  const obj = JSON.parse(src).sources;
  var counter = 0;

  initialState(playBtns);
  autoState(playBtns, counter);

  video.src(obj[counter]);
  video.poster(obj[counter].poster);
  title.innerText = `${
    obj[counter].title.length > 29
      ? obj[counter].title.substring(0, 29) + "..."
      : obj[counter].title
  }`;
  artist.innerText = `${
    obj[counter].artist.length > 29
      ? obj[counter].artist.substring(0, 29) + "..."
      : obj[counter].artist
  }`;
  // video.play()
  playBtns.forEach((item, key) => {
    item.addEventListener("click", (event) => {
      video.src(obj[key]);
      title.innerText = `${
        obj[key].title.length > 29
          ? obj[key].title.substring(0, 29) + "..."
          : obj[key].title
      }`;
      artist.innerText = `${
        obj[key].artist.length > 29
          ? obj[key].artist.substring(0, 29) + "..."
          : obj[key].artist
      }`;
      counter = key;
      video.play();
      initialState(playBtns);
      dynamicState(event);
    });
  });

  video.on("ended", () => {
    counter++;
    if (counter >= obj.length) {
      counter = 0;
    }
    initialState(playBtns);
    autoState(playBtns, counter);
    video.src(obj[counter]);
    title.innerText = `${
      obj[counter].title.length > 29
        ? obj[counter].title.substring(0, 29) + "..."
        : obj[counter].title
    }`;
    artist.innerText = `${
      obj[counter].artist.length > 29
        ? obj[counter].artist.substring(0, 29) + "..."
        : obj[counter].artist
    }`;
    video.play();
  });
};

parser(sources);

const enablePreview = () => {
  const interval = setInterval(() => {
    const videos = document.querySelectorAll(".video");

    videos.forEach((video) => {
      video.onmouseover = () => {
        let duration = video.duration;
        setInterval(() => {
          if (video.currentTime >= 6 && video.currentTime <= 8) {
            video.currentTime = duration / 2;
          } else if (
            video.currentTime >= 8 &&
            video.currentTime >= duration / 2 + 5 &&
            video.currentTime < duration
          ) {
            video.currentTime = 1;
          }
          video.play();
        }, 500);
      };
    });

    const sources2 = JSON.parse(sources).sources;
    videos.forEach((video, index) => {
      const holder = document.getElementById(index.toString());
      video.onmouseout = () => {
        holder.innerHTML = `<video
           poster="${sources2[index].poster}"
           src="${sources2[index].src}"
           class="card-img-top video"
           width="100%"
           height="225"
           preserveAspectRatio="xMidYMid slice"
           focusable="false"
           role="img"
           muted
         ></video>`;
         clearInterval(interval)
      };
    });
  }, 2000);
};
//enablePreview()

