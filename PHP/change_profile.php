<?php
	require "init.php";
	
	$table 	   = "user_info";
	$id 	   = $_POST["id"];
	$name 	   = $_POST["name"];
	$surname   = $_POST["surname"];
	$user_name = $_POST["user_name"];
	$user_pass = $_POST["user_pass"];
	$email     = $_POST["email"];
	$age 	   = $_POST["age"];
	$budget	   = $_POST["budget"];
	
	$sql_query = "UPDATE $table SET name='$name', surname='$surname', user_name='$user_name', user_pass='$user_pass', email='$email', age=$age, budget='$budget' WHERE id=$id";
	
	if(mysqli_query($con, $sql_query)) {
		echo "Data insertion success.";
		}
	else {
		echo "Data insertion error ".mysqli_error($con);
		}
	
	mysqli_close($con);

?>
