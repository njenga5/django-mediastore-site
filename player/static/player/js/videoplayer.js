const video = videojs("video", {
  controls: true,
  playbackRates: [0.25, 0.5, 1, 2],
  preload: "auto",
  responsive: true,
  controls: true,
});

const title = document.getElementById('title')
const parser = (src) => {
    const obj = JSON.parse(src);
    var counter = 0
    video.src(obj.sources[counter])
    title.innerText = obj.sources[counter].title 
    video.on('ended', ()=>{
      counter++
      if(counter >= obj.sources.length){
          counter = 0
          video.src(obj.sources[counter])
          title.innerText = obj.sources[counter].title
          video.play()
        }else{
            video.src(obj.sources[counter])
            title.innerText = obj.sources[counter].title
            video.play()
        }
    })
};

const sources = document.getElementById("vid-sources").textContent;
parser(sources);
