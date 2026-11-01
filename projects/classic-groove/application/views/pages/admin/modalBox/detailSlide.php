<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$slideID = $_POST['id'];
$slideShow = getSlideShow($slideID);
?>
<div class="header">Slide infomation</div>
<div class="top">
    <div class="img-placeholder">
        <img class="imgSlide" src="data/imgAlbum/<?= $slideShow['linkHinh'] ?>" alt="imgSlideShow">
        <input type="button" value="change" onclick=uploadImgSlide()>
    </div>
    <div class="info-placeholder">
        <div class="info">
            <div class="item">Name</div>
            <div class="item">
                <?php if (checkCanAccess(13)): ?>
                    <input class="nameSlide" value="<?= $slideShow['tenHinh'] ?>" type="text">
                <?php else: ?>
                    <input class="nameSlide" value="<?= $slideShow['tenHinh'] ?>" type="text" disabled>
                <?php endif ?>
            </div>
            <div class="item">Linked to</div>
            <div class="item">
                <?php if (checkCanAccess(13)): ?>
                    <input class="linkToSlide" value="<?= $slideShow['linkTo'] ?>" type="text">
                <?php else: ?>
                    <input class="linkToSlide" value="<?= $slideShow['linkTo'] ?>" type="text" disabled>
                <?php endif ?>
            </div>
        </div>
        <div class="button">
            <?php if (checkCanAccess(21)): ?>
                <div class="item" onclick="deleteSlide(<?= $slideShow['maHinh'] ?>)">
                    <input type="button" value="Delete">
                </div>
            <?php else: ?>
                <div></div>
            <?php endif ?>
            <?php if (checkCanAccess(13)): ?>
                <div class="item" onclick="updateSlide(<?= $slideShow['maHinh'] ?>)">
                    <input type="button" value="Save">
                </div>
            <?php else: ?>
                <div></div>
            <?php endif ?>
        </div>
    </div>
</div>

<?php
function getSlideShow($slideID)
{
    global $dp;
    $sql = "SELECT * FROM slideshow where maHinh = $slideID";
    $result = $dp->excuteQuery($sql);
    return $result->fetch_assoc();
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}
?>