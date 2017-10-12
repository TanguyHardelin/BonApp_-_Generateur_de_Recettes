<?php
	require "init.php";
	
	$table = "recette";
	$ingredient1 = $_POST["ingredient1"];
	$ingredient2 = $_POST["ingredient2"];
	$ingredient3 = $_POST["ingredient3"];
	$ingredient4 = $_POST["ingredient4"];
	$ingredient5 = $_POST["ingredient5"];
	$ingredient6 = $_POST["ingredient6"];
	$ingredient7 = $_POST["ingredient7"];
	$ingredient8 = $_POST["ingredient8"];
	$ingredient9 = $_POST["ingredient9"];
	$ingredient10 = $_POST["ingredient10"];
	$ingredient11 = $_POST["ingredient11"];
	$ingredient12 = $_POST["ingredient12"];
	$ingredient13 = $_POST["ingredient13"];
	$ingredient14 = $_POST["ingredient14"];
	$ingredient15 = $_POST["ingredient15"];
	$quantiteIngredient1 = $_POST["quantiteIngredient1"];
	$quantiteIngredient2 = $_POST["quantiteIngredient2"];
	$quantiteIngredient3 = $_POST["quantiteIngredient3"];
	$quantiteIngredient4 = $_POST["quantiteIngredient4"];
	$quantiteIngredient5 = $_POST["quantiteIngredient5"];
	$quantiteIngredient6 = $_POST["quantiteIngredient6"];
	$quantiteIngredient7 = $_POST["quantiteIngredient7"];
	$quantiteIngredient8 = $_POST["quantiteIngredient8"];
	$quantiteIngredient9 = $_POST["quantiteIngredient9"];
	$quantiteIngredient10 = $_POST["quantiteIngredient10"];
	$quantiteIngredient11 = $_POST["quantiteIngredient11"];
	$quantiteIngredient12 = $_POST["quantiteIngredient12"];
	$quantiteIngredient13 = $_POST["quantiteIngredient13"];
	$quantiteIngredient14 = $_POST["quantiteIngredient14"];
	$quantiteIngredient15 = $_POST["quantiteIngredient15"];
	$nbrRecipe = $_POST["nbrRecipe"];
	
	$sql = "SELECT * FROM $table AS t1 JOIN (SELECT CEIL(RAND()*(SELECT MAX(id) FROM $table)) AS id) AS t2 WHERE t1.id >= t2.id AND MATCH(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15) AGAINST('$ingredient1', '$ingredient2', '$ingredient3', '$ingredient4', '$ingredient5', '$ingredient6', '$ingredient7', '$ingredient8', '$ingredient9', '$ingredient10', '$ingredient11', '$ingredient12', '$ingredient13', '$ingredient14', '$ingredient15') ORDER BY t1.id ASC LIMIT 1";
	
	$response = array();
	
	for ($i=0; $i<$nbrRecipe; $i++) {
		$result = mysqli_query($con, $sql);
		
		$row = mysqli_fetch_array($result);
		
		array_push($response, array("id"=>$row[0], "titre_recette"=>$row[1], "ingredient1"=>$row[2], "ingredient2"=>$row[3], "ingredient3"=>$row[4], "ingredient4"=>$row[5], "ingredient5"=>$row[6], "ingredient6"=>$row[7], "ingredient7"=>$row[8], "ingredient8"=>$row[9], "ingredient9"=>$row[10], "ingredient10"=>$row[11], "ingredient11"=>$row[12], "ingredient12"=>$row[13], "ingredient13"=>$row[14], "ingredient14"=>$row[15], "ingredient15"=>$row[16], "quantiteIngredient1"=>$row[17], "quantiteIngredient2"=>$row[18], "quantiteIngredient3"=>$row[19], "quantiteIngredient4"=>$row[20], "quantiteIngredient5"=>$row[21], "quantiteIngredient6"=>$row[22], "quantiteIngredient7"=>$row[23], "quantiteIngredient8"=>$row[24], "quantiteIngredient9"=>$row[25], "quantiteIngredient10"=>$row[26], "quantiteIngredient11"=>$row[27], "quantiteIngredient12"=>$row[28], "quantiteIngredient13"=>$row[29], "quantiteIngredient14"=>$row[30], "quantiteIngredient15"=>$row[31], "preparation"=>$row[32], "source"=>$row[33], "nbrPersonnes"=>$row[34], "type"=>$row[35], "difficulte"=>$row[36], "cost"=>$row[37], "preparation_time"=>$row[38], "cooking_time"=>$row[39], "image"=>$row[40]));
		}
	
	echo json_encode(array("server_response"=>$response));
	
	mysqli_close($con);

?>
