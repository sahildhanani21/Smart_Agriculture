<?php

$servername = "localhost";

$username = "";

$password = "";

$dbname = "id19667734_agriitech";

$conn = new mysqli($servername, $username, $password, $dbname);

if (!$conn){

	die("Connection Failed: ". mysqli_connect_error());

} ?>

