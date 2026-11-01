<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$supplyRecord = getAllSupplyRecord();
?>
<div id="supplyRecord">
  <div class="header">
    <h2><i class="fa-regular fa-box-open"></i> Supply record</h2>
    <?php if (checkCanAccess(5)): ?>
      <div class="button-placeholder">
        <div class="new-button" onclick="loadModalBoxByAjax('newSupply')">
          <div class="icon-placeholder"><i class="fa-solid fa-album-circle-plus"></i></div>
          <div class="info-placeholder">New</div>
        </div>
      </div>
    <?php endif ?>
  </div>
  <div class="title-list">
    <div class="title-placeholder">
      <div class="title" style="padding-right: 10px;">No.</div>
      <div class="title" style="padding-right: 15px;">Record ID</div>
      <div class="title" style="padding-right: 15px;">Importer</div>
      <div class="title" style="padding-right: 10px;">Record date</div>
      <div class="title">Total cost</div>
      <div class="title">Supplier</div>
      <div class="title"></div>
    </div>
  </div>
  <div class="list">
    <?php for ($i = 0; $i < count($supplyRecord); $i++): ?>
      <div class="placeholder">
        <div class="info">
          <div class="item">
            <?= sprintf("%02d", $i + 1) ?>
          </div>
          <div class="item">
            <?= $supplyRecord[$i]['maPhieuNhap'] ?>
          </div>
          <div class="item">
            <?= $supplyRecord[$i]['nguoiNhap'] ?>
          </div>
          <div class="item">
            <?= date("d/m/Y", strtotime($supplyRecord[$i]['ngayNhap'])) ?>
          </div>
          <div class="item">
            <?= $supplyRecord[$i]['TongGia'] ?>
          </div>
          <div class="item">
            <?= $supplyRecord[$i]['tenNCC'] ?>
          </div>
          <div class="item" onclick="loadModalBoxByAjax('detailSupply',<?= $supplyRecord[$i]['maPhieuNhap'] ?>)"><i
              class="fa-regular fa-circle-info"></i></div>
        </div>
      </div>
    <?php endfor; ?>
  </div>
  <div id="modal-box"></div>
</div>

<?php
function getAllSupplyRecord()
{
  global $dp;
  $sql = "SELECT * FROM phieunhap join nhacungcap on phieunhap.NCC = nhacungcap.maNCC";
  $result = $dp->excuteQuery($sql);
  $supplyRecord = array();
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      array_push($supplyRecord, $row);
    }
  }
  return $supplyRecord;
}
function checkCanAccess($permission)
{
  if (in_array($permission, $_SESSION['permission']))
    return true;
  return false;
}
?>