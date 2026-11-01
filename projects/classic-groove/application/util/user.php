<?php
session_start();
require("../util/dataProvider.php");
$dp = new DataProvider();
switch ($_SERVER["REQUEST_METHOD"]) {
  case 'GET':
    switch ($_GET['action']) {
      case 'isLogin':
        if (isset($_SESSION['userID'])) {
          echo 1;
        } else {
          echo 0;
        }
        break;
      case 'getRole':
        echo $_SESSION['role'];
        break;
    }
    break;
  case 'POST':
    switch ($_POST['action']) {
      case 'checkLogin':
        $username = $_POST['user'];
        $password = $_POST['pass'];
        $md5Pass = md5($password);
        $result = $dp->getUserByUsername($username);
        if ($result != null) {
          if (mysqli_num_rows($result) == 0) {
            echo "Account does not exist!";
          } else {
            $user = $result->fetch_assoc();
            if ($user['matKhau'] != $md5Pass) {
              echo "Wrong password!";
            } else {
              $sql = "Select hoTen from nguoidung where manguoidung ='" . $username . "'";
              $name = $dp->excuteQuery($sql)->fetch_assoc()["hoTen"];
              $_SESSION['userID'] = $user['username'];
              $_SESSION['userName'] = $name;
              $_SESSION['role'] = $user['vaiTro'];
              $_SESSION['permission'] = $dp->getPermissionByRoleID($user['vaiTro']);
              if ($user['vaiTro'] == 1) {
                echo "cus";
              } else {
                echo "emp";
              }
            }
          }
        }
        break;
      case 'checkUsernameExist':
        $username = $_POST['user'];
        $result = $dp->getUserByUsername($username);
        if (mysqli_num_rows($result) != 0) {
          echo true;
        } else {
          echo false;
        }
        break;
      case 'register':
        $name = $_POST['name'];
        $phone = $_POST['phone'];
        $username = $_POST['user'];
        $password = $_POST['pass'];
        $md5Pass = md5($password);
        $sql1 = "INSERT INTO nguoidung
        VALUES ('" . $username . "','" . $name . "','" . $phone . "', null, null, 'Hoạt động', 'KH')";
        $result1 = $dp->excuteQuery($sql1);
        $sql2 = "INSERT INTO taikhoan
        VALUES ('" . $username . "','" . (new Datetime())->format('Y-m-d') . "','Hoạt động','" . $md5Pass . "',1);";
        $result2 = $dp->excuteQuery($sql2);
        if ($result1 && $result2) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
      case 'createNewAccount':
        $username = $_POST['username'];
        $name = $_POST['name'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $role = $_POST['role'];
        $password = $_POST['password'];
        $address = $_POST['address'];
        $typeUser = ($role == 1) ? "KH" : "NV";
        $sql1 = "INSERT INTO nguoidung
        VALUES ('" . $username . "','" . $name . "','" . $phone . "', '" . $address . "',
                '" . $email . "', 'Hoạt động', '" . $typeUser . "')";
        $result1 = $dp->excuteQuery($sql1);
        $sql2 = "INSERT INTO taikhoan
        VALUES ('" . $username . "','" . (new Datetime())->format('Y-m-d') . "',
                'Hoạt động','" . $password . "'," . $role . ");";
        $result2 = $dp->excuteQuery($sql2);
        if ($result1 && $result2) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
    }
    break;
  case 'PUT':
    switch ($_GET['action']) {
      case 'updateUser':
        $fullname = $_GET['fullname'];
        $phone = $_GET['phone'];
        $password = $_GET['password'];
        $address = $_GET['address'];
        $email = $_GET['email'];
        $sql1 = "UPDATE nguoidung
                SET hoTen='" . $fullname . "',
                    SDT='" . $phone . "',
                    diaChi='" . $address . "',
                    email='" . $email . "'
                WHERE maNguoiDung='" . $_SESSION['userID'] . "'";
        $result1 = $dp->excuteQuery($sql1);
        $sql2 = "UPDATE taikhoan
                SET matKhau='" . $password . "'
                WHERE username='" . $_SESSION['userID'] . "'";
        $result2 = $dp->excuteQuery($sql2);
        if ($result1 && $result2) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
      case 'updateAccount':
        $username = $_GET['username'];
        $fullname = $_GET['fullname'];
        $phone = $_GET['phone'];
        $password = $_GET['password'];
        $md5Pass = md5($password);
        $address = $_GET['address'];
        $email = $_GET['email'];
        $role = $_GET['role'];
        $typeUser = ($role == 1) ? "KH" : "NV";
        $sql1 = "UPDATE nguoidung
                SET hoTen='" . $fullname . "',
                    SDT='" . $phone . "',
                    diaChi='" . $address . "',
                    email='" . $email . "',
                    loaiNguoiDung='" . $typeUser . "'
                WHERE maNguoiDung='" . $username . "'";
        $result1 = $dp->excuteQuery($sql1);
        $sql2 = "UPDATE taikhoan
                SET matKhau='" . $md5Pass . "',
                    vaiTro=" . $role .
          " WHERE username='" . $username . "'";
        $result2 = $dp->excuteQuery($sql2);
        if ($result1 && $result2) {
          echo "Success";
        } else {
          echo "Error";
        }
        break;
      case 'updatePassword':
        $oldPassword = $_GET['oldPassword'];
        $newPassword = $_GET['newPassword'];
        $confirmNewPassword = $_GET['confirmNewPassword'];
        $username = $_SESSION['userName'];
        $result = $dp->getUserByUsername($username);
        if ($result != null) {
          if (mysqli_num_rows($result) == 0) {
            echo 'Account does not exist!';
          } else {
            $user = $result->fetch_assoc();
            $password = $user['matKhau'];
            if ($password != md5($oldPassword)) {
              echo 'Old password is not correct!';
            } else {
              $md5Pass = md5($newPassword);
              $sql = "UPDATE taikhoan
                SET matKhau='" . $md5Pass .
                "' WHERE username='" . $username . "'";
              $result = $dp->excuteQuery($sql);
              if ($result) {
                echo "Success";
              } else {
                echo "Error";
              }
            }
          }
        }
        break;
    }
    break;
}