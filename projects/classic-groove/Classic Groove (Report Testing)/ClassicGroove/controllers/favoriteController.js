const addToFavorite = (albumID) => {
  $.ajax({
    url: "util/albums.php",
    type: "POST",
    data: { albumID: albumID, action: "favorite" },
    success: function (res) {
      if (res == "success") {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Added to your Favorite",
          1
        );
        loadProductDetailsByAjax(albumID);
      } else {
        customNotice("fa-sharp fa-light fa-circle-exclamation", res,3);
      }
    },
  });
};

const disLike = (albumID) => {
  $.ajax({
    url: "util/albums.php?albumID=" + albumID + "&action=dislike",
    type: "DELETE",
    success: function (res) {
      if (res == "success") {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Removed from your Favorite",1
        );
        loadProductDetailsByAjax(albumID);
      } else {
        customNotice("fa-sharp fa-light fa-circle-exclamation", res,3);
      }
    },
  });
};


module.exports = { 
  addToFavorite, 
  disLike, };