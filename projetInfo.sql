-- MySQL dump 10.13  Distrib 5.7.18, for Linux (x86_64)
--
-- Host: localhost    Database: projetInfo
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recette`
--

DROP TABLE IF EXISTS `recette`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recette` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `titre_recette` char(100) DEFAULT NULL,
  `ingredient1` char(30) DEFAULT NULL,
  `ingredient2` char(30) DEFAULT NULL,
  `ingredient3` char(30) DEFAULT NULL,
  `ingredient4` char(30) DEFAULT NULL,
  `ingredient5` char(30) DEFAULT NULL,
  `ingredient6` char(30) DEFAULT NULL,
  `ingredient7` char(30) DEFAULT NULL,
  `ingredient8` char(30) DEFAULT NULL,
  `ingredient9` char(30) DEFAULT NULL,
  `ingredient10` char(30) DEFAULT NULL,
  `ingredient11` char(30) DEFAULT NULL,
  `ingredient12` char(30) DEFAULT NULL,
  `ingredient13` char(30) DEFAULT NULL,
  `ingredient14` char(30) DEFAULT NULL,
  `ingredient15` char(30) DEFAULT NULL,
  `quantiteIngredient1` smallint(6) DEFAULT NULL,
  `quantiteIngredient2` smallint(6) DEFAULT NULL,
  `quantiteIngredient3` smallint(6) DEFAULT NULL,
  `quantiteIngredient4` smallint(6) DEFAULT NULL,
  `quantiteIngredient5` smallint(6) DEFAULT NULL,
  `quantiteIngredient6` smallint(6) DEFAULT NULL,
  `quantiteIngredient7` smallint(6) DEFAULT NULL,
  `quantiteIngredient8` smallint(6) DEFAULT NULL,
  `quantiteIngredient9` smallint(6) DEFAULT NULL,
  `quantiteIngredient10` smallint(6) DEFAULT NULL,
  `quantiteIngredient11` smallint(6) DEFAULT NULL,
  `quantiteIngredient12` smallint(6) DEFAULT NULL,
  `quantiteIngredient13` smallint(6) DEFAULT NULL,
  `quantiteIngredient14` smallint(6) DEFAULT NULL,
  `quantiteIngredient15` smallint(6) DEFAULT NULL,
  `preparation` text,
  `source` char(25) DEFAULT NULL,
  `nbrPersonnes` char(30) DEFAULT NULL,
  `type` char(20) DEFAULT NULL,
  `difficulte` char(25) DEFAULT NULL,
  `cost` char(25) DEFAULT NULL,
  `preparation_time` int(11) DEFAULT NULL,
  `cooking_time` int(11) DEFAULT NULL,
  `image` char(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ind_1_ing` (`ingredient1`),
  FULLTEXT KEY `ind_2_ing` (`ingredient1`,`ingredient2`),
  FULLTEXT KEY `ind_3_ing` (`ingredient1`,`ingredient2`,`ingredient3`),
  FULLTEXT KEY `ind_4_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`),
  FULLTEXT KEY `ind_5_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`),
  FULLTEXT KEY `ind_6_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`),
  FULLTEXT KEY `ind_7_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`),
  FULLTEXT KEY `ind_8_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`),
  FULLTEXT KEY `ind_9_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`),
  FULLTEXT KEY `ind_10_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`),
  FULLTEXT KEY `ind_11_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`,`ingredient11`),
  FULLTEXT KEY `ind_12_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`,`ingredient11`,`ingredient12`),
  FULLTEXT KEY `ind_13_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`,`ingredient11`,`ingredient12`,`ingredient13`),
  FULLTEXT KEY `ind_14_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`,`ingredient11`,`ingredient12`,`ingredient13`,`ingredient14`),
  FULLTEXT KEY `ind_15_ing` (`ingredient1`,`ingredient2`,`ingredient3`,`ingredient4`,`ingredient5`,`ingredient6`,`ingredient7`,`ingredient8`,`ingredient9`,`ingredient10`,`ingredient11`,`ingredient12`,`ingredient13`,`ingredient14`,`ingredient15`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recette`
--

LOCK TABLES `recette` WRITE;
/*!40000 ALTER TABLE `recette` DISABLE KEYS */;
/*!40000 ALTER TABLE `recette` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `surname` char(20) DEFAULT NULL,
  `user_name` char(20) DEFAULT NULL,
  `user_pass` char(20) DEFAULT NULL,
  `email` char(50) DEFAULT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ind_user_name` (`user_name`),
  FULLTEXT KEY `ind_full_name` (`name`),
  FULLTEXT KEY `ind_full_surname` (`surname`),
  FULLTEXT KEY `ind_full_name_surname` (`name`,`surname`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,'yy','yy','yy','yy','yy',15),(2,'ya','ya','ya','ya','ya',15),(3,'yo','yo','yo','yo','yo',15),(4,'yi','yi','yi','yi','yi',15),(5,'yu','yu','yu','yu','yu',15),(7,'ye','ye','ye','ye','ye',15),(9,'etienne','landure','truc','wech','jhrfejr@truc.com',15),(12,'etienne','landure','machin','wech','jhrfejr@truc.com',15),(13,'a','a','a','a','a',15),(16,'a','a','b','a','a',15),(18,'a','a','c','a','a',15);
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-09 11:11:06
