<?php
require("../../util/dataProvider.php");
$dp = new DataProvider();
$albumID = $_POST["albumID"];
$sql = "SELECT * FROM baihat_album join baihat on baihat_album.BaiHat_maBaiHat = baihat.maBaiHat
where Album_maAlbum = " . $albumID;
$result = $dp->excuteQuery($sql);
$songs = array();
if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    array_push($songs, $row);
  }
}
echo json_encode($songs);
?>