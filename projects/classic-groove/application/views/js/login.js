function eyePassword() {
  let password = document.getElementById("password-field");
  let eyeicon = document.getElementById("eyeicon");
  if (password.type == "password") {
    password.type = "text";
    eyeicon.className = "fa-thin fa-eye";
  } else {
    password.type = "password";
    eyeicon.className = "fa-thin fa-eye-slash";
  }
};
function eyePassword2() {
  let password = document.getElementById("password-field2");
  let eyeicon2 = document.getElementById("eyeicon2");
  if (password.type == "password") {
    password.type = "text";
    eyeicon2.className = "fa-thin fa-eye";
  } else {
    password.type = "password";
    eyeicon2.className = "fa-thin fa-eye-slash";
  }
};
function eyePassword3() {
  let password = document.getElementById("password-field3");
  let eyeicon3 = document.getElementById("eyeicon3");
  if (password.type == "password") {
    password.type = "text";
    eyeicon3.className = "fa-thin fa-eye";
  } else {
    password.type = "password";
    eyeicon3.className = "fa-thin fa-eye-slash";
  }
};
function eyePasswordProfile() {
  let password = document.getElementById("password-field4");
  let eyeicon4 = document.getElementById("eyeicon4");
  if (password.type == "password") {
    password.type = "text";
    eyeicon4.className = "fa-thin fa-eye";
  } else {
    password.type = "password";
    eyeicon4.className = "fa-thin fa-eye-slash";
  }
};