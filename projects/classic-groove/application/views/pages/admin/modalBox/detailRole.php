<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$roleID = $_POST['id'];
$role = getRole($roleID);
$listPermission = getListPermission($roleID);
$functions = getAllFunction();
?>

<h1>Role descriptions</h1>
<div class="info-role">
    <div class="role-header">Role infomation</div>
    <div class="row">
        <label for="">ID:</label>
        <Span>
            <?= $role['maVaiTro'] ?>
        </Span>
    </div>
    <div class="row">
        <label for="">Name:</label>
        <?php if (checkCanAccess(16)): ?>
            <input type="text" value=" <?= $role['tenVaiTro'] ?>">
        <?php else: ?>
            <input type="text" value=" <?= $role['tenVaiTro'] ?>" disabled>
        <?php endif ?>
    </div>
    <div class="row">
        <label for="">Des:</label>
        <?php if (checkCanAccess(16)): ?>
            <textarea name="" id="" cols="30" rows="5"> <?= $role['moTa'] ?></textarea>
        <?php else: ?>
            <textarea name="" id="" cols="30" rows="5" disabled> <?= $role['moTa'] ?></textarea>
        <?php endif ?>
    </div>
    <div class="button-layout">
        <?php if (checkCanAccess(16)): ?>
            <div class="button-container" onclick="updateRole(<?= $role['maVaiTro'] ?>)">
                <i class="fa-solid fa-folder-arrow-down"></i>
                <span class="info-placeholder">save</span>
            </div>
        <?php endif ?>
        <?php if (checkCanAccess(17)): ?>
            <div class="button-container" onclick="deleteRole(<?= $role['maVaiTro'] ?>)">
                <i class="fa-solid fa-x"></i>
                <span class="info-placeholder">delete</span>
            </div>
        <?php endif ?>

    </div>
</div>
<div class="role-placeholder">
    <?php foreach ($functions as $fs): ?>
        <div class="role-box">
            <div class="role-header">
                <?= $fs['tenChucNang'] ?> management
            </div>
            <?php foreach (getDetailRoleByFunction($fs['maChucNang']) as $f): ?>
                <div class="role-item">
                    <?= $f['NoiDungQuyen'] ?>
                </div>
                <div class="checkbox-placeholder">
                    <input type="checkbox" value="<?= $f['maCTQ'] ?>" <?php if (checkExist($f['maCTQ'])): ?>checked<?php endif ?>
                        <?php if (!checkCanAccess(16)): ?> disabled<?php endif ?>>
                </div>
            <?php endforeach ?>
        </div>
    <?php endforeach ?>
</div>
<?php
function getRole($roleID)
{
    global $dp;
    $sql = "SELECT * FROM vaitro where maVaiTro = " . $roleID;
    $result = $dp->excuteQuery($sql);
    return $result->fetch_assoc();
}
function getListPermission($roleID)
{
    global $dp;
    $sql = "SELECT * FROM vaitro_quyen where VaiTro_maVaiTro = " . $roleID;
    $result = $dp->excuteQuery($sql);
    $listPermission = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($listPermission, $row['Quyen_maCTQ']);
        }
    }
    return $listPermission;
}
function checkExist($perID)
{
    global $listPermission;
    foreach ($listPermission as $per) {
        if ($per == $perID) {
            return true;
        }
    }
    return false;
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}

function getAllFunction()
{
    global $dp;
    $sql = "SELECT * FROM chucnang";
    $result = $dp->excuteQuery($sql);
    $function = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($function, $row);
        }
    }
    return $function;
}
function getDetailRoleByFunction($f)
{
    global $dp;
    $sql = "SELECT * FROM quyen WHERE chucNang = $f";
    $result = $dp->excuteQuery($sql);
    $detailRole = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($detailRole, $row);
        }
    }
    return $detailRole;
}
?>