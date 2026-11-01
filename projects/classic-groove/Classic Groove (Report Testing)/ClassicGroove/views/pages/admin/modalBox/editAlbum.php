<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
$albumID = $_POST['id'];
$album = getAlbum($albumID);
$kinds = getKinds();
$songs = getSong($albumID);
?>
<div class="modal-placeholder" id="edit-album">
    <div class="modal-box">
        <div class="modal-header ">
            <h1><i class="fa-regular fa-pen-to-square"></i> Edit album</h1>
        </div>
        <div class="modal-left ">
            <div class="modal-info">
                <div class="modal-item">
                    <div class="item-header">Album id</div>
                    <div class="item-input"><input type="text" class="albumID" value="<?= $album['maAlbum'] ?>"
                            disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Album name</div>
                    <div class="item-input"><input type="text" class="albumName" value="<?= $album['tenAlbum'] ?>">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Kind</div>
                    <div class="item-input"><select class="albumKind" name="" id="">
                            <option value="<?= $album['maLoai'] ?>"><?= $album['tenLoai'] ?></option>
                            <?php foreach ($kinds as $k): ?>
                                <?php if ($k['maLoai'] == $album['maLoai']) {
                                    continue;
                                }
                                ?>
                                <option value="<?= $k['maLoai'] ?>"><?= $k['tenLoai'] ?></option>
                            <?php endforeach ?>
                        </select>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Artist name</div>
                    <div class="item-input"><input type="text" class="albumArtist" value="<?= $album['tacGia'] ?>">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Quanitity</div>
                    <div class="item-input"><input type="text" class="albumQuanitity" value="<?= $album['soLuong'] ?>" disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Price</div>
                    <div class="item-input"><input type="text" class="albumPrice" value="<?= $album['gia'] ?>"></div>
                </div>

                <div class="modal-item">
                    <div class="item-header">Image</div>
                    <div class="item-input img-container">
                        <img width="100%" src="data/imgAlbum/<?= $album['hinh'] ?>" alt="img">
                        <input type="button" value="Change" onclick="uploadImg()">
                        <input type="button" value="Delete" onclick="deleteImg()">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Describe</div>
                    <div class="item-input"><textarea class="albumDescribe" cols="30"
                            rows="6"><?= $album['moTa'] ?></textarea></div>
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
                            <div class="item"><?=$songs[$i]['maBaiHat']?></div>
                            <div class="item input-container">
                                <input type="text" value="<?= $songs[$i]['tenBaiHat'] ?>">
                            </div>
                            <div class="item input-container songFile-container">
                                <span><?= $songs[$i]['linkFile'] ?>.mp3</span>
                                <input type="button" value="Change" onclick="changeSong(this)">
                            </div>
                            <div class="item" onclick="deleteSong(this)"><i class="fa-solid fa-xmark-large fa-sm"
                                    style="color: #f2623e;"></i></div>
                        </div>
                    </div>
                <?php endfor ?>
            </div>
            <div class="btn-song">
                <input type="button" value="Add new song" onclick="addBlankSong()">
                <input type="button" value="Add existing song" onclick="openAddExistingSong()">
            </div>
        </div>
        <div class="modal-button">
            <div class="button-layout"></div>
            <div class="button-layout">
                <div></div>
                <div class="edit-button" onclick="updateAlbum(<?= $album['maAlbum'] ?>)">
                    <div class="icon-placeholder"><i class="fa-solid fa-folder-arrow-down"></i></div>
                    <div class="info-placeholder">Save</div>
                </div>
                <div class="back-button" onclick="loadModalBoxByAjax('detailAlbum',<?= $album['maAlbum'] ?>)">
                    <div class="icon-placeholder"><i class="fa-solid fa-xmark"></i></div>
                    <div class="info-placeholder">Cancel</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="modal-placeholder" id="add_exist_song">
    <div class="modal-box">
        <h1><i class="fa-regular fa-pen-to-square"></i>Add existing song</h1>
        <div id="suggestion-container">
            <label for="my-input">Type name or id song:</label> <br> <br>
            <input type="text" id="my-input" name="my-input" oninput="suggest()">
            <ul id="suggestion-list">
            </ul>
        </div><br>
        <div class="modal-button">
            <input type="button" class="btn-add" value="Add" onclick="addExistingSong()">
            <input type="button" class="btn-cancel" value="Cancel" onclick="closeAddExistingSong()">
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
function getKinds()
{
    global $dp;
    $sql = "SELECT * FROM theloai";
    $result = $dp->excuteQuery($sql);
    $kinds = array();
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            array_push($kinds, $row);
        }
    }
    return $kinds;
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
?>?>
