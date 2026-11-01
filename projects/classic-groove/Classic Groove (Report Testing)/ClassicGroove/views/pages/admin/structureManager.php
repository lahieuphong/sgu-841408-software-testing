<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$slideShow = getAllSlideShow();
?>

<div id="structure">
    <div class="header">
        <h2><i class="fa-solid fa-puzzle"></i> Structure management</h2>
        <?php if (checkCanAccess(20)): ?>
            <div class="button-placeholder">
                <div class="new-button" onclick="loadModalBoxByAjax('newSlide')">
                    <div class="icon-placeholder"><i class="fa-solid fa-user-plus fa-sm"></i></div>
                    <div class="info-placeholder">New</div>
                </div>
            </div>
        <?php endif ?>
    </div>
    <div class="manageSilder">
        <div></div>
        <div class="bottom">
            <div class="title-list">
                <div class="title-placeholder">
                    <div class="title">No.</div>
                    <div class="title">Image</div>
                    <div class="title">Name</div>
                    <div class="title">Linked to</div>
                    <div class="title"></div>
                </div>
            </div>
            <div class="list">
                <?php for ($i = 0; $i < count($slideShow); $i++): ?>
                    <div class="silde-placeholder">
                        <div class="item">
                            <?= sprintf("%02d", $i + 1) ?>
                        </div>
                        <div class="item">
                            <div class="img-placeholder">
                                <img src="data/slideShow/<?= $slideShow[$i]['linkHinh'] ?>" alt="imgSlideShow">
                            </div>
                        </div>
                        <div class="item">
                            <?= $slideShow[$i]['tenHinh'] ?>
                        </div>
                        <div class="item">
                            <?= $slideShow[$i]['linkTo'] ?>
                        </div>
                        <div class="item"><i class="fa-regular fa-circle-info"
                                onclick="loadModalBoxByAjax('detailSlide',<?= $slideShow[$i]['maHinh'] ?>)"></i></div>
                    </div>
                <?php endfor ?>
            </div>
        </div>
        <div id="modal-box"></div>
    </div>
</div>

<?php
function getAllSlideShow()
{
    global $dp;
    $sql = "SELECT * FROM slideshow";
    $result = $dp->excuteQuery($sql);
    $slideShow = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($slideShow, $row);
        }
    }
    return $slideShow;
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}
?>