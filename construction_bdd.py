# -*- coding: utf-8 -*-

# MODULES
# Modules importés
try: 
	import os
	import sys
	import mysql.connector
	from mysql.connector import errorcode
	from bs4 import BeautifulSoup
	import time
	
except ImportError, err:
	print "Impossible de charger le module. %s" % (err)
	sys.exit(1)


# Données
TABLES 	   = { }
conn       = ""
cursor     = ""
error_file = open("error_file.txt", 'w')
	
config = {
	'user' 		: 'user',
	'password' 	: 'enib29pinfo!!',
	'host' 		: 'localhost',
	'database' 	: 'projetInfo'
	}

TABLES['recette'] =	(
	"CREATE TABLE recette ("
  	"`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"
  	"`titre_recette` char(100) DEFAULT NULL,"
  	"`ingredient1` char(20) DEFAULT NULL,"
  	"`ingredient2` char(20) DEFAULT NULL,"
  	"`ingredient3` char(20) DEFAULT NULL,"
  	"`ingredient4` char(20) DEFAULT NULL,"
  	"`ingredient5` char(20) DEFAULT NULL,"
  	"`ingredient6` char(20) DEFAULT NULL,"
  	"`ingredient7` char(20) DEFAULT NULL,"
  	"`ingredient8` char(20) DEFAULT NULL,"
  	"`ingredient9` char(20) DEFAULT NULL,"
  	"`ingredient10` char(20) DEFAULT NULL,"
  	"`ingredient11` char(20) DEFAULT NULL,"
  	"`ingredient12` char(20) DEFAULT NULL,"
  	"`ingredient13` char(20) DEFAULT NULL,"
  	"`ingredient14` char(20) DEFAULT NULL,"
  	"`ingredient15` char(20) DEFAULT NULL,"
  	"`quantiteIngredient1` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient2` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient3` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient4` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient5` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient6` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient7` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient8` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient9` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient10` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient11` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient12` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient13` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient14` smallint(6) DEFAULT NULL,"
  	"`quantiteIngredient15` smallint(6) DEFAULT NULL,"
  	"`preparation` text,"
  	"`source` char(25) DEFAULT NULL,"
  	"`nbrPersonnes` char(30) DEFAULT NULL,"
  	"PRIMARY KEY (`id`),"
  	"FULLTEXT KEY `full_ingredients` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`,`ingredient11`,`ingredient12`,`ingredient13`,`ingredient14`,`ingredient15`)"
	") ENGINE=InnoDB DEFAULT CHARSET=utf8;")


##################################################################
########################## PARSING HTML ##########################
##################################################################


def deleteElements(txt):
	val=False
	txt_final=""
	
	for i in txt:
		if not val:
			if i == "<":
				val = True
				pass
			else:
				txt_final += i
		elif val:
			if i ==">":
				val = False
				pass
	
	return txt_final


def deleteCharacter(txt, character):
	txt_final = ""
	for i in txt:
		if i==character:
			pass
		else:
			txt_final+=i
	
	return txt_final


