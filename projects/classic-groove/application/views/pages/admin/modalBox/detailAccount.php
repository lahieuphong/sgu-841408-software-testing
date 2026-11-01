<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$accountID = $_POST["id"];
$account = getAccount($accountID);
$role = getListRole();
?>
<div class="modal-placeholder" id="detail-account">
    <div class="modal-box">
        <div class="modal-header">
            <h1><i class="fa-regular fa-square-kanban fa-rotate-270"></i>Account details</h1>
        </div>
        <div class="modal-info">
            <div class="modal-item">
                <div class="item-header">Account id</div>
                <div class="item-input"><input type="text" value="<?= $account['username'] ?>" disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Account name</div>
                <div class="item-input"><input type="text" value="<?= $account['hoTen'] ?>" disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Email</div>
                <div class="item-input"><input type="text" value="<?= $account['email'] ?>" disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Phone number</div>
                <div class="item-input"><input type="text" value="<?= $account['SDT'] ?>" disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Date created</div>
                <div class="item-input"><input type="text" value="<?= date('d/m/Y', strtotime($account['ngayTao'])) ?>"
                        disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Role</div>
                <div class="item-input"><select name="" id="" disabled>
                        <option value="<?= $account['vaiTro'] ?>"> <?= $account['tenVaiTro'] ?></option>
                    </select>
                </div>
            </div>
            <div class="modal-item">
                <div class="item-header">Status</div>
                <div class="item-input"><input type="text" value="<?= $account['TrangThai'] ?>" disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Password</div>
                <div class="item-input"><input type="text" value="<?= $account['matKhau'] ?>" disabled></div>
            </div>
            <div class="modal-item" style=" grid-column: 1 / 3; width: 90%; margin: 0 5%;">
                <div class="item-header">Address</div>
                <div class="item-input"><input type="text" class="orderAddress" value="<?= $account['diaChi'] ?>"
                        disabled></div>
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <?php if (checkCanAccess(8)): ?>
                    <div class="edit-button" onclick="loadModalBoxByAjax('editAccount','<?= $accountID ?>')">
                        <div class="icon-placeholder"><i class="fa-solid fa-pen-to-square"></i></div>
                        <div class="info-placeholder">Edit</div>
                    </div>
                <?php else: ?>
                    <div></div>
                <?php endif; ?>
                <div class="back-button" onclick="closeDetailAccount()">
                    <div class="icon-placeholder"><i class="fa-solid fa-angle-left"></i></div>
                    <div class="info-placeholder">Back</div>
                </div>
            </div>
        </div>
    </div>
</div>
<?php
function getAccount($accountID)
{
    global $dp;
    $sql = "SELECT * FROM taikhoan
            join nguoidung on taikhoan.username = nguoidung.maNguoiDung
            join vaitro on taikhoan.vaiTro = vaitro.maVaiTro
            WHERE taikhoan.username ='" . $accountID . "'";
    $result = $dp->excuteQuery($sql);
    return $result->fetch_assoc();
}
function getListRole()
{
    global $dp;
    $sql = "SELECT * FROM vaitro";
    $result = $dp->excuteQuery($sql);
    $role = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($role, $row);
        }
    }
    return $role;
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}
?>