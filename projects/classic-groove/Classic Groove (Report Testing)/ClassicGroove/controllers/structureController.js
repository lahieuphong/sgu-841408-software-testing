const updateSlide = (slideID) => {
  if (!checkAddSlide()) return;
  let imgInput = document.querySelector(".imgSlide");
  let nameInput = document.querySelector(".nameSlide");
  let linkToInput = document.querySelector(".linkToSlide");
  $.ajax({
    url:
      "util/structure.php?slideID=" +
      slideID +
      "&slideName=" +
      nameInput.value +
      "&slideImg=" +
      imgInput.src.split("/").pop() +
      "&slideLinkTo=" +
      parseInt(linkToInput.value) +
      "&action=updateSlide",
    type: "PUT",

    success: function (res) {
      if (res != "Success") {
        console.log(res);
      } else
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Update successfully!",
          1
        );
      loadPageByAjax("structureManager");
    },
  });
};
const uploadImgSlide = () => {
  let fileInput = document.createElement("input");
  fileInput.type = "file";
  fileInput.click();
  fileInput.onchange = () => {
    let file_data = fileInput.files[0];
    let form_data = new FormData();
    if (!file_data.type.startsWith("image/")) {
      customNotice(
        "fa-sharp fa-light fa-circle-exclamation",
        "Please upload an image!",
        3
      );
      return;
    }
    form_data.append("file", file_data);
    form_data.append("target_directory", "../data/slideShow/");
    //Ajax to send file to upload
    $.ajax({
      url: "util/upload.php",
      type: "POST",
      data: form_data,
      dataType: "script",
      cache: false,
      contentType: false,
      processData: false,
      success: function (res) {
        if (res) {
          document.querySelector(".top .img-placeholder img").src =
            "data/slideShow/" + fileInput.files[0].name;
          customNotice(
            "fa-sharp fa-light fa-circle-check",
            "Uploaded successfully",
            1
          );
        } else
          customNotice(
            "fa-sharp fa-light fa-circle-exclamation",
            "Upload failed",
            3
          );
      },
    });
  };
};

const checkAddSlide = () => {
  let imgInput = document.querySelector(".imgSlide");
  let nameInput = document.querySelector(".nameSlide");
  let linkToInput = document.querySelector(".linkToSlide");
  if (imgInput.src.split("/").pop() == "default.jfif") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please upload an image!",
      3
    );
    return false;
  }
  if (nameInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please enter a name!",
      3
    );
    return false;
  }
  if (linkToInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please enter a link!",
      3
    );
    return false;
  }
  if (isNaN(linkToInput.value)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please enter a id album in Linked To!",
      3
    );
    return false;
  }

  return true;
};
const checkAlbumExist = async () => {
  let linkToInput = document.querySelector(".linkToSlide");
  let allAlbum = JSON.parse(await getInfoAlbum());
  let exist = false;
  for (let i = 0; i < allAlbum.length; i++) {
    if (allAlbum[i].maAlbum == parseInt(linkToInput.value)) exist = true;
  }
  if (!exist) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please enter a link exist!",
      3
    );
    return false;
  }
  return true;
};
const addSlide = async () => {
  if (!checkAddSlide()) return;
  if (!(await checkAlbumExist())) return;
  let imgInput = document.querySelector(".imgSlide");
  let nameInput = document.querySelector(".nameSlide");
  let linkToInput = document.querySelector(".linkToSlide");
  $.ajax({
    url: "util/structure.php",
    type: "POST",
    data: {
      slideName: nameInput.value,
      slideImg: imgInput.src.split("/").pop(),
      slideLinkTo: parseInt(linkToInput.value),
      action: "addSlide",
    },
    success: function (res) {
      if (res != "Success") {
        console.log(res);
      } else
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Added successfully!",
          1
        );
      loadPageByAjax("Structure");
    },
  });
};

const deleteSlide = (slideID) => {
  let choice = confirm("Are you sure to delete this slide?");
  if (!choice) return;
  $.ajax({
    url: "util/structure.php?slideID=" + slideID + "&action=deleteSlide",
    type: "DELETE",
    success: function (res) {
      if (res != "Success") {
        console.log(res);
      } else
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Deleted successfully!",
          1
        );
      loadPageByAjax("Structure");
    },
  });
};

module.exports = {
  updateSlide,
  uploadImgSlide,
  checkAddSlide,
  checkAlbumExist,
  addSlide,
  deleteSlide,
};