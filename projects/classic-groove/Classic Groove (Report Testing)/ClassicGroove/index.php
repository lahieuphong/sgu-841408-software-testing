<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel='shortcut icon' href='views/assets/img/LogoWeb.ico' />
  <link rel="stylesheet" href="views/assets/icons/all.css" />
  <link rel="stylesheet" href="views/style/user/header.css">
  <link rel="stylesheet" href="views/style/user/reset.css" />
  <link rel="stylesheet" href="views/style/user/home.css" />
  <link rel="stylesheet" href="views/style/user/footer.css" />
  <link rel="stylesheet" href="views/style/user/favorite.css" />
  <link rel="stylesheet" href="views/style/user/myAccount.css" />
  <link rel="stylesheet" href="views/style/user/mycart.css">
  <link rel="stylesheet" href="views/style/user/search.css" />
  <link rel="stylesheet" href="views/style/user/productDetails.css">
  <link rel="stylesheet" href="views/style/user/songControl.css">
  <link rel="stylesheet" href="views/style/user/login.css">
  <link rel="stylesheet" href="views/style/user/myAccount.css">
  <link rel="stylesheet" href="views/style/user/notice.css">
  <link rel="stylesheet" href="views/style/user/purchaseHistory.css">
  <link rel="stylesheet" href="views/style/admin/productManager.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <!-- <link rel="stylesheet" href="/assets/icons/scrollbar.css"> -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Dosis:wght@700;800&display=swap" rel="stylesheet">
  <!-- font-family: "Dosis", sans-serif; -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>


  <title>Classic-Groove</title>
</head>

<body>
  <div id="warrper">
    <header id="header">
      <?php include 'views/pages/user/header.php' ?>
    </header>
    <main>
      <div id="search">
        <?php include 'views/pages/user/search.php' ?>
      </div>
      <div id="content">

      </div>

      <div id="song-control">
        <?php include 'views/pages/user/songControl.php' ?>
      </div>
      <div id="notice">

      </div>
    </main>
  </div>
</body>
<!-- views -->
<script src="views/js/effectPages.js"></script>
<script src="views/js/songControl.js"></script>
<script src="views/js/loadPage.js"></script>
<script src="views/js/login.js"></script>
<script src="views/js/notice.js"></script>
<!-- controllers -->
<Script src="controllers/loginController.js"></Script>
<Script src="controllers/cartController.js"></Script>
<Script src="controllers/orderController.js"></Script>
<script src="controllers/favoriteController.js"></script>
<script src="controllers/userController.js"></script>

</html>