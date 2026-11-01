<?php
require("../../../util/dataProvider.php");
$dp = new DataProvider();
session_start();
$userID = $_SESSION['userID'];
$sql1 = "SELECT giohang.soLuong as ghsl, album.*, theloai.* FROM giohang join album on giohang.maAlbum = album.maAlbum
        join theloai on album.theloai = theloai.maLoai where maKhachHang = '" . $userID . "'";
$result1 = $dp->excuteQuery($sql1);
$album = array();
if ($result1->num_rows > 0) {
    while ($row = $result1->fetch_assoc()) {
        array_push($album, $row);
    }
}
$sql2 = "select diaChi from nguoiDung where maNguoiDung='" . $userID . "'";
$result2 = $dp->excuteQuery($sql2);
$address = $result2->fetch_assoc()['diaChi'];
?>
<div id="mycart">
    <div class="left-placeholder">
        <?php foreach ($album as $al): ?>
            <div class="product-placeholder">
                <div class="product-img-placeholder">
                    <img src="data/imgAlbum/<?= $al['hinh'] ?>" alt="poster">
                </div>
                <div class="product-info-placeholder">
                    <div class="album-name">
                        <?= $al['tenAlbum'] ?>
                    </div>
                    <div class="album-artist">
                        <?= $al['tacGia'] ?>
                    </div>
                    <div class="product-kind">
                        <?= $al['tenLoai'] ?>
                    </div>
                    <div class="QPT">
                        <div class="QPT-info">Quantity</div>
                        <div class="QPT-info">Price</div>
                        <div class="QPT-info">Total</div>
                        <div class="QPT-info">
                            <div class="quantity-placeholder">
                                <div class="quantity-info"
                                    onclick="changeQuantity(<?= $al['maAlbum'] ?>,-1,this);summary()">
                                    <i class="fa-solid fa-minus fa-xs"></i>
                                </div>
                                <input type="text" class="quantity-info" value="<?= $al['ghsl'] ?>"
                                    onchange="changeQuantity(<?= $al['maAlbum'] ?>,0,this);summary()">
                                <div class="quantity-info" onclick="
                                changeQuantity(<?= $al['maAlbum'] ?>,1,this);summary()">
                                    <i class="fa-solid fa-plus-large fa-xs"></i>
                                </div>
                            </div>
                        </div>
                        <div class="QPT-info each">$
                            <?= number_format((float) $al["gia"], 2, '.', '') ?>
                        </div>
                        <div class="QPT-info total">$
                            <?= number_format((float) ($al['gia'] * $al['ghsl']), 2, '.', '') ?>
                        </div>
                    </div>
                </div>
                <div class="button-placeholder">
                    <div class="erase-button" onclick=deleteFromCart(<?= $al['maAlbum'] ?>,this)>
                        <i class="fa-solid fa-xmark fa-lg"></i>
                    </div>
                    <div class="check-button">
                        <input type="checkbox" value="<?= $al['maAlbum'] ?>" onchange="summary(this)">
                    </div>
                </div>
            </div>
        <?php endforeach ?>
    </div>
    <div class="right-placeholder">
        <div class="totalprice-placeholder">
            <div class="totalprice-header">
                <h1>Checkout</h1>
            </div>
            <div class="checkout-address">
                Address
                <textarea name="" id="checkout-address" cols="20" rows="5"><?php echo $address ?></textarea>
            </div>
            <div class="totalprice-info">
                <div class="price-kind">Subtotal:</div>
                <div class="price-detail subtotal">$0.00</div>
                <div class="price-kind">Shipping:</div>
                <div class="price-detail shipping">$0.00</div>
                <div class="price-kind">Discount:</div>
                <div class="price-detail discount">$0.00</div>
            </div>
            <div class="totalprice-final">
                <div class="price-kind">Total:</div>
                <div class="price-detail total-final">$0.00</div>
            </div>
            <div class="totalprice-button" onclick="order()">
                <button>Place order</button>
            </div>
        </div>
    </div>
    <div class="modal-placeholder" id="orderSuccess">
        <div class="modal-box">
            <div class="modal-info-placeholder">
                <div class="modal-info">
                    <div class="img-placeholder">
                        <img src="views/assets/img/fast-delivery.png" alt="">
                    </div>
                </div>
                <div class="modal-info">Your order is being processed and shipped in shortly !</div>
                <div class="modal-info">Thank you for buying our albums</div>
            </div>
            <div class="modal-button-placeholder">
                <div class="home-button" onclick="loadHomeByAjax(1)">
                    <div class="button-item">
                        <i class="fa-solid fa-house "></i>
                    </div>
                    <div class="button-item">
                        Back to home
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>