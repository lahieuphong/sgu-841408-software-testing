<?php
$albumID = $_POST['password'];
$damahoa = md5($albumID);
echo $damahoa;