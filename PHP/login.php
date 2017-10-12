<?php
	require "init.php";
	
	$table = "user_info";
	$user_name = $_POST["login_name"];
	$user_pass = $_POST["login_pass"];
	
	$sql = "SELECT * FROM $table WHERE user_name LIKE '$user_name' AND user_pass LIKE '$user_pass'";
	
	$result = mysqli_query($con, $sql);
	
	$response = array();
	
	$row = mysqli_fetch_array($result);
	
	array_push($response, array("id"=>$row[0], "name"=>$row[1], "surname"=>$row[2], "user_name"=>$row[3], "user_pass"=>$row[4], "email"=>$row[5], "age"=>$row[6], "budget"=>$row[7]));
	
	echo json_encode(array("server_response"=>$response));
	
	mysqli_close($con);

?>
