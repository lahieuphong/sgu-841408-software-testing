// ADMIN -> ACCOUNT -> edit/new

let nameAcc = null;
let emailAcc = null;
let usernameAcc = null;
let phoneAcc = null;
let roleAcc = null;
let passwordAcc = null;
let addressAcc = null;
let isAccountDiff = false;

const setAccountInfo = () => {
  usernameAcc = document.querySelector("#edit-account .accountID").value;
  nameAcc = document.querySelector("#edit-account .nameAccount").value;
  emailAcc = document.querySelector("#edit-account .emailAccount").value;
  phoneAcc = document.querySelector("#edit-account .phoneAccount").value;
  roleAcc = parseInt(
    document.querySelector("#edit-account .roleAccount").value
  );
  passwordAcc = document.querySelector("#edit-account .passwordAccount").value;
  addressAcc = document.querySelector("#edit-account .addressAccount").value;
};
const updateAccount = () => {
  if (!checkInputUpdateAccount()) return;
  setAccountInfo();
  $.ajax({
    url:
      "util/user.php?fullname=" +
      nameAcc +
      "&email=" +
      emailAcc +
      "&phone=" +
      phoneAcc +
      "&password=" +
      passwordAcc +
      "&address=" +
      addressAcc +
      "&username=" +
      usernameAcc +
      "&role=" +
      roleAcc +
      "&action=updateAccount",
    type: "PUT",
    success: function (res) {
      if (res != "Success") alert(res);
      else {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Update successfully!",
          1
        );
        isAccountInfoChange();
      }
    },
  });
};
const checkInputUpdateAccount = () => {
  if (!isAccountDiff) return false;
  let nameInput = document.querySelector("#edit-account .nameAccount");
  let emailInput = document.querySelector("#edit-account .emailAccount");
  let phoneInput = document.querySelector("#edit-account .phoneAccount");
  let passwordInput = document.querySelector("#edit-account .passwordAccount");
  if (nameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your fullname!",
      3
    );
    nameInput.focus();
    return false;
  }
  if (emailInput.value != "" && !isEmailValid(emailInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Invalid email address!",
      3
    );
    emailInput.focus();
    return false;
  }

  if (nameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your name!",
      3
    );
    nameInput.focus();
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
  if (passwordInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your password!",
      3
    );
    passwordInput.focus();
    return false;
  }
  if (!isPasswordValid(passwordInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Password that contain at least eight characters, including at least one number and includes both lowercase and uppercase letters and special characters, for example #, ?, !.",
      3
    );
    passwordInput.focus();
    return false;
  }
  return true;
};
const isAccountInfoChange = () => {
  let saveBtn = document.querySelector("#edit-account .btnAccountSave");
  if (
    nameAcc == document.querySelector("#edit-account .nameAccount").value &&
    emailAcc == document.querySelector("#edit-account .emailAccount").value &&
    phoneAcc == document.querySelector("#edit-account .phoneAccount").value &&
    roleAcc ==
      parseInt(document.querySelector("#edit-account .roleAccount").value) &&
    passwordAcc ==
      document.querySelector("#edit-account .passwordAccount").value &&
    addressAcc == document.querySelector("#edit-account .addressAccount").value
  ) {
    saveBtn.style.cursor = "no-drop";
    saveBtn.style.opacity = "0.5";
    isAccountDiff = false;
  } else {
    saveBtn.style.cursor = "pointer";
    saveBtn.style.opacity = "1";
    isAccountDiff = true;
  }
};
const createNewAccount = async () => {
  if (!(await checkInputCreateNewAccount())) return;
  let username = document.querySelector("#new-account .username").value;
  let name = document.querySelector("#new-account .name").value;
  let email = document.querySelector("#new-account .email").value;
  let phone = document.querySelector("#new-account .phoneNumber").value;
  let role = parseInt(document.querySelector("#new-account .role").value);
  let password = document.querySelector("#new-account .password").value;
  let address = document.querySelector("#new-account .address").value;
  $.ajax({
    url: "util/user.php",
    type: "POST",
    data: {
      username: username,
      name: name,
      email: email,
      phone: phone,
      role: role,
      password: password,
      address: address,
      action: "createNewAccount",
    },
    success: function (res) {
      if (res == "Success") {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Account successfully created",
          1
        );
      } else {
        customNotice("fa-sharp fa-light fa-circle-exclamation", res, 3);
      }
    },
  });
};
const checkInputCreateNewAccount = async () => {
  let usernameInput = document.querySelector("#new-account .username");
  let nameInput = document.querySelector("#new-account .name");
  let emailInput = document.querySelector("#new-account .email");
  let phoneInput = document.querySelector("#new-account .phoneNumber");
  let passwordInput = document.querySelector("#new-account .password");

  if (usernameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your user name!",
      3
    );
    usernameInput.focus();
    return false;
  }
  if (await isUsernameExist(usernameInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Username already exists!",
      3
    );
    usernameInput.focus();
    return false;
  }
  if (nameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your fullname!",
      3
    );
    nameInput.focus();
    return false;
  }
  if (emailInput.value != "" && !isEmailValid(emailInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Invalid email address!",
      3
    );
    emailInput.focus();
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
  if (nameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your name!",
      3
    );
    nameInput.focus();
    return false;
  }
  if (phoneInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Pleae, enter your phone number!",
      3
    );
    phoneInput.focus();
    return false;
  }
  if (passwordInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your password!",
      3
    );
    passwordInput.focus();
    return false;
  }
  if (!isPasswordValid(passwordInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Password that contain at least eight characters, including at least one number and includes both lowercase and uppercase letters and special characters, for example #, ?, !.",
      3
    );
    passwordInput.focus();
    return false;
  }
  return true;
};

module.exports = {
  setAccountInfo,
  updateAccount,
  checkInputUpdateAccount,
  isAccountInfoChange,
  createNewAccount,
  checkInputCreateNewAccount,
};