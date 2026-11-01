<div class="control-btn">
  <div>
    <i class="fa-solid fa-circle-caret-down fa-xl" onclick="closeSong()" style="
    margin-bottom: 20px;
    font-size: calc(10px + 1vw);
"></i>
  </div>
  <div class="prev-track" onclick="prevTrack()"><i class="fa-solid fa-backward-step"></i></div>
  <div class="playpause-track" onclick="playpauseTrack()"><i class="fa-solid fa-circle-play"></i></div>
  <div class="next-track" onclick="nextTrack()"><i class="fa-solid fa-forward-step"></i></div>
  <div class="volume-container">
    <i class="fa-sharp fa-solid fa-volume" onclick=setVolumeMute()></i>
    <i class="fa-sharp fa-solid fa-volume-slash" style="display:none" onclick=setVolumeMute()></i>
    <div>
      <input type="range" value="99" min="1" max="100" class="volume_slider" oninput="setVolume()">
    </div>
  </div>
</div>
<div class="time-btn">
  <span class="current-time">0:00</span>
  <input type="range" min="0" max="100" value="0" class="seek_slider" onchange="changeInputColorRange(), seekTo()">
  <span class="total-duration">0:30</span>
</div>
<div class="note">
  <span class="track-name">First song on the track list</span>
</div>