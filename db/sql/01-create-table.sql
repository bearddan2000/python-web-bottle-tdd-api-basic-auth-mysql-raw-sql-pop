DROP TABLE IF EXISTS `beverage`.pop;

CREATE TABLE `beverage`.pop (
	id INT PRIMARY KEY auto_increment,
	name varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `test_chained`.pop;

CREATE TABLE `test_chained`.pop (
	id INT PRIMARY KEY auto_increment,
	name varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `test_raw`.pop;

CREATE TABLE `test_raw`.pop (
	id INT PRIMARY KEY auto_increment,
	name varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `test_api`.pop;

CREATE TABLE `test_api`.pop (
	id INT PRIMARY KEY auto_increment,
	name varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
