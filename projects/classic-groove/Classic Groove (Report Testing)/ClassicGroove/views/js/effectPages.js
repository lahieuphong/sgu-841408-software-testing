let changeInputColorRange = () => {
  let input = document.querySelector(".seek_slider");
  let value = ((input.value - input.min) / (input.max - input.min)) * 100;
  input.style.background =
    "linear-gradient(to right, #f2623e 0%, #f2623e " +
    value +
    "%, #fff " +
    value +
    "%, white 100%)";
};



const changeToolTip = (input) => {
  let val = parseInt(input.value);
  let tooltip = document.querySelector("#search .tooltiptext");
  if (val == 0) tooltip.innerHTML = "All";
  else tooltip.innerHTML = (val - 1) * 100 + " - " + val * 100 + " $";
};

let active = 0;
const nextSlide = () => {
  let items = document.querySelectorAll(".slider .list .item");
  let lengthItems = items.length - 1;
  active = active + 1 <= lengthItems ? active + 1 : 0;
  reloadSlider();
};
const prevSlide = () => {
  let items = document.querySelectorAll(".slider .list .item");
  let lengthItems = items.length - 1;
  active = active - 1 >= 0 ? active - 1 : lengthItems;
  reloadSlider();
};
let refreshInterval = setInterval(() => {
  let nextBtn = document.getElementById("next");
  if (nextBtn != null) nextBtn.click();
}, 3000);

const reloadSlider = () => {
  let slider = document.querySelector(".slider .list");
  let dots = document.querySelectorAll(".slider .dots li");
  slider.style.left = -78 * active + "vw";

  let last_active_dot = document.querySelector(".slider .dots li.active");
  last_active_dot.classList.remove("active");
  dots[active].classList.add("active");

  clearInterval(refreshInterval);
  refreshInterval = setInterval(() => {
    let next = document.querySelector("#next");
    if (next != null) next.click();
  }, 3000);
};

const changeSlide = (key) => {
  active = key;
  reloadSlider();
};

window.addEventListener("resize", function () {
  if (window.innerWidth <= 1000) {
    document.querySelector(
      "#header > div > div.top > div.logo-placeholder > img"
    ).src = "views/assets/img/Logo2.png";
  } else {
    document.querySelector(
      "#header > div > div.top > div.logo-placeholder > img"
    ).src = "views/assets/img/Logo.png";
  }
});
let rotationDegrees = 0;
const turnArrow = (arrow) => {
  rotationDegrees -= 180;
  arrow.style.transform = `rotate(${rotationDegrees}deg)`;
};
