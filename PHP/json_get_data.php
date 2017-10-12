<?php
	require "init.php";
	
	$table = "user_info"; // A CHANGER
	$sql = "SELECT * FROM $table";
	
	$result = mysqli_query($con, $sql);
	
	$response = array();
	
	while ($row = mysqli_fetch_array($result)) {
		array_push($response,array("name"=>$row[0], "user_name"=>$row[1], "user_pass"=>$row[2]));
		}
	
	echo json_encode(array("server_response"=>$response));
	
	mysqli_close($con);
	
?>
