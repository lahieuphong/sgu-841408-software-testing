<?php
$filename = $_FILES["file"]["name"];
$target_directory = $_POST['target_directory'];
$target_file = $target_directory . basename($_FILES["file"]["name"]);
$newfilename = $target_directory . $filename;
if (move_uploaded_file($_FILES["file"]["tmp_name"], $newfilename))
    echo 1;
else
    echo 0;
?>