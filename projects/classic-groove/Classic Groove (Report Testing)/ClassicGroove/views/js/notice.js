const customNotice = async (icon, content, type) => {
  //random number
  let randomNumber = Math.floor(Math.random() * 1000);
  let alert = htmlToElement(
    `<div class="container"><span class="slide"></span><p class="cart-removing"><i class="${icon}"></i> ${content} </p></div>`
  );
  switch (type) {
    case 1: //success
      alert.style.backgroundColor = "#2EA043";
      break;
    case 2: //warning
      alert.style.backgroundColor = "#ffb000";
      break;
    case 3: //error
      alert.style.backgroundColor = "#db161d";
      break;
    default:
      alert.style.backgroundColor = " #f2623e";
  }

  const notice = document.querySelector("#notice");
  notice.appendChild(alert);
  notice.querySelector(".slide").classList.add("slide");
  await sleep(3000);
  notice.querySelector(".slide").style.width = "0";
  alert.classList.add("fade");
  await sleep(800);
  notice.removeChild(alert);
};

const htmlToElement = (html) => {
  var template = document.createElement("template");
  html = html.trim(); // Never return a text node of whitespace as the result
  template.innerHTML = html;
  return template.content.firstChild;
};

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
