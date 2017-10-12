<?php
	require "init.php";
	
	$table = "recette";
	
	$sql_query = "SELECT id FROM $table WHERE id=(SELECT MAX(id) FROM $table);";
	
	$result="";
	if($result = mysqli_query($con, $sql_query)) {
		$row = mysqli_fetch_array($result);
		$nbr_recettes = $row['id'];
		echo "<h1>Pour l'instant il y a $nbr_recettes recettes.</h1>\n";
	}
	
	mysqli_close($con);
	
?>
