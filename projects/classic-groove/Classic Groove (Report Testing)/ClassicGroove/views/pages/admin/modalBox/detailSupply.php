<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
$recordID = $_POST["id"];
$record = getRecord($recordID);
$detailRecord = getDetailRecord($recordID);
?>
<div class="modal-placeholder" id="detail-supply">
    <div class="modal-box">
        <div class="modal-header ">
            <h1><i class="fa-regular fa-square-kanban fa-rotate-270"></i>Supply detail</h1>
        </div>
        <div class="modal-left ">
            <div class="modal-info">
                <div class="modal-item">
                    <div class="item-header">Record Id</div>
                    <div class="item-input"><input type="text" class="albumID" value="<?= $record['maPhieuNhap'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Importer</div>
                    <div class="item-input"><input type="text" class="albumName" value="<?= $record['nguoiNhap'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Record date</div>
                    <div class="item-input"><input type="text" class="albumArtist"
                            value="<?= date("d/m/Y", strtotime($record['ngayNhap'])) ?> " disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Total cost</div>
                    <div class="item-input"><input type="text" class="albumQuanitity" value="<?= $record['TongGia'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item" style=" grid-column: 1 / 3; width: 90%; margin: 0 5%;">
                    <div class="item-header">Distributor</div>
                    <div class="item-input"><input type="text" class="albumQuanitity" value="<?= $record['tenNCC'] ?>"
                            disabled></div>
                </div>
            </div>
        </div>
        <div class="modal-right ">
            <div class="title-list">
                <div class="title-placeholder">
                    <div class="title" style="padding-right: 10px;">No.</div>
                    <div class="title" style="padding-right: 15px;">Album ID</div>
                    <div class="title" style="padding-right: 15px;">Price</div>
                    <div class="title" style="padding-right: 10px;">Quantity</div>
                </div>
            </div>
            <div class="list">
                <?php for ($i = 0; $i < count($detailRecord); $i++): ?>
                    <div class="placeholder">
                        <div class="info">
                            <div class="item">
                                <?= sprintf("%02d", $i + 1) ?>
                            </div>
                            <div class="item">
                                <?= $detailRecord[$i]['album'] ?>
                            </div>
                            <div class="item">
                                <?= $detailRecord[$i]['gia'] ?>
                            </div>
                            <div class="item">
                                <?= $detailRecord[$i]['SoLuong'] ?>
                            </div>
                        </div>
                    </div>
                <?php endfor; ?>
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <div></div>
                <div></div>
                <div class="back-button" onclick="closeDetailSupply()">
                    <div class="icon-placeholder"><i class="fa-solid fa-angle-left"></i></div>
                    <div class="info-placeholder">Back</div>
                </div>
            </div>
        </div>
    </div>
</div>
<?php
function getRecord($recordID)
{
    global $dp;
    $dp = new DataProvider();
    $sql = "SELECT * FROM phieunhap join nhacungcap on phieunhap.NCC = nhacungcap.maNCC WHERE maPhieuNhap = $recordID";
    $result = $dp->excuteQuery($sql);
    return $result->fetch_assoc();
}
function getDetailRecord($recordID)
{
    global $dp;
    $dp = new DataProvider();
    $sql = "SELECT * FROM chitietphieunhap WHERE phieuNhap = $recordID";
    $result = $dp->excuteQuery($sql);
    $detailRecord = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($detailRecord, $row);
        }
    }
    return $detailRecord;
}
?>