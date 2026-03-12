/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - farmarbook
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmarbook` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `farmarbook`;

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ptype` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `quan` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `tc` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `customer` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `date` DATE,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

 
/*Data for the table `cart` */


insert into `cart`(`id`,`ptype`,`name`,`quan`,`price`,`tc`,`image`,`owner`,`customer`,`address`,`date`) values (1,'Farming Vehicles','tractor','2','1500','3000','abc.jpg','raj','chotu','kphb','2025-04-02');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`id`,`username`,`password`,`email`,`mobile`,`address`) values (1,'chotu','chotu','moulalicce225@gmail.com','8639966858','hyd');

/*Table structure for table `ml` */

DROP TABLE IF EXISTS `ml`;

CREATE TABLE `ml` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ml` */

insert  into `ml`(`username`,`password`) values ('ml','ml');

/*Table structure for table `owner` */

DROP TABLE IF EXISTS `owner`;

CREATE TABLE `owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`id`,`username`,`password`,`email`,`mobile`,`address`) values (1,'raj','raj','raj@gmail.com','8639966858','hyd');

/*Table structure for table `purchase` */

DROP TABLE IF EXISTS `purchase`;

CREATE TABLE `purchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ptype` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `quan` varchar(100) DEFAULT NULL,
  `tc` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `customer` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `status1` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `purchase` */

insert  into `purchase`(`id`,`ptype`,`name`,`quan`,`tc`,`image`,`owner`,`customer`,`address`,`rating`,`status`,`status1`) values (1,'Farming Vehicles','tractor','2','3000','abc.jpg','raj','chotu','kphb','good','accepted','positive');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ptype` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
`image` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`id`,`ptype`,`name`,`quantity`,`price`,`image`,`time`,`address`,`owner`) values (1,'Farming Vehicles','tractor','13','1500','abc.jpg','9am to 9pm','hyd','raj');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;	