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
    huge: 900
  },
});

const title = document.getElementById("title");
const artist = document.getElementById("artist");
const playBtns = document.querySelectorAll(".play-btn");

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
  playBtns[counter].children[0].textContent = "Playing"

};

const parser = (src) => {
  const obj = JSON.parse(src);
  var counter = 0;

  
  initialState(playBtns);
  autoState(playBtns, counter);

  video.src(obj.sources[counter]);
  video.poster(obj.sources[counter].poster)
  title.innerText = `${obj.sources[counter].title.length > 29?obj.sources[counter].title.substring(0, 29)+'...':obj.sources[counter].title}`;
  artist.innerText = `${obj.sources[counter].artist.length > 29?obj.sources[counter].artist.substring(0, 29)+'...':obj.sources[counter].artist}`;
  // video.play()
  playBtns.forEach((item, key) => {
    item.addEventListener("click", (event) => {
      video.src(obj.sources[key]);
      title.innerText = `${obj.sources[key].title.length > 29?obj.sources[key].title.substring(0, 29)+'...':obj.sources[key].title}`;
      artist.innerText = `${obj.sources[key].artist.length > 29?obj.sources[key].artist.substring(0, 29)+'...':obj.sources[key].artist}`;
      counter = key;
      video.play();
      initialState(playBtns, );
      dynamicState(event);
    });
  });

  video.on("ended", () => {
    counter++;
    if (counter >= obj.sources.length) {
      counter = 0;
    }
    initialState(playBtns);
    autoState(playBtns, counter);
    video.src(obj.sources[counter]);
    title.innerText = `${obj.sources[counter].title.length > 29?obj.sources[counter].title.substring(0, 29)+'...':obj.sources[counter].title}`;
    artist.innerText = `${obj.sources[counter].artist.length > 29?obj.sources[counter].artist.substring(0, 29)+'...':obj.sources[counter].artist}`;
    video.play();
  });
};

const sources = document.getElementById("vid-sources").textContent;
parser(sources);
