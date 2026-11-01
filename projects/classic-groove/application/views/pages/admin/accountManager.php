<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$account = getAllAccount();
?>
<div id="accountManager">
    <div class="header">
        <h2><i class="fa-solid fa-user fa-sm"></i> Account management</h2>
        <?php if (checkCanAccess(7)): ?>
            <div class="button-placeholder">
                <div class="new-button" onclick="loadModalBoxByAjax('newAccount')">
                    <div class="icon-placeholder"><i class="fa-solid fa-user-plus fa-sm"></i></div>
                    <div class="info-placeholder">New</div>
                </div>
            </div>
        <?php endif ?>
    </div>
    <div class="title-list">
        <div class="title-placeholder">
            <div class="title" style="padding-right: 10px;">No.</div>
            <div class="title">Username</div>
            <div class="title">Account name</div>
            <div class="title">Phone number</div>
            <div class="title">Role</div>
            <div class="title">Status</div>
        </div>
    </div>
    <div class="list">
        <?php for ($i = 0; $i < count($account); $i++): ?>
            <div class="placeholder">
                <div class="info">
                    <div class="item">
                        <?= sprintf("%02d", $i + 1) ?>
                    </div>
                    <div class="item">
                        <?= $account[$i]['username'] ?>
                    </div>
                    <div class="item">
                        <?= $account[$i]['hoTen'] ?>
                    </div>
                    <div class="item">
                        <?= $account[$i]['SDT'] ?>
                    </div>
                    <div class="item">
                        <?= $account[$i]['tenVaiTro'] ?>
                    </div>
                    <div class="item">
                        <?= $account[$i]['TrangThai'] ?>
                    </div>
                    <div class="item" onclick="loadModalBoxByAjax('detailAccount', '<?= $account[$i]['username'] ?>')">
                        <i class="fa-regular fa-circle-info"></i>
                    </div>
                </div>
            </div>
        <?php endfor; ?>
    </div>
    <div id="modal-box"></div>
</div>

<?php
function getAllAccount()
{
    global $dp;
    $sql = "SELECT * FROM taikhoan
            join nguoidung on taikhoan.username = nguoidung.maNguoiDung
            join vaitro on taikhoan.vaiTro = vaitro.maVaiTro";
    $result = $dp->excuteQuery($sql);
    $account = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($account, $row);
        }
    }
    return $account;
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}
?>