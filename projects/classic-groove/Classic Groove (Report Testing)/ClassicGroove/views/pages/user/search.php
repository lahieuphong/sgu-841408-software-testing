<?php
require("util/dataProvider.php");
$dp = new DataProvider();

$sql = "SELECT * FROM theloai ";
$result = $dp->excuteQuery($sql);
$category = array();
if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    array_push($category, $row);
  }
}
?>
<div class="search-container">
  <div class="search">
    <i class="fa-solid fa-magnifying-glass"></i>
    <input type="text" id="search-btn" placeholder="What do you want to listen or buy?" onchange="loadHomeByAjax(1)">
  </div>
</div>
<div class="drop-menu-container">

  <div class="drop-menu">
    <i class="fa-sharp fa-regular fa-bars-filter"></i>
    <select name="" id="drop-menu-btn" onchange="loadHomeByAjax(1)">
      <option value="0">All</option>
      <?php
      foreach ($category as $cat) {
        echo "<option value='" . $cat['maLoai'] . "'>" . $cat['tenLoai'] . "</option>";
      }
      ?>
    </select>
  </div>
</div>
<div class="price-container">
  <div class="price-begin">
    <i class="fa-thin fa-coin"></i>
    <input type="text" name="" id="" placeholder="Start price" value="" onchange="loadHomeByAjax(1)">
  </div>
  <div class="price-end">
    <i class="fa-thin fa-coins"></i>
    <input type="text" name="" id="" placeholder="End price" value="" onchange="loadHomeByAjax(1)">
  </div>
</div>