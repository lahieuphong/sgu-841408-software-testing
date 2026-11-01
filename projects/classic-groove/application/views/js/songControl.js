let playpause_btn = document.querySelector(".playpause-track");
let next_btn = document.querySelector(".next-track");
let seek_slider = document.querySelector(".seek_slider");
let prev_btn = document.querySelector(".prev-track");
let curr_time = document.querySelector(".current-time");
let total_duration = document.querySelector(".total-duration");
let volume_slider = document.querySelector(".volume_slider");
let track_name = document.querySelector(".track-name");

let track_index = 0;
let isPlaying = false;
let updateTimer;

let curr_track = document.createElement("audio");

let track_list;
async function playTrackList(albumID) {
  await $.ajax({
    url: "views/js/songs.php",
    type: "POST",
    dataType: "json",
    data: { albumID: albumID },
    success: function (data) {
      track_list = data;
      // console.log(data);
    },
  });
  loadTrack(0);
  $("#song-control").css("display", "flex");
}
function loadTrack(track_index) {
  clearInterval(updateTimer);
  resetValues();
  curr_track.src = "data/songs/" + track_list[track_index].linkFile + ".mp3";
  curr_track.load();
  playTrack();

  // track_art.style.backgroundImage = "url(" + track_list[track_index].image + ")";
  track_name.textContent = track_list[track_index].tenBaiHat;
  // track_artist.textContent = track_list[track_index].artist;
  // now_playing.textContent = "PLAYING " + (track_index + 1) + " OF " + track_list.length;

  updateTimer = setInterval(seekUpdate, 1000);
  curr_track.addEventListener("ended", nextTrack);
}

function resetValues() {
  curr_time.textContent = "00:00";
  total_duration.textContent = "00:00";
  seek_slider.value = 0;
}

function playpauseTrack() {
  if (!isPlaying) playTrack();
  else pauseTrack();
}

function playTrack() {
  curr_track.play();
  isPlaying = true;
  playpause_btn.innerHTML = '<i class="fa-solid fa-circle-pause"></i>';
}

function pauseTrack() {
  curr_track.pause();
  isPlaying = false;
  playpause_btn.innerHTML = '<i class="fa-solid fa-circle-play"></i>';
}
function nextTrack() {
  if (track_index < track_list.length - 1) track_index += 1;
  else track_index = 0;
  loadTrack(track_index);
  playTrack();
}

function prevTrack() {
  if (track_index > 0) track_index -= 1;
  else track_index = track_list.length;
  loadTrack(track_index);
  playTrack();
}

function seekTo() {
  let seekto = curr_track.duration * (seek_slider.value / 100);
  curr_track.currentTime = seekto;
}

function setVolume() {
  curr_track.volume = volume_slider.value / 100;
}
function seekUpdate() {
  let seekPosition = 0;

  if (!isNaN(curr_track.duration)) {
    seekPosition = curr_track.currentTime * (100 / curr_track.duration);

    seek_slider.value = seekPosition;

    let currentMinutes = Math.floor(curr_track.currentTime / 60);
    let currentSeconds = Math.floor(
      curr_track.currentTime - currentMinutes * 60
    );
    let durationMinutes = Math.floor(curr_track.duration / 60);
    let durationSeconds = Math.floor(
      curr_track.duration - durationMinutes * 60
    );

    if (currentSeconds < 10) {
      currentSeconds = "0" + currentSeconds;
    }
    if (durationSeconds < 10) {
      durationSeconds = "0" + durationSeconds;
    }
    if (currentMinutes < 10) {
      currentMinutes = "0" + currentMinutes;
    }
    if (durationMinutes < 10) {
      durationMinutes = "0" + durationMinutes;
    }

    curr_time.textContent = currentMinutes + ":" + currentSeconds;
    total_duration.textContent = durationMinutes + ":" + durationSeconds;
    changeInputColorRange();
  }
}
const closeSong = () => {
  curr_track.pause();
  isPlaying = false;
  document.querySelector("#song-control").style.display = "none";
};

const setVolumeMute = () => {
  let unmute = document.querySelector(".volume-container i:nth-of-type(1)");
  let mute = document.querySelector(".volume-container i:nth-of-type(2)");
  if (mute.style.display == "none") {
    unmute.style.display = "none";
    mute.style.display = "block";
    curr_track.muted = true;
  } else {
    unmute.style.display = "block";
    mute.style.display = "none";
    curr_track.muted = false;
  }
};
