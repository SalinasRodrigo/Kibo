CREATE DATABASE  IF NOT EXISTS `proyecto_grupal_bd` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `proyecto_grupal_bd`;
-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: proyecto_grupal_bd
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

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
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'TVs','2023-03-08','2023-03-08'),(2,'Speakers','2023-03-08','2023-03-08'),(3,'Monitor','2023-03-09','2023-03-09'),(4,'Smartphones','2023-03-12','2023-03-12'),(5,'Auriculares','2023-03-14','2023-03-14'),(6,'Notebooks','2023-03-16','2023-03-16');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas`
--

DROP TABLE IF EXISTS `marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marcas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas`
--

LOCK TABLES `marcas` WRITE;
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` VALUES (1,'Xiaomi','2023-03-08','2023-03-08'),(2,'Samsung','2023-03-08','2023-03-08'),(3,'HP','2023-03-08','2023-03-08'),(4,'LG','2023-03-09','2023-03-09'),(5,'JBL','2023-03-10','2023-03-10'),(6,'DELL','2023-03-15','2023-03-15');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `descuento` tinyint(4) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `stock_ideal` int(11) DEFAULT NULL,
  `stock_disponible` int(11) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  `marca_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_productos_marcas1_idx` (`marca_id`),
  KEY `fk_productos_categorias1_idx` (`categoria_id`),
  CONSTRAINT `fk_productos_categorias1` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_marcas1` FOREIGN KEY (`marca_id`) REFERENCES `marcas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Xiaomi Mi TV Smart Q1 75” UHD','Procesador y almacenamiento\r\n\r\nMediaTek MT9611\r\nCPU: CPU: Cuatro núcleos, hasta 1,5 GHz\r\nGPU: Mali G52 MP2\r\nRAM: 2GB\r\nStorage: 32GB',12200000,0,'/static/files/1.jpg',5,5,'2023-03-08','2023-03-11',1,1),(2,'Speaker Jbl Flip 5 Azul','12 horas de música continua.\r\n\r\nCertificado IPX7.\r\n\r\nBatería mejorada 4800 mAh.\r\n\r\nPuerto USB-C.\r\n\r\nResiste al agua y flota',745000,0,'/static/files/2.jpg',10,10,'2023-03-10','2023-03-10',5,2),(3,'Samsung Galaxy A04 SM-A045M/DS Dual 64 GB - Black','Tamaño de pantalla: 6.5\" PLS LCD\r\nResolución: 720 x 1600\r\nCámara principal: Dual 50MP + 2MP\r\nCámara frontal: 5MP',954980,0,'/static/files/3.jpg',3,3,'2023-03-12','2023-03-12',2,4),(4,'Xiaomi Redmi Note 10S Dual 128 GB - Azul','Tamaño de Pantalla: 6.43\'\'\r\nResolución: 1080 x 2400\r\nCámara principal: Cuádruple 64MP + 8MP + 2MP + 2MP\r\nCámara frontal: 13MP\r\nMemoria interna: 128 GB',1500177,0,'/static/files/4.jpg',6,6,'2023-03-12','2023-03-12',1,4),(5,'Auricular JBL T110','El auricular JBL T110 es ligero, cómodo y compacto. Debajo de la carcasa duradera del auricular, un par de controladores de 9 mm que reproducen el sonido JBL Pure Bass que enfatiza los graves profundos. Además, el control remoto de un solo botón en un cable plano sin enredos le permite controlar la reproducción de música, así como llamadas sobre la marcha con un micrófono incorporado.',48000,0,'/static/files/5.jpg',5,5,'2023-03-14','2023-03-14',5,5),(6,'Xiaomi Poco M5 Dual','La nueva Xiaomi Poco M5 con la pantalla 6.58\'\', cuenta con cámara principal triple de 50MP + 2MP + 2MP y la cámara frontal de 5MP, su diseño súper elegante se fusiona en total armonía con su potente rendimiento. Batería de 5.000mAh.',1355000,0,'/static/files/6.jpg',7,7,'2023-03-16','2023-03-16',1,4),(7,'Auricular Xiaomi 1More HSEJ03JY','El auricular Xiaomi Mi 1More HSEJ03JY es compacto y brinda versatilidad al usuario. Se puede usar con diferentes dispositivos: como computadoras portátiles, teléfonos inteligentes, reproductores de MP3, tabletas, entre otros. Tiene un diseño moderno y cómodo y se puede usar mientras hace ejercicio o simplemente escucha música mientras estudia o trabaja.',40000,0,'/static/files/7.jpg',3,3,'2023-03-16','2023-03-16',1,4),(8,'Speaker Xiaomi MDZ-36-DB','El speaker Xiaomi Mi Portable MDZ-36-DB cuenta con diseño compacto y resistente. A pesar de su tamaño cuenta con una potencia de 16 W ideal para campamentos o aventuras al aire libre. Posee conectividad bluetooth 5.0, Jack 3.5 mm y la tecnología TWS, a través de la cual es posible conectar otro speaker con TWS y aumentar la potencia sonora.',284000,0,'/static/files/8.jpg',15,15,'2023-03-16','2023-03-16',1,2),(9,'Monitor LED Samsung LT24H315HLB 24\" HD','Samsung TH315S cuenta con una plataforma Smart Hub, una portal muy avanzado a través de la cual puedes explorar una gran variedad de aplicaciones, videoclips, programas de televisión y publicaciones sociales. Con ella, el acceso a tus medios favoritos es más rápido y sencillo.',1442648,0,'/static/files/9.jpg',15,15,'2023-03-16','2023-03-16',2,3),(10,'Monitor LED LG UltraGear 32GN600 31.5\"','El monitor LG UltraGear 32GN600 para juegos tiene un diseño elegante con una velocidad ultrarrápida de 165Hz les permite a los jugadores ver rápidamente el próximo cuadro y hace que la imagen aparezca con fluidez con resolución QHD de 2560 x 1440 para brindar la mejor experiencia de juego.',2920000,0,'/static/files/10.jpg',6,6,'2023-03-16','2023-03-16',4,3),(11,'Notebook Dell Inspiron 15 3501 15.6\"','La notebook Dell Inspiron 15 3501 tiene una pantalla de 15.6\" con resolución HD (1366 x 768 p) que ofrece imágenes más nítidas y colores más brillantes. El dispositivo está equipado con un procesador Intel Core i3 de undécima generación para un rendimiento excepcional. Incorpora 1 TB de almacenamiento HDD y 4 GB de RAM DDR4.',3850000,0,'/static/files/11.jpg',7,7,'2023-03-16','2023-03-16',6,6),(12,'Notebook HP ProBook 635 G8 13.3\"','La notebook HP ProBook 635 Aero G8 tiene una pantalla IPS de 13.3\" con resolución Full HD (1920 x 1080p) que ofrece imágenes nítidas y colores vivos. Está equipada con un procesador AMD Ryzen 5 5600U Hexa-Core para un rendimiento superior, memoria de almacenamiento SSD M.2 NVMe de 256 GB y memoria RAM de 16 GB DDR4, ideal para trabajar, estudiar o divertirse.',5302000,0,'/static/files/12.jpg',10,10,'2023-03-16','2023-03-16',3,6),(13,'Notebook HP 15Z-EF2000 15.6\"','La notebook HP 15Z-EF2000 tiene una pantalla IPS de 15.6\" con resolución Full HD (1920 x 1080p) que ofrece imágenes nítidas y colores más vivos. Está equipado con un procesador AMD Ryzen 7 5700U para un rendimiento superior, 512 GB de almacenamiento SSD M.2 NVMe y 12 GB de RAM, ideal para trabajar, estudiar o jugar. ',5752000,0,'/static/files/13.jpg',20,20,'2023-03-16','2023-03-16',3,6),(14,'Notebook Dell Latitude 5430 14\"','La notebook Latitude 5430 de 14\" de Dell ofrece a los profesionales y estudiantes una herramienta de rendimiento de alto nivel. Está equipada con un procesador Intel Core i7-1265U de 10 núcleos, 16 GB de memoria RAM DDR4 de 3200 MHz y 256 GB de almacenamiento en una unidad de estado sólido M.2. ',10178000,0,'/static/files/14.jpg',12,12,'2023-03-16','2023-03-16',6,6),(15,'Televisor Smart LED LG 43LM6370','Los televisores LG Full HD ofrecen imágenes más precisas con una resolución sorprendente y colores vivos.Los televisores LG FHD están hechos para impresionar con una calidad de imagen clara que es dos veces mejor que la HD. Y con Dynamic Color y Active HDR, todo su contenido favorito será más realista y vibrante.',2256000,0,'/static/files/15.jpg',5,5,'2023-03-16','2023-03-16',4,1);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `nivel` tinyint(4) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'German','González','german.gonzalez@gmail.com','$2b$12$r9J6hlahNbPXEcxzCzlTZe5keYud4Ggdk.M/6GHIQaRmzYOpTeKxK','Calle Jaime San Just','0992843527',0,'2023-03-14','2023-03-14'),(2,'','Molinas','tadeo25.molinas@gmail.com','$2b$12$DrvSmitwBCdJjbAm2lK3MOmI.z57Dpx3iErvV4R3uqAmpRws9nTj6','Calle Caacupe','0992843527',1,'2023-03-14','2023-03-15');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_cab`
