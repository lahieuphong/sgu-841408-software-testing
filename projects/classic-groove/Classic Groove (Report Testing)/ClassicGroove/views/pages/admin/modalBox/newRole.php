<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$newRoleID = getNewRoleID();
$functions = getAllFunction();
?>

<h1>Role new</h1>
<div class="info-role">
    <div class="role-header">Role infomation</div>
    <div class="row">
        <label for="">ID:</label>
        <Span>
            <?= $newRoleID ?>
        </Span>
    </div>
    <div class="row">
        <label for="">Name:</label>
        <input type="text" value="">
    </div>
    <div class="row">
        <label for="">Des:</label>
        <textarea name="" id="" cols="30" rows="5"></textarea>
    </div>
    <div class="button-layout">
        <div class="button-container" onclick="addNewRole(<?= $newRoleID ?>)">
            <i class="fa-solid fa-folder-arrow-down"></i>
            <span class="info-placeholder">save</span>
        </div>
        <div class="button-container" onclick="loadPageByAjax('Permission')">
            <i class="fa-solid fa-back"></i>
            <span class="info-placeholder">Cancel</span>
        </div>
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
                    <input type="checkbox" value="<?= $f['maCTQ'] ?>" <?php if (!checkCanAccess(16)): ?> disabled<?php endif ?>>
                </div>
            <?php endforeach ?>
        </div>
    <?php endforeach ?>
</div>
<?php
function getNewRoleID()
{
    global $dp;
    $sql = "SELECT MAX(maVaiTro) AS maxID FROM vaitro";
    $result = $dp->excuteQuery($sql);
    $row = mysqli_fetch_array($result);
    return $row['maxID'] + 1;
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