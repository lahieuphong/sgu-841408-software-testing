<?php
if (isset($_POST["page"])) {
  switch ($_POST["page"]) {
    case "home":
      include("home.php");
      break;
    case "favorites":
      include("favorites.php");
      break;
    case "myCart":
      include("myCart.php");
      break;
    case "myAccount":
      include("myAccount.php");
      break;
    case "login":
      include("login.php");
      break;
    case "footer":
      include("footer.php");
      break;
    case "Statistic":
      include("../admin/statistic.php");
      break;
    case "Album":
      include("../admin/productManager.php");
      break;
    case "Order":
      include("../admin/orderManager.php");
      break;
    case "Account":
      include("../admin/accountManager.php");
      break;
    case "distributor":
      include("../admin/distributor.php");
      break;
    case "Structure":
      include("../admin/structureManager.php");
      break;
    case "Supply":
      include("../admin/supplyRecord.php");
      break;
    case "Permission":
      include("../admin/roleManager.php");
      break;
    default:
      echo `<h1>Page not found 404</h1>`;
  }
} else {
  // include("pages/user/home.php");
  // include("pages/user/login.php");
  // include("pages/admin/productManager.php");
  // include("pages/user/purchaseHistory.php");
}
?>