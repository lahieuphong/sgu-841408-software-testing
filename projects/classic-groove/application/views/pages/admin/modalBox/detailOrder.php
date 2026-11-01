<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$orderID = $_POST['id'];
$order = getOrder($orderID);
$detailOrder = getDetailOrder($orderID);
?>
<div class="modal-placeholder" id="detail-order">
    <div class="modal-box">
        <div class="modal-header">
            <h1><i class="fa-regular fa-square-kanban fa-rotate-270"></i>Order details</h1>
        </div>
        <div class="modal-left">
            <div class="modal-info">
                <div class="modal-item">
                    <div class="item-header">Order id</div>
                    <div class="item-input"><input type="text" class="orderId" value="<?= $order['maHoaDon'] ?>"
                            disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Account id</div>
                    <div class="item-input"><input type="text" class="orderAccount" value="<?= $order['khachHang'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Date of order</div>
                    <div class="item-input"><input type="text" class="orderDate"
                            value="<?= date("d/m/Y", strtotime($order['thoiGianDat'])) ?>" disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Total price</div>
                    <div class="item-input"><input type="text" class="orderPrice" value="<?= $order['tongTien'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Discount</div>
                    <?php
                    if ($order['khuyenMai'] == 0) {
                        $km = "No discount";
                    } else {
                        $km = $order['khuyenMai'] . "%";
                    }
                    ?>
                    <div class="item-input"><input type="text" class="orderDiscount" value="<?= $km ?>" disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Status</div>
                    <div class="item-input">
                        <select name="" id="" class="orderStatus" disabled>
                            <option value="<?= $order['trangThai'] ?>"><?= $order['trangThai'] ?></option>
                        </select>
                    </div>
                </div>
                <div class="modal-item" style=" grid-column: 1 / 3; width: 90%; margin: 0 5%;">
                    <div class="item-header">Address</div>
                    <div class="item-input"><input type="text" class="orderAddress"
                            value="<?= $order['diaChiGiaoHang'] ?>" disabled></div>
                </div>
            </div>
        </div>
        <div class="modal-right">
            <div class="title-list">
                <div class="title-placeholder">
                    <div class="title">No.</div>
                    <div class="title">AID</div>
                    <div class="title">Album name</div>
                    <div class="title">Quantity</div>
                    <div class="title">Price</div>
                </div>
            </div>
            <div class="list">
                <?php for ($i = 0; $i < count($detailOrder); $i++): ?>
                    <div class="placeholder">
                        <div class="info">
                            <div class="item">
                                <?= sprintf("%02d", $i + 1) ?>
                            </div>
                            <div class="item">
                                <?= $detailOrder[$i]['album'] ?>
                            </div>
                            <div class="item">
                                <?= $detailOrder[$i]['ten'] ?>
                            </div>
                            <div class="item">
                                <?= $detailOrder[$i]['soLuong'] ?>
                            </div>
                            <div class="item>" style="
                            display:flex;
                            justify-content:center;
                            align-items:center;
                            color: var(--gr1)"><?= $detailOrder[$i]['gia'] ?></div>
                        </div>
                    </div>
                <?php endfor; ?>
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <?php if (checkCanAccess(11)): ?>
                    <?php if ($order['trangThai'] != 'Cancel' && $order['trangThai'] != 'Delivered'): ?>
                        <div class="edit-button" onclick="loadModalBoxByAjax('editOrder',<?= $orderID ?>)">
                            <div class="icon-placeholder"><i class="fa-solid fa-pen-to-square"></i></div>
                            <div class="info-placeholder">Edit</div>
                        </div>
                    <?php else: ?>
                        <div></div>
                    <?php endif ?>
                <?php else: ?>
                    <div></div>
                <?php endif; ?>
                <div class="back-button" onclick="closeDetailorder()">
                    <div class="icon-placeholder"><i class="fa-solid fa-angle-left"></i></div>
                    <div class="info-placeholder">Back</div>
                </div>
            </div>
        </div>
    </div>
</div>
<?php
function getOrder($orderID)
{
    global $dp;
    $sql = "SELECT * FROM hoadon WHERE maHoaDon = " . $orderID;
    $result = $dp->excuteQuery($sql);
    return $result->fetch_assoc();
}
function getDetailOrder($orderID)
{
    global $dp;
    $sql = "SELECT chitiethoadon.*, album.tenAlbum as ten, album.gia as gia
            FROM chitiethoadon join album on chitiethoadon.album = album.maAlbum
            WHERE hoaDon = " . $orderID;
    $result = $dp->excuteQuery($sql);
    $detailOrder = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($detailOrder, $row);
        }
    }
    return $detailOrder;
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}
?>