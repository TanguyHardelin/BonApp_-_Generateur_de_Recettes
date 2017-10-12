<?php
	require "init.php";
	
	$table 		   = "recette";
	$nbrRecipe         = $_POST["nbrRecipe"];
	$nbr_ingredients   = $_POST["nbrIngredients"];
	$cost1		   = $_POST["cout1"];
	$cost2		   = $_POST["cout2"];
	$cost3		   = $_POST["cout3"];
	$nbrRecipe 	   = intval($nbrRecipe);
	$nbr_ingredients   = intval($nbr_ingredients);
	$ingredients	   = array();
	$liste_ingredients = "";

	for ($i=0; $i<$nbr_ingredients; $i++) {
		array_push($ingredients,$_POST["ingredient".$i]);
		$liste_ingredients.=$ingredients[$i];
		$liste_ingredients.=" ";
	}
	
	$liste_ingredients.=" -confiture -alcool";	
		
	//$sql = "select *, match (ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15) against ('$liste_ingredients' IN BOOLEAN MODE) from recette where (match (ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15) against ('$liste_ingredients' IN BOOLEAN MODE)) > 0";
	$sql = "SELECT * FROM (select *, match (ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15) against ('$liste_ingredients' IN BOOLEAN MODE) from $table where (match (ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15) against ('$liste_ingredients' IN BOOLEAN MODE)) > 0 AND cost IN ('$costi1', '$cost2', '$cost3')) AS t1 JOIN (SELECT CEIL(RAND()*(SELECT MAX(id) FROM $table)) AS id) AS t2 WHERE t1.id >= t2.id ORDER BY t1.id ASC LIMIT 1";
		
	$response = array();
	$indice = 0;
	
	while($indice < $nbrRecipe){
		
		$result = mysqli_query($con, $sql);
		$row = mysqli_fetch_array($result);	
		
		$bad_url = "https://images.marmitoncdn.org/recipephotos/multiphoto/73/7384b2af-4ec1-4d71-914d-f01dddc51eb7_normal.jpg";
		
		while (strcmp($row[40], $bad_url)==0){
			$result = mysqli_query($con, $sql);
			$row = mysqli_fetch_array($result);
		}
		
		array_push($response, array("id"=>$row[0], "titre_recette"=>$row[1], "ingredient1"=>$row[2], "ingredient2"=>$row[3], "ingredient3"=>$row[4], "ingredient4"=>$row[5], "ingredient5"=>$row[6], "ingredient6"=>$row[7], "ingredient7"=>$row[8], "ingredient8"=>$row[9], "ingredient9"=>$row[10], "ingredient10"=>$row[11], "ingredient11"=>$row[12], "ingredient12"=>$row[13], "ingredient13"=>$row[14], "ingredient14"=>$row[15], "ingredient15"=>$row[16], "quantiteIngredient1"=>$row[17], "quantiteIngredient2"=>$row[18], "quantiteIngredient3"=>$row[19], "quantiteIngredient4"=>$row[20], "quantiteIngredient5"=>$row[21], "quantiteIngredient6"=>$row[22], "quantiteIngredient7"=>$row[23], "quantiteIngredient8"=>$row[24], "quantiteIngredient9"=>$row[25], "quantiteIngredient10"=>$row[26], "quantiteIngredient11"=>$row[27], "quantiteIngredient12"=>$row[28], "quantiteIngredient13"=>$row[29], "quantiteIngredient14"=>$row[30], "quantiteIngredient15"=>$row[31], "preparation"=>$row[32], "source"=>$row[33], "nbrPersonnes"=>$row[34], "type"=>$row[35], "difficulte"=>$row[36], "cost"=>$row[37], "preparation_time"=>$row[38], "cooking_time"=>$row[39], "image"=>$row[40], "infosIngredient1"=>$row[41], "infosIngredient2"=>$row[42], "infosIngredient3"=>$row[43], "infosIngredient4"=>$row[44], "infosIngredient5"=>$row[45], "infosIngredient6"=>$row[46], "infosIngredient7"=>$row[47], "infosIngredient8"=>$row[48], "infosIngredient9"=>$row[49], "infosIngredient10"=>$row[50], "infosIngredient11"=>$row[51], "infosIngredient12"=>$row[52], "infosIngredient13"=>$row[53], "infosIngredient14"=>$row[54], "infosIngredient15"=>$row[55]));

		$indice+=1;
		}
	
	echo json_encode(array("server_response"=>$response));
	
	mysqli_close($con);

?>
