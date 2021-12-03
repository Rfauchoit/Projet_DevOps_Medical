-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: medical
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `adresse`
--

LOCK TABLES `adresse` WRITE;
/*!40000 ALTER TABLE `adresse` DISABLE KEYS */;
INSERT INTO `adresse` VALUES (1,'45787775','Allee des Isabelle',60200,'Bordeaux'),(2,'2','allee',60200,'compiegne'),(3,'14','rrr',20,'fg'),(4,'14','hdfhdf',60000,'fdjdghjgdh'),(5,'47','ff',20,'fsd'),(6,'11','Momo',60,'Momo'),(7,'50','r',60,'r'),(8,'45','Mannequin',60200,'Compiegne'),(9,'458','Allee des infimiers',60200,'Bordeaux'),(10,'45501','Allee des infimiers',60200,'Bordeaux'),(11,'4578777','Allee des infimiers',60200,'Bordeaux'),(12,'45','eee',60200,'fdsff'),(13,'45','rue',60,'ville'),(14,'8','Allee des infimiers',60200,'Bordeaux'),(15,'75','Allee des infimiers',60200,'Bordeaux'),(16,'800','Allee des infimiers',60200,'Bordeaux'),(17,'0','0',0,'0'),(18,'900','Allee des infimiers',60200,'Bordeaux'),(19,'15','Zoubida',59100,'Zoubida'),(20,'45','Randy',59640,'Randy'),(21,'500','Allee des infimiers',60200,'Bordeaux'),(22,'85','Semifir',59100,'Semifir'),(23,'45','Test',75000,'Test'),(24,'45','zoubi',62,'ffff'),(25,'50','Rue',60,'Ville'),(26,'500','Rue',60,'Ville');
/*!40000 ALTER TABLE `adresse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `deplacement`
--

LOCK TABLES `deplacement` WRITE;
/*!40000 ALTER TABLE `deplacement` DISABLE KEYS */;
INSERT INTO `deplacement` VALUES (11,22,'2021-12-10 00:00:00',1500),(12,88,'2021-12-16 00:00:00',20),(13,88,'2021-12-23 00:00:00',20);
/*!40000 ALTER TABLE `deplacement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `infirmier`
--

LOCK TABLES `infirmier` WRITE;
/*!40000 ALTER TABLE `infirmier` DISABLE KEYS */;
/*!40000 ALTER TABLE `infirmier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (22,1,NULL,'Cyriak','Inconnu','2021-12-23','f',52552542),(23,2,NULL,'Isabelle','Isabelle','2021-12-04','mascuFeminin',5082654655),(61,NULL,NULL,'Romy','Romy','2021-12-17','f',205555),(64,2,NULL,'afoutni','zoubida','2021-12-23','f',25752753),(65,NULL,NULL,'Randy','Randy','1937-07-02','Masculin',5055058565),(66,2,NULL,'Randy','Lony','2004-12-16','Inconnu',524588522),(69,2,NULL,'Tommy','Tommy','2021-12-17','f',5775785785),(87,19,NULL,'Jean','Dupont','2021-12-01','Masculin',20202020121),(88,20,NULL,'Dupont','Jean','2021-12-24','feminin',50222);
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-03 12:20:52
