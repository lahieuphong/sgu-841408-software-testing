<?php
require("util/dataProvider.php");
$dp = new DataProvider();
session_start();
$role = $_SESSION['role'];
$function = getFunction($role);
?>
<div class="background">
  <div class="top">
    <div class="logo-placeholder">
      <img src="views/assets/img/Logo.png" alt="logo">
    </div>
    <div class="top-menu">
      <?php foreach ($function as $f): ?>
        <?php if (checkCanAccess($f['maCTQ'])): ?>
          <div class="tab-title" onclick="selectMenuAdmin(this,'<?= $f['tenChucNang'] ?>')">
            <div class="tab-icon"><i class="<?= $f['icon'] ?>"></i></div>
            <div class="tab-info">
              <?= $f['tenChucNang'] ?>
            </div>
          </div>
        <?php endif ?>
      <?php endforeach ?>
    </div>
  </div>
  <div class="bottom">
    <div class="info-placeholder" onclick="logout()">
      <h3>Hello
        <?= $_SESSION['userName'] ?>
      </h3>
      <div class="log-out-button">
        <i class="fa-solid fa-right-from-bracket"></i>
      </div>
    </div>
  </div>
</div>
<?php
function checkCanAccess($permission)
{
  if (in_array($permission, $_SESSION['permission']))
    return true;
  return false;
}
function getFunction($role)
{
  global $dp;
  $sql = "SELECT cn.tenChucNang, q.maCTQ, cn.icon
          FROM vaitro vt JOIN vaitro_quyen vtq ON vt.maVaiTro = vtq.VaiTro_maVaiTro
            JOIN quyen q ON vtq.Quyen_maCTQ = q.maCTQ
            JOIN chucNang cn on q.chucNang = cn.maChucNang
          WHERE vt.maVaiTro = $role
          AND q.laTieuDe = 1
          ORDER BY q.chucNang";
  $result = $dp->excuteQuery($sql);
  $function = array();
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      array_push($function, $row);
    }
  }
  return $function;
}
?>