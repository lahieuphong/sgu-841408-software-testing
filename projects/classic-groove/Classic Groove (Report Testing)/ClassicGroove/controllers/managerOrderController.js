let orderStatus = null;
let orderID = null;
let isOrderDiff = false;
const setOrderInfo = () => {
  orderStatus = document.querySelector("#edit-order .orderStatus").value;
  orderID = document.querySelector("#edit-order .orderID").value;
};
const isOrderInfoChange = () => {
  let saveBtn = document.querySelector("#edit-order .btnOrderSave");
  if (orderStatus == document.querySelector("#edit-order .orderStatus").value) {
    saveBtn.style.cursor = "no-drop";
    saveBtn.style.opacity = "0.5";
    isOrderDiff = false;
  } else {
    saveBtn.style.cursor = "pointer";
    saveBtn.style.opacity = "1";
    isOrderDiff = true;
  }
};
const updateOrder = () => {
  if (!isOrderDiff) return;
  setOrderInfo();
  $.ajax({
    url:
      "util/order.php?status=" +
      orderStatus +
      "&orderID=" +
      orderID +
      "&action=updateOrder",
    type: "PUT",
    success: function (res) {
      if (res == "Not enough product quantity") {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Not enough product quantity!",
          3
        );
      } else if (res != "Success") alert(res);
      else {
        customNotice(
          "fa-sharp fa-light fa-circle-check",
          "Update successfully!",
          1
        );
        loadPageByAjax("Order");
      }
    },
  });
};

module.exports = {
  setOrderInfo,
  isOrderInfoChange,
  updateOrder,
};