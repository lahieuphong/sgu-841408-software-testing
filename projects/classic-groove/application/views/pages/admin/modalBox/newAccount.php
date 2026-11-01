<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
$role = getListRole();
?>
<div class="modal-placeholder" id="new-account">
    <div class="modal-box">
        <div class="modal-header">
            <h1><i class="fa-solid fa-user-plus"></i>New Account</h1>
        </div>
        <div class="modal-info">
            <div class="modal-item">
                <div class="item-header">Username</div>
                <div class="item-input"><input class="username" type="text"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Account name</div>
                <div class="item-input"><input class="name" type="text"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Email</div>
                <div class="item-input"><input class="email" type="text"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Phone number</div>
                <div class="item-input"><input class="phoneNumber" type="text"></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Date created</div>
                <div class="item-input"><input type="text" value="<?= date('d/m/Y') ?>" disabled></div>
            </div>
            <div class="modal-item">
                <div class="item-header">Role</div>
                <div class="item-input"><select class="role" name="" id="">
                        <?php foreach ($role as $r): ?>
                            ?>
                            <option value="<?= $r['maVaiTro'] ?>"><?= $r['tenVaiTro'] ?></option>
                        <?php endforeach ?>
                    </select>
                </div>
            </div>
            <div class="modal-item">
                <div class="item-header">Status</div>
                <div class="item-input"><input type="text" style="cursor:default !important" value="Hoạt động" disabled>
                </div>
            </div>
            <div class="modal-item">
                <div class="item-header">Password</div>
                <div class="item-input"><input class="password" type="text"></div>
            </div>
            <div class="modal-item" style=" grid-column: 1 / 3; width: 90%; margin: 0 5%;">
                <div class="item-header">Address</div>
                <div class="item-input"><input type="text" class="address"></div>
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <div class="edit-button" onclick="createNewAccount()">
                    <div class="icon-placeholder"><i class="fa-solid fa-user-plus"></i></div>
                    <div class="info-placeholder">Add</div>
                </div>
                <div class="back-button" onclick="closeNewAccount()">
                    <div class="icon-placeholder"><i class="fa-solid fa-xmark"></i></div>
                    <div class="info-placeholder">Cancel</div>
                </div>
            </div>
        </div>
    </div>
</div>
<?php
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
?>