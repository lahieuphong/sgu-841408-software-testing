<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$newSupplyID = getNewSupplyID();
$distributor = getAllDistributor();
?>
<div class="modal-placeholder" id="new-supply">
    <div class="modal-box">
        <div class="modal-header ">
            <h1><i class="fa-regular fa-square-kanban fa-rotate-270"></i>Supply detail</h1>
        </div>
        <div class="modal-left ">
            <div class="modal-info">
                <div class="modal-item">
                    <div class="item-header">Record Id</div>
                    <div class="item-input"><input type="text" class="supplyID" value="<?= $newSupplyID ?>" disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Importer</div>
                    <div class="item-input"><input type="text" class="supplyImport" value="<?= $_SESSION['userID'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Record date</div>
                    <div class="item-input"><input type="text" class="supplyDate" value="<?= date("d/m/Y") ?> "
                            disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Total cost</div>
                    <div class="item-input"><input type="text" class="total-cost" value="0" disabled></div>
                </div>
                <div class="modal-item" style=" grid-column: 1 / 3; width: 90%; margin: 0 5%;">
                    <div class="item-header">Distributor</div>
                    <div class="item-input"><select class="supplyDistributor" name="" id="">
                            <?php foreach ($distributor as $d): ?>
                                <option value="<?= $d['maNCC'] ?>"><?= $d['tenNCC'] ?></option>
                            <?php endforeach; ?>
                        </select>
                    </div>
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
                
            </div>
            <div class="btnAddAlbum">
                <input type="button" value="+" onclick="openAddAlbum()">
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <div></div>
                <div class="edit-button" onclick="addNewSupply()">
                    <div class="icon-placeholder"><i class="fa-solid fa-pen-to-square"></i></div>
                    <div class="info-placeholder">Add</div>
                </div>
                <div class="back-button" onclick="closeNewSupply()">
                    <div class="icon-placeholder"><i class="fa-solid fa-angle-left"></i></div>
                    <div class="info-placeholder">Back</div>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="modal-placeholder" id="add_exist_album">
    <div class="modal-box">
        <h1><i class="fa-regular fa-pen-to-square"></i>Add Album</h1>
        <div id="suggestion-container">
            <label for="my-input">Type name or id Album:</label> <br> <br>
            <input type="text" id="my-input" name="my-input" oninput="suggestAlbum()">
            <ul id="suggestion-list">
            </ul>
        </div><br>
        <div class="modal-button">
            <input type="button" class="btn-add" value="Add" onclick="addExistingAlbum()">
            <input type="button" class="btn-cancel" value="Cancel" onclick="closeAddAlbum()">
        </div>
    </div>
</div>
<?php
function getNewSupplyID()
{
    global $dp;
    $sql = "SELECT MAX(maPhieuNhap) AS maxID FROM phieunhap";
    $result = $dp->excuteQuery($sql);
    $row = mysqli_fetch_array($result);
    return $row['maxID'] + 1;
}
function getAllDistributor()
{
    global $dp;
    $sql = "SELECT * FROM nhacungcap";
    $result = $dp->excuteQuery($sql);
    $distributor = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($distributor, $row);
        }
    }
    return $distributor;
}
?>