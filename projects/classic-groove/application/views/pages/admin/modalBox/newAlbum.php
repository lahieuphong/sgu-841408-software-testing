<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
$newID = getNewID();
$kinds = getKinds();
?>
<div class="modal-placeholder" id="new-album">
    <div class="modal-box">
        <div class="modal-header">
            <h1><i class="fa-regular fa-album-circle-plus"></i>New album</h1>
        </div>
        <div class="modal-left ">
            <div class="modal-info">
                <div class="modal-item">
                    <div class="item-header">Album id</div>
                    <div class="item-input"><input type="text" class="albumID" value="<?= $newID ?>" disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Album name</div>
                    <div class="item-input"><input type="text" class="albumName" value="">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Kind</div>
                    <div class="item-input"><select class="albumKind" name="" id="">
                            <option value="0">Choose type</option>
                            <?php foreach ($kinds as $k): ?>
                                <option value="<?= $k['maLoai'] ?>"><?= $k['tenLoai'] ?></option>
                            <?php endforeach ?>
                        </select>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Artist name</div>
                    <div class="item-input"><input type="text" class="albumArtist" value="">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Quanitity</div>
                    <div class="item-input"><input type="text" class="albumQuanitity" value="0" disabled>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Price</div>
                    <div class="item-input"><input type="text" class="albumPrice" value=""></div>
                </div>

                <div class="modal-item">
                    <div class="item-header">Image</div>
                    <div class="item-input img-container">
                        <img width="100%" src="data/imgAlbum/default.jfif" alt="img">
                        <input type="button" value="Change" onclick="uploadImg()">
                        <input type="button" value="Delete" onclick="deleteImg()">
                    </div>
                </div>
                <div class="modal-item">
                    <div class="item-header">Describe</div>
                    <div class="item-input"><textarea class="albumDescribe" cols="30" rows="6"></textarea></div>
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
                <div class="edit-button" onclick="newAlbum(<?= $newID ?>)">
                    <div class="icon-placeholder"><i class="fa-solid fa-folder-arrow-down"></i></div>
                    <div class="info-placeholder">Add</div>
                </div>
                <div class="back-button" onclick="closeNewalbum()">
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
function getNewID()
{
    global $dp;
    $sql = "SELECT MAX(maAlbum) AS 'newID' FROM album";
    $result = $dp->excuteQuery($sql);
    $newID = 0;
    if ($result->num_rows > 0) {
        $newID = $result->fetch_assoc()['newID'] + 1;
    }
    return $newID;
}
?>