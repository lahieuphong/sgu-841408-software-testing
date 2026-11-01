<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel='shortcut icon' href='views/assets/img/LogoWeb.ico' />
  <link rel="stylesheet" href="views/assets/icons/all.css" />
  <link rel="stylesheet" href="views/style/admin/productManager.css">
  <link rel="stylesheet" href="views/style/admin/reset.css">
  <link rel="stylesheet" href="views/style/admin/header.css">
  <link rel="stylesheet" href="views/style/user/notice.css">



  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="views/assets/icons/scrollbar.css">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <!-- Admin page -->
  <link rel="stylesheet" href="views/style/admin/accountManager.css">
  <link rel="stylesheet" href="views/style/admin/orderManager.css">
  <link rel="stylesheet" href="views/style/admin/changeProduct.css">
  <link rel="stylesheet" href="views/style/admin/search.css">
  <link rel="stylesheet" href="views/style/admin/structureManager.css">
  <link rel="stylesheet" href="views/style/admin/distributor.css">
  <link rel="stylesheet" href="views/style/admin/supplyRecord.css">
  <link rel="stylesheet" href="views/style/admin/roleManager.css">
  <link rel="stylesheet" href="views/style/admin/statistic.css">
  <link href="https://fonts.googleapis.com/css2?family=Dosis:wght@700;800&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://code.highcharts.com/highcharts.js"></script>
  <script src="https://code.highcharts.com/modules/exporting.js"></script>
  <script src="https://code.highcharts.com/modules/export-data.js"></script>
  <script src="https://code.highcharts.com/modules/accessibility.js"></script>


  <title>Administrator</title>
</head>

<body>
  <div id="warrper">
    <header id="header">
      <?php include 'views/pages/admin/header.php' ?>
    </header>
    <main>
      <div id="content">
      </div>
      <div id="notice">

      </div>
  </div>
  </main>
</body>
<!-- views -->
<script src="views/js/effectPages.js"></script>
<script src="views/js/songControl.js"></script>
<script src="views/js/loadPage.js"></script>
<script src="views/js/login.js"></script>
<script src="views/js/modalBox.js"></script>
<script src="views/js/notice.js"></script>

<!-- controllers -->
<script src="controllers/albumController.js"></script>
<script src="controllers/orderController.js"></script>
<script src="controllers/loginController.js"></script>
<script src="controllers/userController.js"></script>
<script src="controllers/managerAccountController.js"></script>
<script src="controllers/roleController.js"></script>
<script src="controllers/managerOrderController.js"></script>
<script src="controllers/supplyController.js"></script>
<script src="controllers/structureController.js"></script>
<script src="controllers/statisticController.js"></script>

</html>