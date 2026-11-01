<?php
session_start();
require("../util/dataProvider.php");
$dp = new DataProvider();
switch ($_SERVER["REQUEST_METHOD"]) {
  case 'GET':
    switch ($_GET['action']) {
      case 'getOrderInfo':
        $orderID = $_GET['orderID'];
        $sql = "SELECT * FROM hoadon WHERE maHoaDon = " . $orderID;
        $result = $dp->excuteQuery($sql)->fetch_assoc();
        if ($result) {
          echo json_encode($result);
        } else {
          echo "Error";
        }
        break;
      case 'getAlbumsInOrder':
        $orderID = $_GET['orderID'];
        $sql = "SELECT * FROM chitiethoadon WHERE hoaDon = " . $orderID;
        $result = $dp->excuteQuery($sql);
        $albums = array();
        if ($result) {
          while ($row = $result->fetch_assoc()) {
            $albums[] = $row;
          }
          echo json_encode($albums);
        } else {
          echo "Error";
        }
        break;
    }
    break;

  case 'POST':
    switch ($_POST['action']) {
      case 'createOrder':
        $total = $_POST['total'];
        $address = $_POST['address'];
        $userID = $_SESSION['userID'];
        $albums = json_decode($_POST['albums']);
        $hoaDonID = $dp->getNewHoaDonId();
        $sql1 = "INSERT INTO hoadon
        VALUES (" . $hoaDonID . "," . $total . ",'" . (new Datetime())->format('Y-m-d') . "',
        'Pending','" . $userID . "',null,'" . $address . "')";
        $result1 = $dp->excuteQuery($sql1);
        $error = false;
        foreach ($albums as $album) {
          $sql = "INSERT INTO chitiethoadon
                  VALUES (" . $album->{"albumID"} . "," . $hoaDonID . "," . $album->{"quantity"} . ")";
          $result = $dp->excuteQuery($sql);
          if (!$result) {
            $error = true;
          }
        }
        if ($result1 && !$error) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
    }
    break;
  case 'PUT':
    switch ($_GET['action']) {
      case 'cancelOrder':
        $orderID = $_GET['orderID'];
        $sql = "UPDATE hoadon SET trangThai = 'Cancel' WHERE maHoaDon = " . $orderID;
        $result = $dp->excuteQuery($sql);
        if ($result) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
      case 'updateOrder':
        $orderID = $_GET['orderID'];
        $status = $_GET['status'];
        $f = true;
        if ($status == "Shipping") {
          $sql = "SELECT cthd.album, cthd.soLuong
          FROM chitiethoadon cthd join hoadon hd on cthd.hoaDon = hd.maHoaDon
          WHERE hd.maHoaDon = $orderID";
          $result = $dp->excuteQuery($sql);
          $albums = array();
          if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
              array_push($albums, $row);
            }
          }
          foreach ($albums as $album) {
            $sql = "SELECT soLuong FROM album where maAlbum=" . $album['album'];
            $result = $dp->excuteQuery($sql);
            $sl = $result->fetch_assoc()['soLuong'];
            if ($sl < $album['soLuong']) {
              $f = false;
              break;
            }
          }
        }
        if (!$f) {
          echo "Not enough product quantity";
          break;
        }


        $sql = "UPDATE hoadon SET trangThai = '" . $status . "' WHERE maHoaDon = " . $orderID;
        $result1 = $dp->excuteQuery($sql);
        $error = false;
        if ($status == "Shipping") {
          $sql = "SELECT cthd.album, cthd.soLuong
                  FROM chitiethoadon cthd join hoadon hd on cthd.hoaDon = hd.maHoaDon
                  WHERE hd.maHoaDon = $orderID";
          $result = $dp->excuteQuery($sql);
          $albums = array();
          if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
              array_push($albums, $row);
            }
          }
          foreach ($albums as $album) {
            $sql = "UPDATE album SET soLuong = soLuong - " . $album['soLuong'] . " WHERE maAlbum = " . $album['album'];
            $result = $dp->excuteQuery($sql);
            if (!$result) {
              $error = true;
            }
          }
        }
        if ($result1 && !$error) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
    }
    break;
}