-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com    Database: mayankdb
-- ------------------------------------------------------
-- Server version	5.6.27-log

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
-- Table structure for table `Daily_Rental`
--

DROP TABLE IF EXISTS `Daily_Rental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Daily_Rental` (
  `Rent_Id` int(10) NOT NULL AUTO_INCREMENT,
  `Cust_Id` int(10) DEFAULT NULL,
  `Vehicle_Id` int(10) DEFAULT NULL,
  `Location` varchar(20) DEFAULT NULL,
  `No_Of_Days` int(4) DEFAULT NULL,
  `Start_Date` date DEFAULT NULL,
  `Return_Date` date DEFAULT NULL,
  `Amount_Due` float(9,3) DEFAULT NULL,
  `Booking_Status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Rent_Id`),
  KEY `Vehicle_Id` (`Vehicle_Id`),
  KEY `Cust_Id` (`Cust_Id`),
  CONSTRAINT `Daily_Rental_ibfk_1` FOREIGN KEY (`Vehicle_Id`) REFERENCES `Car_Details` (`Vehicle_Id`),
  CONSTRAINT `Daily_Rental_ibfk_2` FOREIGN KEY (`Cust_Id`) REFERENCES `Customer` (`Cust_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Daily_Rental`
--

LOCK TABLES `Daily_Rental` WRITE;
/*!40000 ALTER TABLE `Daily_Rental` DISABLE KEYS */;
/*!40000 ALTER TABLE `Daily_Rental` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-12 17:28:17
