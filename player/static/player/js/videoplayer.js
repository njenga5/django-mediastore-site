const video = videojs("video", {
  controls: true,
  playbackRates: [0.25, 0.5, 1, 2],
  preload: "auto",
  responsive: true,
  controls: true,
});

const title = document.getElementById("title");
const delBtns = document.querySelectorAll(".delete-btn");
const playBtns = document.querySelectorAll(".play-btn");

const initialState = (playBtns, delBtns) => {
  playBtns.forEach((element) => {
    element.removeAttribute("disabled");
    element.children[0].classList.add("btn-outline-primary");
    element.children[0].classList.remove("disabled");
    element.children[0].classList.remove("btn-outline-secondary");
    element.children[0].textContent = "Play";
  });
  delBtns.forEach((element) => {
    element.removeAttribute("disabled");
    element.children[0].classList.add("btn-outline-danger");
    element.children[0].classList.remove("disabled");
    element.children[0].classList.remove("btn-outline-secondary");
  });
};

const dynamicState = (delBtns, event, key) => {
  event.target.parentNode.setAttribute("disabled", "true");
  event.target.classList.remove("btn-outline-primary");
  event.target.classList.add("disabled");
  event.target.classList.add("btn-outline-secondary");
  event.target.textContent = "Playing";

  delBtns[key].setAttribute("disabled", "true");
  delBtns[key].children[0].classList.remove("btn-outline-danger");
  delBtns[key].children[0].classList.add("disabled");
  delBtns[key].children[0].classList.add("btn-outline-secondary");
};

const autoState = (playBtns, delBtns, counter) => {
  playBtns[counter].setAttribute("disabled", "true");
  playBtns[counter].children[0].classList.remove("btn-outline-primary");
  playBtns[counter].children[0].classList.add("disabled");
  playBtns[counter].children[0].classList.add("btn-outline-secondary");
  playBtns[counter].children[0].textContent = "Playing"

  delBtns[counter].setAttribute("disabled", "true");
  delBtns[counter].children[0].classList.remove("btn-outline-danger");
  delBtns[counter].children[0].classList.add("disabled");
  delBtns[counter].children[0].classList.add("btn-outline-secondary");
};

const parser = (src) => {
  const obj = JSON.parse(src);
  var counter = 0;
  
  initialState(playBtns, delBtns);
  autoState(playBtns, delBtns, counter);

  video.src(obj.sources[counter]);
  title.innerText = `${obj.sources[counter].title.length > 29?obj.sources[counter].title.substring(0, 29)+'...':obj.sources[counter].title}`;
  playBtns.forEach((item, key) => {
    item.addEventListener("click", (event) => {
      video.src(obj.sources[key]);
      title.innerText = `${obj.sources[key].title.length > 29?obj.sources[key].title.substring(0, 29)+'...':obj.sources[key].title}`;
      counter = key;
      video.play();
      initialState(playBtns, delBtns);
      dynamicState(delBtns, event, key);
    });
  });

  video.on("ended", () => {
    counter++;
    if (counter >= obj.sources.length) {
      counter = 0;
      initialState(playBtns, delBtns);
      autoState(playBtns, delBtns, counter);
      video.src(obj.sources[counter]);
      title.innerText = `${obj.sources[counter].title.length > 29?obj.sources[counter].title.substring(0, 29)+'...':obj.sources[counter].title}`;
      video.play();
    } else {
      initialState(playBtns, delBtns);
      autoState(playBtns, delBtns, counter);
      video.src(obj.sources[counter]);
      title.innerText = `${obj.sources[counter].title.length > 29?obj.sources[counter].title.substring(0, 29)+'...':obj.sources[counter].title}`;
      video.play();
    }
  });
};

const sources = document.getElementById("vid-sources").textContent;
parser(sources);