def recuperation_infos():
	global cursor, conn, config, error_file
	
	try:
		fichier = open("page.html").read()
		
		soup =  BeautifulSoup(fichier, "lxml")
	
		titre			  = ""
		quantites		  = ""
		recette			  = ""
		type_of_recipe	  = ""
		difficulte		  = ""
		cost			  = ""
		preparation_time  = ""
		cooking_time	  = ""
		image			  = ""
		ingredients		  = list()
		infos_ingredients = list()
		
		titre = fichier.split("<title>")[1].split(" :")[0].split("\n")[1].split("\t")[1]
		
		recette = deleteElements(fichier.split('<div class="m_content_recette_todo">')[1].split("</div>")[0])
		recette = deleteCharacter(recette, '"')
		
		ingredients       = fichier.split('"recipeIngredients": "')[1].split('",')[0].split(",")
		nbrPersonnes      = fichier.split('"recipeServings": ')[1].split('\r\n  }')[0]
		type_of_recipe    = fichier.split('"recipeType": "')[1].split('",')[0]
		difficulte        = fichier.split('"recipeDifficulty": "')[1].split('",')[0]
		cost              = fichier.split('"recipeCost": "')[1].split('",')[0]
		preparation_time  = fichier.split('"recipePreparationTime": ')[1].split(',')[0]
		cooking_time      = fichier.split('"recipeCookingTime": ')[1].split(',')[0]
		infos_ingredients = fichier.split('"recipeIngredient": [')[1].split("],")[0]
		
		infos_ingredients = infos_ingredients.split('"')
		
		infos = list()
		for i in range(1, len(infos_ingredients)-1):
			test = True
			for j in range(len(infos_ingredients[i])):
				if infos_ingredients[i][j]==",":
					test = False
					break
			if test:
				infos.append(infos_ingredients[i])
		
		for i in range(len(ingredients) - len(infos)):
			infos.append("")
		
		try :
			image = fichier.split('class="m_pinitimage" src="')[1].split('" alt=')[0]
		except IndexError:
			try :
				image = fichier.split("""<img class="photo m_pinitimage" src='""")[1].split("'")[0]
			except IndexError:
				try:
					image = fichier.split("""m_pinitimage" src='""")[1].split("'")[0]
				except IndexError:
					image = "https://images.marmitoncdn.org/recipephotos/multiphoto/73/7384b2af-4ec1-4d71-914d-f01dddc51eb7_normal.jpg"
		
		cmd = ""
	
		if len(ingredients)==1:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1) VALUES (NULL, "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0])
		
		elif len(ingredients)==2:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2) VALUES (NULL, "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1])
		
		elif len(ingredients)==3:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2])
		
		elif len(ingredients)==4:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3])
		
		elif len(ingredients)==5:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4])
		
		elif len(ingredients)==6:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5])
		
		elif len(ingredients)==7:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6])
		
		elif len(ingredients)==8:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7])
		
		elif len(ingredients)==9:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8])
		
		elif len(ingredients)==10:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9, infosIngredient10) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8], infos[9])
		
		elif len(ingredients)==11:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9, infosIngredient10, infosIngredient11) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], ingredients[10], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8], infos[9], infos[10])
		
		elif len(ingredients)==12:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9, infosIngredient10, infosIngredient11, infosIngredient12) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], ingredients[10], ingredients[11], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8], infos[9], infos[10], infos[11])
		
		elif len(ingredients)==13:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9, infosIngredient10, infosIngredient11, infosIngredient12, infosIngredient13) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], ingredients[10], ingredients[11], ingredients[12], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8], infos[9], infos[10], infos[11], infos[12])
		
		elif len(ingredients)==14:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9, infosIngredient10, infosIngredient11, infosIngredient12, infosIngredient13, infosIngredient14) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], ingredients[10], ingredients[11], ingredients[12], ingredients[13], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8], infos[9], infos[10], infos[11], infos[12], infos[13])
		
		elif len(ingredients)==15:
			cmd = """INSERT INTO %s (id, titre_recette, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15, preparation, source, nbrPersonnes, type, difficulte, cost, preparation_time, cooking_time, image, infosIngredient1, infosIngredient2, infosIngredient3, infosIngredient4, infosIngredient5, infosIngredient6, infosIngredient7, infosIngredient8, infosIngredient9, infosIngredient10, infosIngredient11, infosIngredient12, infosIngredient13, infosIngredient14, infosIngredient15) VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Marmiton", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");""" % ("recette", titre, ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], ingredients[10], ingredients[11], ingredients[12], ingredients[13], ingredients[14], recette, nbrPersonnes, type_of_recipe, difficulte, cost, preparation_time, cooking_time, image, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6], infos[7], infos[8], infos[9], infos[10], infos[11], infos[12], infos[13], infos[14])
		
		cursor.execute(cmd)
		
		conn.commit()
		
		return True
	
	except UnicodeDecodeError:
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur d'encodage.\n")
		error_file.flush()
		return False
	except IndexError:
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur d'index.\n")
		error_file.flush()
		return False
	except TypeError:
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Pas assez d'arguments pour le format du str.\n")
		error_file.flush()
		return False
	except mysql.connector.errors.ProgrammingError:
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL -> problème de syntaxe pour " + str(len(ingredients)) +".\n")
		error_file.flush()
		return False
	except mysql.connector.errors.DataError:
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL -> La donnée est trop longue pour la colonne.\n")
		error_file.flush()
		return False
	except:
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur inconnue.\n")
		error_file.flush()
		return False


def recup_lien_ingredients(lettre):
	global cursor, conn, error_file
	os.system("torsocks wget -q http://www.marmiton.org/recettes/recettes-index.aspx?letter="+lettre+" -O index_ingredient.html")
	liste_url=[]
	fichier_index_ingredient=open("index_ingredient.html",'r')
	texte_fichier=fichier_index_ingredient.read()
	
	# Vérification si on n'est pas bloqué
	soup =  BeautifulSoup(texte_fichier, "lxml")
	titre = soup.title.text.split('\t')[1].encode('utf-8')
	
	if titre=="Trop de connexions":
		print "On est bloqué, nik tou"
		
		error_file.write("Blocage effectué par le site de Marmiton à " + time.strftime("%H:%M:%S") + " le " + time.strftime("%A %d %B %Y") + ".\nFermeture du programme.")
		
		error_file.close()
		cursor.close()
		conn.close()
		
		sys.exit(1)
	
	my_texte=texte_fichier.split('<ul class="m-lsting-ing">')[1].split("</ul>")[0]

	my_texte=my_texte.split("href=\"")
	for j in range (len(my_texte)):
		if(j!=0):
			liste_url.append(my_texte[j].split("\"")[0])

	return liste_url


