let fullname = null;
let phone = null;
let password = null;
let address = null;
let email = null;
let isDiff = false;

const setUserInfo = () => {
  fullname = document.querySelector("#myaccount #txtHoTen").value;
  phone = document.querySelector("#myaccount #txtSDT").value;
  // password = document.querySelector("#myaccount #password-field4").value;
  address = document.querySelector("#myaccount #txtAddress").value;
  email = document.querySelector("#myaccount #txtEmail").value;
};
const IsInfoChange = () => {
  let saveBtn = document.querySelector("#myaccount .btnSave");
  if (
    fullname == document.querySelector("#myaccount #txtHoTen").value &&
    phone == document.querySelector("#myaccount #txtSDT").value &&
    // password == document.querySelector("#myaccount #password-field4").value &&
    address == document.querySelector("#myaccount #txtAddress").value &&
    email == document.querySelector("#myaccount #txtEmail").value
  ) {
    saveBtn.style.cursor = "no-drop";
    saveBtn.style.opacity = "0.5";
    isDiff = false;
  } else {
    saveBtn.style.cursor = "pointer";
    saveBtn.style.opacity = "1";
    isDiff = true;
  }
};

const checkInputUpdateUser = () => {
  if (!isDiff) return false;
  let fullnameInput = document.querySelector("#myaccount #txtHoTen");
  let phoneInput = document.querySelector("#myaccount #txtSDT");
  let passwordInput = document.querySelector("#myaccount #password-field4");
  let addressInput = document.querySelector("#myaccount #txtAddress");
  let emailInput = document.querySelector("#myaccount #txtEmail");
  if (fullnameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your fullname!",
      3
    );
    fullnameInput.focus();
    return false;
  }
  if (phoneInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your phone number!",
      3
    );
    phoneInput.focus();
    return false;
  }
  if (!isVietnamesePhoneNumberValid(phoneInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Invalid phone number!",
      3
    );
    phoneInput.focus();
    return false;
  }
  // if (passwordInput.value == "") {
  //   customNotice(
  //     "fa-sharp fa-light fa-circle-exclamation",
  //     "Please, enter your password!",
  //     3
  //   );
  //   passwordInput.focus();
  //   return false;
  // }
  // if (!isPasswordValid(passwordInput.value)) {
  //   customNotice(
  //     "fa-sharp fa-light fa-circle-exclamation",
  //     "Password that contain at least eight characters, including at least one number and includes both lowercase and uppercase letters and special characters, for example #, ?, !.",
  //     3
  //   );
  //   passwordInput.focus();
  //   return false;
  // }
  if (addressInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your address!",
      3
    );
    addressInput.focus();
    return false;
  }
  if (emailInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your email!",
      3
    );
    emailInput.focus();
    return false;
  }
  if (!isEmailValid(emailInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Invalid email!",
      3
    );
    emailInput.focus();
    return false;
  }

  return true;
};
const updateUser = () => {
  if (!checkInputUpdateUser()) return;
  setUserInfo();
  $.ajax({
    url:
      "util/user.php?fullname=" +
      fullname +
      "&phone=" +
      phone +
      "&password=" +
      password +
      "&address=" +
      address +
      "&email=" +
      email +
      "&action=updateUser",
    type: "PUT",
    success: function (res) {
      if (res != "Success") alert(res);
      else {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Update successfully!",
          1
        );
        IsInfoChange();
      }
    },
  });
};
const checkInputUpdatePassword = () => {
  const oldPassword = document.querySelector('#txtOldPassword')
  const newPassword = document.querySelector('#txtNewPassword')
  const confirmNewPassword = document.querySelector('#txtConfirmNewPassword')
  if (oldPassword.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your old Password!",
      3
    );
    oldPassword.focus();
    return false;
  }
  if (newPassword.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your new Password!",
      3
    );
    newPassword.focus();
    return false;
  }
  if (confirmNewPassword.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your confirm New Password!",
      3
    );
    confirmNewPassword.focus();
    return false;
  }

  if (newPassword.value != confirmNewPassword.value) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Password confirm is correct!",
      3
    );
    return false
  }
  return true
}
const updatePassword = () => {
  if (!checkInputUpdatePassword()) return;
  const oldPassword = document.querySelector('#txtOldPassword').value
  const newPassword = document.querySelector('#txtNewPassword').value
  const confirmNewPassword = document.querySelector('#txtConfirmNewPassword').value
  console.log(oldPassword, newPassword, confirmNewPassword)
  $.ajax({
    url:
      "util/user.php?oldPassword=" +
      oldPassword +
      "&newPassword=" +
      newPassword +
      "&confirmNewPassword=" +
      confirmNewPassword +
      "&action=updatePassword",
    type: "PUT",
    success: function (res) {
      if (res != "Success") {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          res,
          3
        );
      }
      else {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Update successfully!",
          1
        );
      }
    },
  });
}

function isEmailValid(email) {
  return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
}

module.exports = {
  setUserInfo,
  IsInfoChange,
  checkInputUpdateUser,
  updateUser,
  checkInputUpdatePassword,
  updatePassword,
};