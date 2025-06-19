<?php

$servername = "localhost";

$username = "id19667734_agriitech_admin";

$password = "Jaypatel@2022";

$dbname = "id19667734_agriitech";

$conn = new mysqli($servername, $username, $password, $dbname);

if (!$conn){

	die("Connection Failed: ". mysqli_connect_error());

} ?>

