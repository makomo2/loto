CREATE DATABASE `loto`;
USE `loto`;

CREATE TABLE `loto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kind` varchar(10) NOT NULL,
  `times` int NOT NULL,
  `date` date NOT NULL,
  `numbers` varchar(50) NOT NULL,
  `bonus` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
