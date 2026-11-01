const updateRole = async (roleID) => {
  if (!checkAddNewRole()) return;
  let listPermissionInput = document.querySelectorAll(
    ".role-placeholder .checkbox-placeholder input"
  );
  let listPermission = [];
  listPermissionInput.forEach((item) => {
    if (item.checked) listPermission.push(parseInt(item.value));
  });
  let roleName = document.querySelector(".info-role input").value.trim();
  let roleDescription = document
    .querySelector(".info-role textarea")
    .value.trim();
  $.ajax({
    url: "util/role.php",
    type: "POST",
    data: {
      roleID: roleID,
      roleName: roleName,
      roleDescription: roleDescription,
      listPermission: listPermission,
      action: "updateRole",
    },
    success: function (res) {
      if (res != "Success") console.log(res);
      else
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Update role successfully!",
          1
        );
      loadPageByAjax("Permission");
      loadModalBoxByAjax("roleManager", roleID);
    },
  });
};
const checkAddNewRole = () => {
  let roleNameInput = document.querySelector(".info-role input");
  if (roleNameInput.value.trim() == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Role name must not be empty!",
      3
    );
    return false;
  }
  return true;
};

const addNewRole = (roleID) => {
  if (!checkAddNewRole()) return;
  let listPermissionInput = document.querySelectorAll(
    ".role-placeholder .checkbox-placeholder input"
  );
  let listPermission = [];
  listPermissionInput.forEach((item) => {
    if (item.checked) listPermission.push(parseInt(item.value));
  });
  let roleName = document.querySelector(".info-role input").value.trim();
  let roleDescription = document
    .querySelector(".info-role textarea")
    .value.trim();
  $.ajax({
    url: "util/role.php",
    type: "POST",
    data: {
      roleID: roleID,
      roleName: roleName,
      roleDescription: roleDescription,
      listPermission: listPermission,
      action: "addNewRole",
    },
    success: function (res) {
      if (res != "Success") console.log(res);
      else
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Add new role successfully!",
          1
        );
      loadPageByAjax("Permission");
    },
  });
};

const deleteRole = (roleID) => {
  let choice = confirm("Are you sure to delete this role?");
  if (!choice) return;
  $.ajax({
    url: "util/role.php?roleID=" + roleID + "&action=deleteRole",
    type: "DELETE",
    success: function (res) {
      if (res != "Success") console.log(res);
      else
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Delete role successfully!",
          1
        );
      loadPageByAjax("Permission");
    },
  });
};

module.exports = {
  updateRole,
  checkAddNewRole,
  addNewRole,
  addNewRole,
};