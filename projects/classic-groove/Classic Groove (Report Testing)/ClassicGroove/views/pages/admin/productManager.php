<?php
require("../../../util/dataProvider.php");
session_start();
$dp = new DataProvider();
if (
  isset($_POST['name'])
  && isset($_POST['category'])
  && isset($_POST['priceStart'])
  && isset($_POST['priceEnd'])
  && isset($_POST['orderDirection'])
) {
  $name = $_POST['name'];
  $category = $_POST['category'];
  $priceStart = $_POST['priceStart'];
  $priceEnd = $_POST['priceEnd'];
  $orderBy = $_POST['orderDirection'];
  $album = searchAlbum($name, $category, $priceStart, $priceEnd, $orderBy);
} else {
  $album = getAllAlbum();
}
$category = getAllCategory();
?>

<div id="productManager">
  <div class="header">
    <h2><i class="fa-solid fa-album"></i>&#09; Product management</h2>
    <?php if (checkCanAccess(19)): ?>
      <div class="button-placeholder">
        <div class="new-button" onclick="loadModalBoxByAjax('newAlbum')">
          <div class="icon-placeholder"><i class="fa-solid fa-user-plus fa-sm"></i></div>
          <div class="info-placeholder">New</div>
        </div>
      </div>
    <? else: ?>
      <div></div>
    <?php endif ?>
    <div class="search-bar">
      <div class="search-input">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" placeholder="Looking for somethings?" onchange="loadAlbumByAjax()">
      </div>
      <div class="filter-input">
        <i class="fa-regular fa-filter"></i>
        <select name="" id="" onchange="loadAlbumByAjax()">
          <option value="0">All</option>
          <?php
          foreach ($category as $cat) {
            echo "<option value='" . $cat['maLoai'] . "'>" . $cat['tenLoai'] . "</option>";
          }
          ?>
        </select>
      </div>
      <div class="date-begin price-begin">
        <i class="fa-thin fa-coin"></i>
        <input type="text" name="" id="" placeholder="Start price" value="" onchange="loadAlbumByAjax()">
      </div>
      <div class="date-end price-end">
        <i class="fa-thin fa-coins"></i>
        <input type="text" name="" id="" placeholder="End price" value="" onchange="loadAlbumByAjax()">
      </div>
    </div>
  </div>
  <div class="title-list">
    <div class="title-placeholder">
      <div class="title">No.</div>
      <div class="title">AlbumID</div>
      <div class="title">
        <span>Album name</span>
        <i class="fa-solid  fa-up" onclick="turnArrow(this);loadAlbumByAjax()"></i>
      </div>
      <div class="title">Artist name</div>
      <div class="title">Kind</div>
      <div class="title">Price</div>
      <div class="title">Quanitity</div>
    </div>
  </div>
  <div class="list">
    <?php for ($i = 0; $i < count($album); $i++): ?>
      <div class="placeholder">
        <div class="info">
          <div class="item">
            <?= sprintf("%02d", $i + 1) ?>
          </div>
          <div class="item">
            <?= $album[$i]['maAlbum'] ?>
          </div>
          <div class="item">
            <?= $album[$i]['tenAlbum'] ?>
          </div>
          <div class="item">
            <?= $album[$i]['tacGia'] ?>
          </div>
          <div class="item">
            <?= $album[$i]['tenLoai'] ?>
          </div>
          <div class="item">
            <?= $album[$i]['gia'] ?>
          </div>
          <div class="item">
            <?= $album[$i]['soLuong'] ?>
          </div>
          <div class="item" onclick="loadModalBoxByAjax('detailAlbum',<?= $album[$i]['maAlbum'] ?>)">
            <i class="fa-regular fa-circle-info"></i>
          </div>
        </div>
      </div>
    <?php endfor; ?>
  </div>
  <div id="modal-box"></div>
</div>




<?php
function getAllAlbum()
{
  global $dp;
  $sql = "SELECT *
        FROM album join theloai on album.theLoai = theloai.maLoai
        where album.TrangThai = 1
        ORDER BY tenAlbum ASC";
  $result = $dp->excuteQuery($sql);
  $album = array();
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      array_push($album, $row);
    }
  }
  return $album;
}
function checkCanAccess($permission)
{
  if (in_array($permission, $_SESSION['permission']))
    return true;
  return false;
}
function getAllCategory()
{
  global $dp;
  $sql = "SELECT * FROM theloai ";
  $result = $dp->excuteQuery($sql);
  $category = array();
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      array_push($category, $row);
    }
  }
  return $category;
}
function searchAlbum($name, $category, $priceStart, $priceEnd, $orderBy)
{
  global $dp;
  $sql = "SELECT *
          FROM album join theloai on album.theLoai = theloai.maLoai
          where trangThai = 1 ";
  $f = false;
  if ($name != "" || $category != 0 || $priceStart != "" && $priceEnd != "") {
    $sql = $sql . "and ";
    if ($name != "") {
      $sql = $sql . "(tenAlbum LIKE '%" . $name . "%' ";
      $sql = $sql . " or maAlbum LIKE '%" . $name . "%') ";
      $f = true;
    }
    if ($category != 0) {
      if ($f) {
        $sql = $sql . "and ";
      }
      $sql = $sql . "theLoai = " . $category . " ";
      $f = true;
    }
    if ($priceStart != "" && $priceEnd != "") {
      if ($f) {
        $sql = $sql . "and ";
      }
      $sql = $sql . "gia >= " . $priceStart . " and gia <= " . $priceEnd . " ";
      $f = true;
    }
  }
  if ($orderBy == "1")
    $sql = $sql . " ORDER BY tenAlbum ASC";
  else {
    $sql = $sql . " ORDER BY tenAlbum DESC";
  }
  $result = $dp->excuteQuery($sql);
  $album = array();
  if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
      array_push($album, $row);
    }
  }
  return $album;
}
?>