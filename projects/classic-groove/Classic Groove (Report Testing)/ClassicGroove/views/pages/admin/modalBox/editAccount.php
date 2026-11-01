<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
$accountID = $_POST["id"];
$account = getAccount($accountID);
$role = getListRole();
?>
<div class="modal-placeholder" id="edit-account">
    <div class="modal-box">
        <div class="modal-header">
            <h1><i class="fa-regular fa-pen-to-square"></i> Edit Account</h1>
        </div>
        <div class="modal-info">
            <div class="modal-item">
                <div class="item-header">Account id</div>
                <div class="item-input"><input type="text" class="accountID" value="<?= $account['username'] ?>"
                        disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Account name</div>
                <div class="item-input"><input type="text" class="nameAccount" value="<?= $account['hoTen'] ?>"
                        oninput="isAccountInfoChange()"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Email</div>
                <div class="item-input"><input type="text" class="emailAccount" value="<?= $account['email'] ?>"
                        oninput="isAccountInfoChange()"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Phone number</div>
                <div class="item-input"><input type="text" class="phoneAccount" value="<?= $account['SDT'] ?>"
                        oninput="isAccountInfoChange()"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Date created</div>
                <div class="item-input"><input type="text" value="<?= date('d/m/Y', strtotime($account['ngayTao'])) ?>"
                        disabled>
                </div>
            </div>
            <div class="modal-item">
                <div class="item-header">Role</div>
                <div class="item-input"><select name="" class="roleAccount"id="" <?php if ($account['vaiTro'] == 1) {
                    echo 'disabled';
                } ?>  oninput="isAccountInfoChange()">
                        <option value="<?= $account['vaiTro'] ?>"> <?= $account['tenVaiTro'] ?></option>
                        <?php foreach ($role as $r): ?>
                            <option value="<?= $r['maVaiTro'] ?>"><?= $r['tenVaiTro'] ?></option>
                        <?php endforeach ?>
                    </select>
                </div>
            </div>
            <div class="modal-item">
                <div class="item-header">Status</div>
                <div class="item-input"><input type="text" value="<?= $account['TrangThai'] ?>"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Password</div>
                <div class="item-input"><input type="text" class="passwordAccount" value="<?= $account['matKhau'] ?>"
                        oninput="isAccountInfoChange()"></div>
            </div>
            <div class="modal-item" style=" grid-column: 1 / 3; width: 90%; margin: 0 5%;">
                <div class="item-header">Address</div>
                <div class="item-input"><input type="text" class="addressAccount" value="<?= $account['diaChi'] ?>"
                        oninput="isAccountInfoChange()"></div>
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <div class="save-button btnAccountSave" onclick="updateAccount()">
                    <div class="icon-placeholder"><i class="fa-solid fa-folder-arrow-down"></i></div>
                    <div class="info-placeholder">Save</div>
                </div>
                <div class="back-button" onclick="loadModalBoxByAjax('detailAccount','<?= $accountID ?>')">
                    <div class="icon-placeholder"><i class="fa-solid fa-xmark"></i></div>
                    <div class="info-placeholder">Cancel</div>
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
    $sql = "SELECT * FROM vaitro where maVaiTro != 1";
    $result = $dp->excuteQuery($sql);
    $role = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            if ($row['maVaiTro'] == 1) {
                continue;
            }
            array_push($role, $row);
        }
    }
    return $role;
}
?>