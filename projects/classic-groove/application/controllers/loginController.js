const login = () => {
  if (!checkInputLogin()) return;
  let username = document.querySelector("#username-field").value;
  let password = document.querySelector("#password-field").value;
  $.ajax({
    url: "util/user.php",
    type: "POST",
    data: { user: username, pass: password, action: "checkLogin" },
    success: function (res) {
      if (res == "cus") {
        window.location.href = "index.php";
      } else if (res == "emp") window.location.href = "admin.php";
      else {
        customNotice("fa-sharp fa-light fa-circle-exclamation", res,3);
      }
    },
  });
};

const checkInputLogin = () => {
  let username = document.querySelector("#username-field").value;
  if (username == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter username!",3
    );
    document.querySelector("#username-field").focus();
    return false;
  }
  let password = document.querySelector("#password-field").value;
  if (password == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your password!",3
    );
    document.querySelector("#password-field").focus();
    return false;
  }
  return true;
};

const logout = () => {
  $.ajax({
    url: "util/logout.php",
    type: "GET",
    success: function () {
      window.location.href = "index.php";
    },
  });
};

const register = async () => {
  if (!(await checkInputRegister())) return;
  let name = document.querySelector("#login .register .name").value;
  let phone = document.querySelector("#login .register .phonenumber").value;
  let username = document.querySelector("#login .register .username").value;
  let password = document.querySelector("#login .register .password").value;
  $.ajax({
    url: "util/user.php",
    type: "POST",
    data: {
      name: name,
      phone: phone,
      user: username,
      pass: password,
      action: "register",
    },
    success: function (res) {
      if (res == "Success") {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Accout successfully created!",1
        );
        loadLoginByAjax("logIn");
        document.querySelector("#username-field").value = username;
        document.querySelector("#password-field").value = password;
      } else
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Accout creation failed!",3
        );
    },
  });
};

const checkInputRegister = async () => {
  let name = document.querySelector("#login .register .name");
  let phone = document.querySelector("#login .register .phonenumber");
  let username = document.querySelector("#login .register .username");
  let password = document.querySelector("#login .register .password");
  let confirmPassword = document.querySelector(
    "#login .register .confirmPassword"
  );
  if (name.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your name!",3
    );
    name.focus();
    return false;
  }
  if (phone.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your phone number!",3
    );
    phone.focus();
    return false;
  }
  if (!isVietnamesePhoneNumberValid(phone.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Invalid phone number!",3
    );
    phone.focus();
    return false;
  }
  if (username.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter username!",3
    );
    username.focus();
    return false;
  }
  if (await isUsernameExist(username.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Username already exists!",3
    );
    username.focus();
    return false;
  }
  if (password.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your password!",3
    );
    password.focus();
    return false;
  }
  if (!isPasswordValid(password.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Password that contain at least eight characters, including at least one number and includes both lowercase and uppercase letters and special characters, for example #, ?, !.",3
    );
    password.focus();
    return false;
  }

  if (confirmPassword.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter confirm password!",3
    );
    confirmPassword.focus();
    return false;
  }
  if (confirmPassword.value != password.value) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      " Confirm password incorrect!",3
    );
    confirmPassword.focus();
    return false;
  }
  return true;
};

function isVietnamesePhoneNumberValid(number) {
  return /(((\+|)84)|0)(3|5|7|8|9)+([0-9]{8})\b/.test(number);
}

function isPasswordValid(password) {
  return /^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/.test(
    password
  );
}

const isUsernameExist = (username) => {
  return $.ajax({
    url: "util/user.php",
    type: "POST",
    data: { user: username, action: "checkUsernameExist" },
  });
};

const isLogin = () => {
  return $.ajax({
    url: "util/user.php?action=isLogin",
    type: "GET",
  });
};

const getRole = () => {
  return $.ajax({
    url: "util/user.php?action=getRole",
    type: "GET",
  });
};

// Make sure to export the function
module.exports = { login, checkInputLogin, logout, register, checkInputRegister, isVietnamesePhoneNumberValid, isPasswordValid, isUsernameExist, isLogin, getRole };