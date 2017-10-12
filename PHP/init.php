<?php
	$db_name	 = "projetInfo";
	$mysql_user  = "user";
	$mysql_pass  = "enib29pinfo!!";
	$server_name = "localhost";
	
	$con = mysqli_connect($server_name, $mysql_user, $mysql_pass, $db_name);
	
	if(!$con) {
		//echo "Connection Error...".mysqli_connect_error();
		}
	else {
		//echo "<h3>Database connection success.</h3>";
		mysqli_set_charset($con, 'utf8'); // Permet d'éviter les bugs lors du json_encode()
		}
	
?>
