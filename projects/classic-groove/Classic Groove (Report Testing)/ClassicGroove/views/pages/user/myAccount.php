<?php
session_start();
require("../../../util/dataProvider.php");
$dp = new DataProvider();
$userID = $_SESSION['userID'];
$result = $dp->getUserByUsername($_SESSION['userID']);
$userInfo = $result->fetch_assoc();
//get bill
$bill = getBill();
sortBillByDateDesc($bill);
//get bill detail
$billDetail = getBillDetail($bill);
//handle detail bil to bill
filtBillDetailToBill($billDetail, $bill);
?>
<div onload="" id="myaccount">
    <div class="flex-container">
        <h2>My profile</h2>
        <div class="top-container">
            <div class="container-info">
                <div class="title">Name</div>
                <div class="title">Phone number</div>
                <div class="info"><input type="text" id="txtHoTen" oninput="IsInfoChange()"
                        value="<?php echo $userInfo['hoTen'] ?>"></div>
                <div class="info"><input type="text" id="txtSDT" oninput="IsInfoChange()"
                        value="<?php echo $userInfo['SDT'] ?>"></div>
                <div class="title">Username</div>
                <!-- <div class="title">Password</div> -->
                <div class="title"></div>
                <div class="info"><input type="text" oninput="IsInfoChange()"
                        value="<?php echo $userInfo['username'] ?>" disabled></div>

                <div></div>
                <div class="title">Address</div>
                <div class="title">Email</div>
                <div class="info"><input type="text" id="txtAddress" oninput="IsInfoChange()"
                        value="<?php echo $userInfo['diaChi'] ?>"></div>
                <div class="info"><input type="text" id="txtEmail" oninput="IsInfoChange()"
                        value="<?php echo $userInfo['email'] ?>"></div>
            </div>
            <div class="contain-button">
                <div class="button-placeholder btnSave"  onclick="updateUser()">
                    <div class="item"><i class="fa-regular fa-floppy-disk"></i></div>
                    <div class="item ">Save change</div>
                </div>
            </div>
        </div>
        <h2>Change password</h2>
        <div class="top-container">
            <div class="container-info" style="grid-template-rows: 1fr 1fr 1fr">
                <div class="title">Old password</div>
                <div class="info"><input type="text" id="txtOldPassword" placeholder='**********'></div>
                <div class="title">New password</div>
                <div class="info"><input type="text" id="txtNewPassword" placeholder='**********'></div>
                <div class="title">Confirm new password</div>
                <div class="info"><input type="text" id="txtConfirmNewPassword" placeholder='**********'></div>
            </div>
            <div class="contain-button">
                <div class="button-placeholder btnSave"style="cursor: pointer; opacity:1" onclick="updatePassword()">
                    <div class="item"><i class="fa-regular fa-floppy-disk"></i></div>
                    <div class="item ">Save change</div>
                </div>
            </div>
        </div>

        <h2>Purchase history</h2>
        <?php foreach ($bill as $b): ?>
            <div class="bottom-container">
                <div class="order-placeholder">
                    <div class="order-header">
                        <div class="order-date">
                            <?= date("F j, Y", strtotime($b['thoiGianDat'])); ?>
                        </div>
                        <div class="order-id">Bill ID:
                            <?= str_pad($b['maHoaDon'], 5, "0", STR_PAD_LEFT) ?>
                        </div>
                        <div class="order-status">
                            <?= $b['trangThai'] ?>
                        </div>
                    </div>
                    <div class="order-details">
                        <?php foreach ($b['detail'] as $detail): ?>
                            <div class="product-placeholder">
                                <div class="img-placeholder">
                                    <img src="./data/imgAlbum/<?= $detail['hinh'] ?>" alt="">
                                </div>
                                <div class="info-placeholder">
                                    <div class="album-name">
                                        <?= $detail['tenAlbum'] ?>
                                    </div>
                                    <div class="sub-total">$
                                        <?= $detail['gia'] * $detail['sl'] ?>
                                    </div>
                                    <div class="artists-name">
                                        <?= $detail['tacGia'] ?>
                                    </div>
                                    <div></div>
                                    <div class="price">Price: $
                                        <?= $detail['gia'] ?>
                                    </div>
                                    <div></div>
                                    <div class="quantity">Quantity:
                                        <?= $detail['sl'] ?>
                                    </div>
                                    <div></div>
                                </div>
                            </div>
                        <?php endforeach ?>
                    </div>
                    <div class="order-total">
                        <div class="total-title">Total billed:</div>
                        <?php
                        $total = 0;
                        foreach ($b['detail'] as $detail) {
                            $total += $detail['gia'] * $detail['sl'];
                        }
                        ?>
                        <div class="total-bill">
                            $
                            <?php echo $total ?>
                        </div>
                    </div>
                    <div class="order-address">
                        <div class="shipping-address">Ship to
                            <?= $b['diaChiGiaoHang'] ?>
                        </div>
                        <?php if ($b['trangThai'] == 'Pending'): ?>
                            <div class="cancel-button" onclick="cancelOrder(
                            <?= $b['maHoaDon'] ?>)">
                                <i class="fa-solid fa-xmark"></i>Cancel
                            </div>
                        <?php endif ?>
                    </div>
                </div>
            </div>
        <?php endforeach ?>
    </div>

</div>

<?php
function getBill()
{
    global $dp;
    $sql1 = "SELECT * FROM hoadon WHERE khachHang = '" . $_SESSION['userID'] . "'";
    $result1 = $dp->excuteQuery($sql1);
    $bill = array();
    while ($row = $result1->fetch_assoc()) {
        array_push($bill, $row);
    }
    return $bill;
}

function getBillDetail($bill)
{
    if (count($bill) == 0) {
        return array();
    }
    global $dp;
    $sql2 = "Select album.*,chitiethoadon.*, chitiethoadon.soLuong as sl from chitiethoadon join album on
    chitiethoadon.album = album.maAlbum where hoaDon in (";
    for ($i = 0; $i < count($bill); $i++) {
        if ($i != count($bill) - 1) {
            $sql2 = $sql2 . $bill[$i]['maHoaDon'] . ",";
        } else {
            $sql2 = $sql2 . $bill[$i]['maHoaDon'] . ")";
        }
    }
    $result2 = $dp->excuteQuery($sql2);
    $billDetail = array();
    while ($row = $result2->fetch_assoc()) {
        array_push($billDetail, $row);
    }
    return $billDetail;
}

function sortBillByDateDesc(&$bill)
{
    for ($i = 0; $i < count($bill); $i++) {
        for ($j = $i + 1; $j < count($bill); $j++) {
            if (strtotime($bill[$i]['thoiGianDat']) < strtotime($bill[$j]['thoiGianDat'])) {
                $temp = $bill[$i];
                $bill[$i] = $bill[$j];
                $bill[$j] = $temp;
            }
        }
    }
    return $bill;
}

function filtBillDetailToBill($billDetail, &$bill)
{
    for ($i = 0; $i < count($bill); $i++) {
        $bill[$i]['detail'] = array();
        for ($j = 0; $j < count($billDetail); $j++) {
            if ($bill[$i]['maHoaDon'] == $billDetail[$j]['hoaDon']) {
                array_push($bill[$i]['detail'], $billDetail[$j]);
            }
        }
    }
}
?>