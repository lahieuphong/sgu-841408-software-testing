<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
$albumID = $_POST['id'];
$album = getAlbum($albumID);
$songs = getSong($albumID);

?>
<div class="modal-placeholder" id="detail-album">
    <div class="modal-box">
        <div class="modal-header ">
            <h1><i class="fa-regular fa-square-kanban fa-rotate-270"></i>Album detail</h1>
        </div>
        <div class="modal-left ">
            <div class="modal-info">
                <div class="modal-item">
                    <div class="item-header">Album id</div>
                    <div class="item-input"><input type="text" class="albumID" value="<?= $album['maAlbum'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Album name</div>
                    <div class="item-input"><input type="text" class="albumName" value="<?= $album['tenAlbum'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Kind</div>
                    <div class="item-input"><select class="albumKind" name="" id="" disabled>
                            <option value="<?= $album['maLoai'] ?>"><?= $album['tenLoai'] ?></option>
                        </select>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Artist name</div>
                    <div class="item-input"><input type="text" class="albumArtist" value="<?= $album['tacGia'] ?>"
                            disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Quanitity</div>
                    <div class="item-input"><input type="text" class="albumQuanitity" value="<?= $album['soLuong'] ?>"
                            disabled></div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Price</div>
                    <div class="item-input"><input type="text" class="albumPrice" value="<?= $album['gia'] ?>" disabled>
                    </div>
                </div>

                <div class="modal-item">
                    <div class="item-header">Image</div>
                    <div class="item-input img-container">
                        <img width="100%" src="data/imgAlbum/<?= $album['hinh'] ?>" alt="img">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Describe</div>
                    <div class="item-input"><textarea cols="30" class="albumDescribe" rows="6"
                            disabled><?= $album['moTa'] ?></textarea>
                    </div>
                </div>
            </div>
        </div>
        <div class="modal-right ">
            <div class="title-list">
                <div class="title-placeholder">
                    <div class="title" style="padding-right: 10px;">No.</div>
                    <div class="title" style="padding-right: 15px;">SID</div>
                    <div class="title" style="padding-right: 15px;">Song name</div>
                    <div class="title" style="padding-right: 10px;">Song file</div>
                </div>
            </div>
            <div class="list">
                <?php for ($i = 0; $i < count($songs); $i++): ?>
                    <div class="placeholder">
                        <div class="info">
                            <div class="item">
                                <?= sprintf("%02d", $i + 1) ?>
                            </div>
                            <div class="item">
                                <?= $songs[$i]['maBaiHat'] ?>
                            </div>
                            <div class="item">
                                <?= $songs[$i]['tenBaiHat'] ?>
                            </div>
                            <div class="item">
                                <?= $songs[$i]['linkFile'] ?>.mp3
                            </div>
                        </div>
                    </div>
                <?php endfor ?>
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <?php if (checkCanAccess(2)): ?>
                    <div class="edit-button" onclick="loadModalBoxByAjax('editAlbum',<?= $album['maAlbum'] ?>)">
                        <div class="icon-placeholder"><i class="fa-solid fa-pen-to-square"></i></div>
                        <div class="info-placeholder">Edit</div>
                    </div>
                <?php else: ?>
                    <div></div>
                <?php endif ?>
                <?php if (checkCanAccess(3)): ?>
                    <div class="delete-button" onclick="deleteAlbum(<?= $album['maAlbum'] ?>)">
                        <div class="icon-placeholder"><i class="fa-solid fa-xmark"></i></div>
                        <div class="info-placeholder">Delete</div>
                    </div>
                <?php else: ?>
                    <div></div>
                <?php endif ?>
                <div class="back-button" onclick="closeDetailalbum()">
                    <div class="icon-placeholder"><i class="fa-solid fa-angle-left"></i></div>
                    <div class="info-placeholder">Back</div>
                </div>
            </div>
        </div>
    </div>
</div>
<?php
function getAlbum($albumID)
{
    global $dp;
    $sql = "SELECT * FROM album
            join theloai on album.theLoai = theloai.maLoai
            WHERE album.maAlbum =" . $albumID;
    $result = $dp->excuteQuery($sql);
    return $result->fetch_assoc();
}
function getSong($albumID)
{
    global $dp;
    $sql = "SELECT * FROM baihat
        join baihat_album on baihat.maBaiHat = baihat_album.BaiHat_maBaiHat
        WHERE baihat_album.Album_maAlbum =" . $albumID;
    $result = $dp->excuteQuery($sql);
    $songs = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($songs, $row);
        }
    }
    return $songs;
}
function checkCanAccess($permission)
{
    if (in_array($permission, $_SESSION['permission']))
        return true;
    return false;
}
?>