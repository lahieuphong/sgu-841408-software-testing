<?php
session_start();
require("../util/dataProvider.php");
$dp = new DataProvider();
switch ($_SERVER["REQUEST_METHOD"]) {
    case 'POST':
        switch ($_POST["action"]) {
            case 'addSlide':
                $slideName = $_POST["slideName"];
                $slideImg = $_POST["slideImg"];
                $slideTo = $_POST["slideLinkTo"];
                $sql = "INSERT INTO slideshow VALUES ('','$slideName', $slideTo, '$slideImg')";
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo 'Success';
                } else {
                    echo 'error';
                }
                break;
        }
        break;
    case 'PUT':
        switch ($_GET["action"]) {
            case 'updateSlide':
                $slideID = $_GET["slideID"];
                $slideName = $_GET["slideName"];
                $slideImg = $_GET["slideImg"];
                $slideTo = $_GET["slideLinkTo"];
                $sql = "UPDATE slideshow SET tenHinh = '$slideName', linkHinh = '$slideImg', linkTo = $slideTo WHERE maHinh = $slideID";
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo 'Success';
                } else {
                    echo 'error';
                }
                break;
        }
        break;
    case 'DELETE':
        switch ($_GET["action"]) {
            case 'deleteSlide':
                $slideID = $_GET["slideID"];
                $sql = "DELETE FROM slideshow WHERE maHinh = $slideID";
                $result = $dp->excuteQuery($sql);
                if ($result) {
                    echo 'Success';
                } else {
                    echo 'error';
                }
                break;
        }
        break;
}