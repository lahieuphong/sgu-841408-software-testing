<?php
class DataProvider
{
  public static function excuteQuery($sql)
  {
    include('connect.php');
    if (!$connection = mysqli_connect($servername, $username, $password, $dbname)) {
      die("couldn't connect to localhost");
    }
    if (!(mysqli_select_db($connection, $dbname))) {
      echo "Khong the ket noi den database";
    }
    if (!(mysqli_query($connection, "set names 'utf8'"))) {
      echo "Khong the set utf8";
    }
    if (!($result = mysqli_query($connection, $sql))) {
      echo "Khong the thuc thi cau truy van";
    }
    if (!(mysqli_close($connection))) {
      echo "Khong the ket noi 4";
    }
    return $result;
  }
  public static function getUserByUsername($username)
  {
    $sql = "select * from taikhoan join nguoiDung on taikhoan.username=nguoiDung.maNguoiDung
    where username='" . $username . "'";
    return self::excuteQuery($sql);
  }
  public static function getNewHoaDonId()
  {
    $sql = "SELECT MAX(maHoaDon) FROM hoadon";
    $result = self::excuteQuery($sql);
    if (mysqli_num_rows($result) != 0) {
      return self::excuteQuery($sql)->fetch_assoc()['MAX(maHoaDon)'] + 1;
    }
    return 1;
  }
  public static function getAlbumInCart($albumID, $userID)
  {
    $sql = "SELECT * FROM giohang where maKhachHang = '" . $userID . "' and maAlbum = " . $albumID;
    return self::excuteQuery($sql);
  }
  public static function isFavorite($albumID, $userID)
  {
    $sql = "SELECT * FROM yeuthich where album = " . $albumID . " and nguoiDung ='" . $userID . "'";
    $result = self::excuteQuery($sql);
    if ($result->num_rows > 0) {
      return true;
    }
    return false;
  }
  public static function getPermissionByRoleID($roleID)
  {
    $sql = "SELECT Quyen_maCTQ FROM vaitro_quyen where VaiTro_maVaiTro = " . $roleID;
    $result = Self::excuteQuery($sql);
    $permissions = array();
    while ($row = $result->fetch_assoc()) {
      array_push($permissions, $row['Quyen_maCTQ']);
    }
    return $permissions;
  }
}