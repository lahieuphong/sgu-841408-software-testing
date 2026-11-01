<?php
if (isset($_POST["modalBox"])) {
    switch ($_POST["modalBox"]) {
        case 'detailAlbum':
            include("modalBox/detailAlbum.php");
            break;
        case 'editAlbum':
            include("modalBox/editAlbum.php");
            break;
        case 'newAlbum':
            include("modalBox/newAlbum.php");
            break;
        case 'detailOrder':
            include("modalBox/detailOrder.php");
            break;
        case 'editOrder':
            include("modalBox/editOrder.php");
            break;
        case 'detailAccount':
            include("modalBox/detailAccount.php");
            break;
        case 'editAccount':
            include("modalBox/editAccount.php");
            break;
        case 'newAccount':
            include("modalBox/newAccount.php");
            break;
        case 'detailSupply':
            include("modalBox/detailSupply.php");
            break;
        case 'newSupply':
            include("modalBox/newSupply.php");
            break;
        case 'detailRole':
            include("modalBox/detailRole.php");
            break;
        case 'newRole':
            include("modalBox/newRole.php");
            break;
        case 'detailSlide':
            include("modalBox/detailSlide.php");
            break;
        case 'newSlide':
            include("modalBox/newSlide.php");
            break;
        default:
            echo `<h1>Page not found 404</h1>`;
    }
} else {
    echo `<h1>Page not found 404</h1>`;
}
?>