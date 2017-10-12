<?php
	require "init.php";
	
	$table = "user_info";
	$name = $_POST["name"];
	$surname = $_POST["surname"];
	$user_name = $_POST["user_name"];
	$user_pass = $_POST["user_pass"];
	$email = $_POST["email"];
	$age = $_POST["age"];
	$budget = $_POST["budget"];	
	$sql_query = "INSERT IGNORE INTO $table VALUES (id, '$name', '$surname', '$user_name', '$user_pass', '$email', $age, '$budget')";
	
	if(mysqli_query($con, $sql_query)) {
		echo "Data insertion success.";
		}
	else {
		echo "Data insertion error ".mysqli_error($con);
		}
	
	mysqli_close($con);

?>