def change_ip():
	global error_file
	os.system("killall -HUP tor")
	new_ip = os.popen("torsocks wget -qO- http://ipecho.net/plain 2> /dev/null ; echo", 'r', 1).read().split('\n')[0]
	print("\n\n------------------\nWARNING: IP CHANGED, NEW IP --> " + new_ip + " \n------------------\n\n")
	error_file.write("\n\n" + time.strftime(">> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: IP changed, now ip is: " + new_ip + ".\n\n")
	error_file.flush()


def recup_recette(ingredient, liste_recette):
	print("Ingredient: "+ingredient)
	os.system("torsocks wget -q http://www.marmiton.org"+ingredient+" -O page_ingredient.html")
	liste_url = []
	my_texte  = ""
	try:
		fichier_index_ingredient = open("page_ingredient.html",'r')
		texte_fichier = fichier_index_ingredient.read()
		my_texte = texte_fichier.split("<ul class=\"m-lsting-recipe\">")[1].split("</ul>")[0]

		my_texte = my_texte.split('href=\"')
	except:
		pass
	else:
		for j in range (len(my_texte)):
			if(j!=0):
				my_texte[j] = my_texte[j].split("\"")[0]
				
				# Récupération de la page
			
				os.system("torsocks wget -q http://www.marmiton.org"+my_texte[j]+" -O page.html")
			
				if recuperation_infos():
			
					# Mettre ici les fonctions de récupération des informations
					#print("Nouvelle recette "+ my_texte[j])
			
					liste_recette.append(my_texte[j])
			
					print("Il y a "+str(len(liste_recette))+" recettes pour l'instant.\n")
			
					if (len(liste_recette)%100==0) : change_ip()
			

def lancement_recuperation():
	alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	liste_recette=[]
	if 1==2:
		pass
	else:
		for j in range(len(alphabet)):
			# On récupère pour la lettre selectionnée la liste d'ingrédients
			liste_ingredients = recup_lien_ingredients(alphabet[j]);
			# Pour chaque ingrédient on va récupérer toutes les recettes
			for i in range(len(liste_ingredients)):
				recup_recette(liste_ingredients[i], liste_recette)
		
		print("Il y a "+str(len(liste_recette))+" recettes au total\n")


#####################################################################
########################## BASE DE DONNEES ##########################
#####################################################################


def create_database(DB_NAME):
	global cursor
	
	try:
		cursor.execute(
			"CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	except mysql.connector.Error as err:
		print "Failed creating database: {}".format(err)
		error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL -> problème de création de la base de données.\n")
		exit(1)


def main():
	global cursor, conn, config, error_file
	
	error_file.write("\n\n------------------------------------------------------------\n")	
	error_file.write(time.strftime(">>> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Lancement du programme.\n\n")
	error_file.flush()
	
	if 1==2:
		pass
	else:
		try:
			conn = mysql.connector.connect(host=config['host'], user=config['user'], password=config['password'])
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print "Something is wrong with your username or password."
				error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL : problème de connexion dû au nom d'utilisateur ou au mot de passe.\n")
				error_file.close()
				exit(1)
			else:
				print err
				error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL : " + str(err) +".\n")
				error_file.close()
				exit(1)
		else:
			cursor = conn.cursor(buffered=True)
		
		try:
			if(type(conn)!=str):
				conn.database = config['database']
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				create_database(cursor)
				conn.database = config['database']
			else:
				print(err)
				error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL : " + str(err) +".\n")
				error_file.close()
				exit(1)
		
		for name, ddl in TABLES.iteritems():
			try:
				print "Creating table {}:".format(name),
				cursor.execute(ddl)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print "Table already exists."
				else:
					print err.msg
					error_file.write(time.strftime("> %A %d %B %Y ") + "[" + time.strftime("%H:%M:%S") + "]: Erreur SQL : " + str(err.msg) +".\n")
					error_file.flush()
			else:
				print "OK"
		
		lancement_recuperation()
		#recuperation_infos()
	  	
	  	error_file.close()
		cursor.close()
		conn.close()


# Lancement du programme
if __name__ == '__main__':
	main()



















