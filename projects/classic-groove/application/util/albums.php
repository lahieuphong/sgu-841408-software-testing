<?php
session_start();
require("../util/dataProvider.php");
$dp = new DataProvider();
switch ($_SERVER["REQUEST_METHOD"]) {
    case 'GET':
        switch ($_GET['action']) {
            case 'getQuantity':
                $albumID = $_GET['albumID'];
                $sql = "SELECT soLuong FROM album WHERE maAlbum = " . $albumID;
                $result = $dp->excuteQuery($sql);
                if ($result->num_rows > 0) {
                    $row = $result->fetch_assoc();
                    echo $row['soLuong'];
                } else {
                    echo "error";
                }
                break;
            case 'getInfoAlbum':
                $sql = "SELECT * FROM album";
                $result = $dp->excuteQuery($sql);
                $album = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($album, $row);
                    }
                }
                if ($result != null) {
                    echo json_encode($album);
                } else {
                    echo "error";
                }
                break;
            case 'getAllSongs':
                $sql = "SELECT * FROM baihat";
                $result = $dp->excuteQuery($sql);
                $songs = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($songs, $row);
                    }
                    echo json_encode($songs);
                }
                break;
            case 'getNewIDSong':
                $sql = "SELECT maBaiHat FROM baihat ORDER BY maBaiHat DESC LIMIT 1";
                $result = $dp->excuteQuery($sql)->fetch_assoc();
                if ($result != null) {
                    echo $result['maBaiHat'] + 1;
                } else {
                    echo "error";
                }
                break;
            case 'getSongByAlbum':
                $albumID = $_GET['albumID'];
                $sql = "SELECT * FROM baihat_album
                        JOIN baihat on baihat_album.BaiHat_maBaiHat = baihat.maBaiHat
                        WHERE baihat_album.Album_maAlbum = " . $albumID;
                $result = $dp->excuteQuery($sql);
                $songs = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($songs, $row);
                    }
                }
                echo json_encode($songs);
                break;
            case 'getAllAlbum':
                $sql = "SELECT * FROM album";
                $result = $dp->excuteQuery($sql);
                $album = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($album, $row);
                    }
                }
                echo json_encode($album);
                break;
        }
        break;
    case 'POST':
        switch ($_POST['action']) {
            case 'favorite':
                if (!isset($_SESSION['userID'])) {
                    echo "You are not logged in!";
                    break;
                }
                $userID = $_SESSION['userID'];
                $albumID = $_POST['albumID'];
                $sql = "INSERT INTO yeuthich
                    VALUES ( " . $albumID . " ,'" . $userID . "')";
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo "success";
                } else {
                    echo "error";
                }
                break;
            case 'addSongInAlbum':
                $albumID = $_POST['albumID'];
                $songID = $_POST['songID'];
                $songName = $_POST['songName'];
                $linkFile = $_POST['linkFile'];
                $sql1 = "INSERT INTO baihat
                        VALUES ( " . $songID . " ,'" . $songName . "','" . $linkFile . "')";
                $result1 = $dp->excuteQuery($sql1);
                $sql2 = "INSERT INTO baihat_album
                        VALUES ( " . $songID . " ," . $albumID . ")";
                $result2 = $dp->excuteQuery($sql2);
                break;
            case 'addSongExistInAlbum':
                $albumID = $_POST['albumID'];
                $songID = $_POST['songID'];
                $sql = "INSERT INTO baihat_album
                            VALUES ( " . $songID . " ," . $albumID . ")";
                $result = $dp->excuteQuery($sql);
                break;
            case 'addNewAlbum':
                $albumID = $_POST['albumID'];
                $albumName = $_POST['albumName'];
                $albumKind = $_POST['albumKind'];
                $albumArtist = $_POST['albumArtist'];
                $ablumPrice = $_POST['albumPrice'];
                $albumImage = $_POST['albumImage'];
                $albumDescribe = $_POST['albumDescribe'];
                $sql = "INSERT INTO album
                        VALUES(" . $albumID . ",'" . $albumName . "'," . $ablumPrice . ",'" . $albumDescribe . "','" . $albumImage . "','" . $albumArtist . "',1,0," . $albumKind . ")";
                echo $sql;
                $result = $dp->excuteQuery($sql);
                break;
        }
        break;
    case 'PUT':
        switch ($_GET['action']) {
            case 'updateSongInAlbum':
                $songID = $_GET['songID'];
                $songName = $_GET['songName'];
                $linkFile = $_GET['linkFile'];
                $sql = "UPDATE baihat
                        SET tenBaiHat = '" . $songName . "',
                            linkFile = '" . $linkFile . "'
                        WHERE maBaiHat = " . $songID;
                $result = $dp->excuteQuery($sql);
                break;
            case 'updateAlbumInfo':
                $albumID = $_GET['albumID'];
                $albumName = $_GET['albumName'];
                $albumKind = $_GET['albumKind'];
                $albumArtist = $_GET['albumArtist'];
                $ablumPrice = $_GET['albumPrice'];
                $albumImage = $_GET['albumImage'];
                $albumDescribe = $_GET['albumDescribe'];
                $sql = "UPDATE album
                        SET tenAlbum = '" . $albumName . "',
                            theLoai = " . $albumKind . ",
                            tacGia = '" . $albumArtist . "',
                            gia = " . $ablumPrice . ",
                            hinh = '" . $albumImage . "',
                            moTa = '" . $albumDescribe . "'
                        WHERE maAlbum = " . $albumID;
                $result = $dp->excuteQuery($sql);
                break;
            case 'deleteAlbum':
                $albumID = $_GET['albumID'];
                $sql = "Update album
                        SET TrangThai = 0
                        WHERE maAlbum = " . $albumID;
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo "Success";
                } else {
                    echo "error";
                }
                break;
        }
        break;
    case 'DELETE':
        switch ($_GET['action']) {
            case 'dislike':
                $userID = $_SESSION['userID'];
                $albumID = $_GET['albumID'];
                $sql = "DELETE FROM yeuthich
                    WHERE nguoiDung = '" . $userID . "' AND album = " . $albumID . "";
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo "success";
                } else {
                    echo "error";
                }
                break;
            case 'deleteSongInAlbum':
                $albumID = $_GET['albumID'];
                $songID = $_GET['songID'];
                $sql = "DELETE FROM baihat_album
                        WHERE BaiHat_maBaiHat = " . $songID . " AND Album_maAlbum = " . $albumID;
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo "success";
                } else {
                    echo "error";
                }
                break;
        }
        break;
}