--

DROP TABLE IF EXISTS `ventas_cab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ventas_cab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `total` varchar(45) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_VentasCab_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_VentasCab_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_cab`
--

LOCK TABLES `ventas_cab` WRITE;
/*!40000 ALTER TABLE `ventas_cab` DISABLE KEYS */;
INSERT INTO `ventas_cab` VALUES (1,'2023-03-12 12:34:17','2444980',1),(2,'2023-03-14 08:37:10','2654960',1),(3,'2023-03-14 09:04:56','1500177',1),(4,'2023-03-14 21:49:29','1644177',1),(5,'2023-03-15 21:16:14','48000',1),(6,'2023-03-15 21:27:45','48000',1);
/*!40000 ALTER TABLE `ventas_cab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_det`
--

DROP TABLE IF EXISTS `ventas_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ventas_det` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) DEFAULT NULL,
  `subtotal` int(11) DEFAULT NULL,
  `producto_id` int(11) NOT NULL,
  `venta_cab_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_VentaDet_productos1_idx` (`producto_id`),
  KEY `fk_VentaDet_VentaCab1_idx` (`venta_cab_id`),
  CONSTRAINT `fk_VentaDet_VentaCab1` FOREIGN KEY (`venta_cab_id`) REFERENCES `ventas_cab` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_VentaDet_productos1` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_det`
--

LOCK TABLES `ventas_det` WRITE;
/*!40000 ALTER TABLE `ventas_det` DISABLE KEYS */;
INSERT INTO `ventas_det` VALUES (1,2,1490000,2,1),(2,1,954980,3,1),(3,1,745000,2,2),(4,2,1909960,3,2),(5,1,1500177,4,3),(6,3,144000,5,4),(7,1,1500177,4,4),(8,1,48000,5,5),(9,1,48000,5,6);
/*!40000 ALTER TABLE `ventas_det` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-16  8:46:07
