<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
if (
    isset($_POST['name']) && isset($_POST['category'])
    && isset($_POST['dateStart'])
    && isset($_POST['dateEnd'])
) {
    $order = searchOrder($_POST['name'], $_POST['category'], $_POST['dateStart'], $_POST['dateEnd']);
} else {
    $order = getAllOrder();
}
?>
<div id="orderManager">
    <div class="header">
        <h2><i class="fa-regular fa-list"></i> Order management</h2>
        <div class="search-bar">
            <div class="search-input">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" placeholder="Looking for somethings?" onchange="loadOrderByAjax()">
            </div>
            <div class="filter-input">
                <i class="fa-regular fa-filter"></i>
                <select name="" id="" onchange="loadOrderByAjax()">
                    <option value="All">All</option>
                    <option value="Pending">Pending</option>
                    <option value="Shipping">Shipping</option>
                    <option value="Delivered">Delivered</option>
                    <option value="Cancel">Cancel</option>
                </select>
            </div>
            <div class="date-begin">
                <input type="date" name="" id="" onchange="loadOrderByAjax()">
            </div>
            <div class="date-end">
                <input type="date" name="" id="" onchange="loadOrderByAjax()">
            </div>
        </div>
    </div>
    <div class="title-list">
        <div class="title-placeholder">
            <div class="title" style="padding-right: 10px;">No.</div>
            <div class="title" style="padding-right: 15px;">Order ID</div>
            <div class="title" style="padding-right: 15px;">Account ID</div>
            <div class="title" style="padding-right: 10px;">Date of order</div>
            <div class="title">Total price</div>
            <div class="title">Discount</div>
            <div class="title">Status</div>
            <div class="title"></div>
        </div>
    </div>
    <div class="list">
        <?php for ($i = 0; $i < count($order); $i++): ?>
            <div class="placeholder">
                <div class="info">
                    <div class="item">
                        <?= sprintf("%02d", $i + 1) ?>
                    </div>
                    <div class="item">
                        <?= $order[$i]['maHoaDon'] ?>
                    </div>
                    <div class="item">
                        <?= $order[$i]['khachHang'] ?>
                    </div>
                    <div class="item">
                        <?= date("d/m/Y", strtotime($order[$i]['thoiGianDat'])) ?>
                    </div>
                    <div class="item">
                        <?= "$" . $order[$i]['tongTien'] ?>
                    </div>
                    <div class="item">
                        <?php if ($order[$i]['khuyenMai'] == 0): ?>
                            <div class="item" style="color: var(--gr1)">No discount</div>
                        <?php else: ?>
                            <?= $order[$i]['khuyenMai'] . "%" ?>
                        <?php endif ?>
                    </div>
                    <div class="item">
                        <?= $order[$i]['trangThai'] ?>
                    </div>
                    <div class="item" onclick="loadModalBoxByAjax('detailOrder',<?= $order[$i]['maHoaDon'] ?>)"><i
                            class="fa-regular fa-circle-info"></i></div>
                </div>
            </div>
        <?php endfor ?>
    </div>
    <div id="modal-box"></div>
</div>
<?php
function getAllOrder()
{
    global $dp;
    $sql = "SELECT * FROM hoadon";
    $result = $dp->excuteQuery($sql);
    $order = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($order, $row);
        }
    }
    return $order;
}

function searchOrder($name, $category, $dateStart, $dateEnd)
{
    global $dp;
    $sql = "SELECT * FROM hoadon ";
    $f = false;

    if ($name != "" || $category != "All" || $dateStart != "" && $dateEnd != "") {
        $sql .= "WHERE ";
        if ($name != "") {
            $sql .= " (khachHang LIKE '%$name%' ";
            $sql .= " or maHoaDon LIKE '%$name%') ";

            $f = true;
        }
        if ($category != "All") {
            if ($f) {
                $sql .= "AND ";
            }
            $sql .= "trangThai = '$category' ";
            $f = true;
        }
        if ($dateStart != "" && $dateEnd != "") {
            if ($f) {
                $sql .= "AND ";
            }
            $sql .= "thoiGianDat >= '$dateStart' And thoiGianDat <= '$dateEnd'";
        }
    }
    $result = $dp->excuteQuery($sql);
    $order = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($order, $row);
        }
    }
    return $order;
}
?>