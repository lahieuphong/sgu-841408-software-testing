const order = async () => {
  if (!checkMyCart()) return;
  await createOrder();
  await deleteFromOrder();
  document.querySelector("#orderSuccess").style.display = "flex";
};

const getTotal = () => {
  let totalInput = document.querySelector(".total-final");
  let total = parseFloat(totalInput.innerHTML.substring(1));
  return total;
};

const createOrder = async () => {
  let albums = getAlbums();
  console.log(albums);
  let total = getTotal();
  let address = document.querySelector("#mycart #checkout-address").value;
  await $.ajax({
    url: "util/order.php",
    type: "POST",
    data: {
      address: address,
      total: total,
      albums: albums,
      action: "createOrder",
    },
    success: function (res) {
      if (res != "Success") alert(res);
    },
  });
};
const getAlbums = () => {
  let listAlbum = [];
  let albums = document.querySelectorAll(
    "#mycart .check-button input[type='checkbox']:checked"
  );
  for (let album of albums) {
    let quantity = album
      .closest(".product-placeholder")
      .querySelector("input.quantity-info").value;
    let albumID = album.value;
    listAlbum.push({ quantity: quantity, albumID: albumID });
  }
  console.log(listAlbum);
  return JSON.stringify(listAlbum);
};
const checkMyCart = () => {
  let albums = document.querySelectorAll(
    "#mycart .check-button input[type='checkbox']:checked"
  );
  let address = document.querySelector("#mycart #checkout-address");
  if (albums.length == 0) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, select the album!",
      3
    );
    return false;
  }
  if (address.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter your address!",
      3
    );
    address.focus();
    return false;
  }
  return true;
};

const deleteFromOrder = async () => {
  let albums = document.querySelectorAll(
    "#mycart .check-button input[type='checkbox']:checked"
  );
  for (let album of albums) {
    await deleteByAlbumID(parseInt(album.value));
    album.closest(".product-placeholder").remove();
  }
};
const cancelOrder = (orderID) => {
  $.ajax({
    url: "util/order.php?orderID=" + orderID + "&action=cancelOrder",
    type: "PUT",
    success: function (res) {
      if (res != "Success") alert(res);
      else {
        customNotice("fa-solid fa-cart-circle-plus", "Cancel your Order", 1);
        loadPageByAjax("Account");
      }
    },
  });
};

const getOrderInfo = (orderID) => {
  return $.ajax({
    url: "util/order.php?orderID=" + orderID + "&action=getOrderInfo",
    type: "GET",
  });
};

const getAlbumsInOrder = (orderID) => {
  return $.ajax({
    url: "util/order.php?orderID=" + orderID + "&action=getAlbumsInOrder",
    type: "GET",
  });
};

module.exports = {
  order,
  getTotal,
  createOrder,
  getAlbums,
  checkMyCart,
  deleteFromOrder,
  cancelOrder,
  getOrderInfo,
  getAlbumsInOrder,
};