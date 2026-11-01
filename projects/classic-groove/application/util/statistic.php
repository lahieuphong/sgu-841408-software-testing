<?php
require("../util/dataProvider.php");
$dp = new DataProvider();
switch ($_SERVER["REQUEST_METHOD"]) {
    case 'GET':
        switch ($_GET['action']) {
            case 'getSales':
                $dateStart = $_GET['dateStart'];
                $dateEnd = $_GET['dateEnd'];
                $typeDate = $_GET['typeDate'];
                switch ($typeDate) {
                    case 1: //year
                        $dateStart .= "-01-01";
                        $dateEnd .= "-12-31";
                        $select = "DATE_FORMAT(thoiGianDat, '%Y')";
                        $as = "y";
                        break;
                    case '2': //month
                        $dateStart .= "-01";
                        $dateEnd = date('Y-m-t', strtotime($dateEnd));
                        $select = "DATE_FORMAT(thoiGianDat, '%Y-%m')";
                        $as = "m";
                        break;
                    case '3': //week
                        $dateStart = date('Y-m-d', strtotime($dateStart . '-1'));
                        $dateEnd = date('Y-m-d', strtotime($dateEnd . '-7'));
                        $select = "DATE_FORMAT(thoiGianDat, '%X-%V')";
                        $as = "w";
                        break;
                    case '4': //date
                        $select = "thoiGianDat";
                        $as = "d";
                        break;
                }
                $sql = "SELECT $select AS $as, SUM(tongTien) AS total
                        FROM hoadon WHERE trangThai = 'Delivered'
                            AND thoiGianDat >= '$dateStart'
                            AND thoiGianDat <= '$dateEnd'
                        GROUP BY $select
                        ORDER BY $as ASC";
                $result = $dp->excuteQuery($sql);
                $data = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($data, $row);
                    }
                }
                echo json_encode($data);
                break;
            case 'getNumberOfKindProductsSold':
                $dateStart = $_GET['dateStart'];
                $dateEnd = $_GET['dateEnd'];
                $sql = "SELECT tl.tenLoai AS ten, IFNULL(SUM(cthd.SoLuong), 0) AS soLuong
                        FROM theLoai tl
                        LEFT JOIN (
                            SELECT a.theLoai, SUM(cthd.SoLuong) AS SoLuong
                            FROM album a
                            LEFT JOIN chitiethoadon cthd ON cthd.album = a.maAlbum
                            LEFT JOIN hoadon hd ON hd.maHoaDon=cthd.hoaDon
                            WHERE hd.trangThai = 'Delivered'
                                AND hd.thoiGianDat >= '$dateStart'
                                AND hd.thoiGianDat <= '$dateEnd'
                            GROUP BY a.theLoai
                        ) AS cthd ON tl.maLoai = cthd.theLoai
                        GROUP BY tl.maLoai";
                $result = $dp->excuteQuery($sql);
                $data = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($data, $row);
                    }
                }
                echo json_encode($data);
                break;
            case 'getNumberOfProductsSold':
                $dateStart = $_GET['dateStart'];
                $dateEnd = $_GET['dateEnd'];
                $sql = "SELECT CONCAT(a.maAlbum,\"-\", a.tenAlbum) as ten, SUM(cthd.soLuong) as soLuong
                        FROM album a JOIN chitiethoadon cthd on a.maAlbum = cthd.album
                            JOIN hoadon hd on cthd.hoaDon = hd.maHoaDon
                        WHERE hd.trangThai = 'Delivered'
                            AND hd.thoiGianDat >= '$dateStart'
                            AND hd.thoiGianDat <= '$dateEnd'
                        GROUP BY a.maAlbum";
                $result = $dp->excuteQuery($sql);
                $data = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($data, $row);
                    }
                }
                echo json_encode($data);
                break;
            case 'getTopKindProducts':
                $dateStart = $_GET['dateStart'];
                $dateEnd = $_GET['dateEnd'];
                $limit = $_GET['limit'];
                $sql = "SELECT tl.tenLoai as ten, SUM(cthd.SoLuong) AS soLuong
                        FROM theLoai tl join album a on tl.maLoai = a.theLoai
                            join chitiethoadon cthd on a.maAlbum = cthd.album
                            join hoadon hd on cthd.hoaDon = hd.maHoaDon
                        WHERE hd.trangThai = 'Delivered'
                            AND hd.thoiGianDat >= '$dateStart'
                            AND hd.thoiGianDat <= '$dateEnd'
                        GROUP BY tl.maLoai
                        ORDER BY soLuong DESC
                        LIMIT $limit";
                $result = $dp->excuteQuery($sql);
                $data = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($data, $row);
                    }
                }
                echo json_encode($data);
                break;
            case 'getTopProducts':
                $dateStart = $_GET['dateStart'];
                $dateEnd = $_GET['dateEnd'];
                $limit = $_GET['limit'];
                $sql = "SELECT CONCAT(a.maAlbum,\"-\", a.tenAlbum) as ten, SUM(cthd.soLuong) as soLuong
                        FROM album a JOIN chitiethoadon cthd on a.maAlbum = cthd.album
                            JOIN hoadon hd on cthd.hoaDon = hd.maHoaDon
                        WHERE hd.trangThai = 'Delivered'
                            AND hd.thoiGianDat >= '$dateStart'
                            AND hd.thoiGianDat <= '$dateEnd'
                        GROUP BY a.maAlbum
                        ORDER BY soLuong DESC
                        LIMIT $limit";
                $result = $dp->excuteQuery($sql);
                $data = array();
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        array_push($data, $row);
                    }
                }
                echo json_encode($data);
        }
        break;
}