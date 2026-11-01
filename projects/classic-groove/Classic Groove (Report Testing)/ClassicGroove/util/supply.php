<?php
session_start();
require("../util/dataProvider.php");
$dp = new DataProvider();
switch ($_SERVER["REQUEST_METHOD"]) {
    case 'POST':
        switch ($_POST['action']) {
            case 'addNewSupply':
                $supplyID = $_POST['supplyID'];
                $importer = $_POST['supplyImport'];
                $distributor = $_POST['supplyDistributor'];
                $totalCost = $_POST['supplyTotalCost'];
                $albumList = json_decode($_POST['albumList']);
                $sql = "INSERT INTO phieunhap
                        VALUES (" . $supplyID . ",'" . (new Datetime())->format('Y-m-d') . "','" . $importer . "'," . $totalCost . "," . $distributor . ")";
                $result1 = $dp->excuteQuery($sql);
                $error = false;
                foreach ($albumList as $album) {
                    $sql = "INSERT INTO chitietphieunhap
                            VALUES (" . $album->{"albumID"} . "," . $supplyID . "," . $album->{"price"} . "," . $album->{"quantity"} . ")";
                    $result2 = $dp->excuteQuery($sql);
                    $sql = "UPDATE album SET soLuong=soluong + " . $album->{"quantity"} . " WHERE maAlbum=" . $album->{"albumID"};
                    $result3 = $dp->excuteQuery($sql);
                    if (!$result2 || !$result3) {
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
}