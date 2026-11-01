<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$role = getAllRole();
?>
<div id="roleManager">
    <div class="header">
        <h2><i class="fa-solid fa-user-pen"></i> Permission</h2>
        <?php if (checkCanAccess(15)): ?>
            <div class="button-placeholder">
                <div class="new-button" onclick="loadModalBoxByAjax('newRole')">
                    <div class="icon-placeholder"><i class="fa-solid fa-user-plus fa-sm"></i></div>
                    <div class="info-placeholder">New</div>
                </div>
            </div>
        <?php endif ?>
    </div>
    <div class="permission-placeholder">
        <div class="title-placeholder">
            <div class="title">No.</div>
            <div class="title">Role id</div>
            <div class="title">Role name</div>
            <div class="title">Description</div>
            <div class="title"></div>

        </div>
        <div class="list-placeholder">
            <?php for ($i = 0; $i < count($role); $i++): ?>
                <div class="role-information">
                    <div class="item">
                        <?= sprintf("%02d", $i + 1) ?>
                    </div>
                    <div class="item">
                        <?= $role[$i]['maVaiTro'] ?>
                    </div>
                    <div class="item">
                        <?= $role[$i]['tenVaiTro'] ?>
                    </div>
                    <div class="item">
                        <?= $role[$i]['moTa'] ?>
                    </div>
                    <div class="item" onclick="loadModalBoxByAjax('detailRole', <?= $role[$i]['maVaiTro'] ?>)"><i
                            class="fa-regular fa-circle-info"></i>
                    </div>
                </div>
            <?php endfor ?>
        </div>
    </div>

    <div id="modal-box"></div>
</div>
<?php
function getAllRole()
{
    global $dp;
    $sql = "SELECT vaiTro FROM taikhoan where username = '" . $_SESSION['userID'] . "'";
    $result = $dp->excuteQuery($sql);
    $currentRole = $result->fetch_assoc()['vaiTro'];
    // $sql = "SELECT * FROM vaitro where maVaiTro not in (1,2,3,$currentRole)";
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