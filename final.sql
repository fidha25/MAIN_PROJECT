/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - privacy_db
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`privacy_db` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `privacy_db`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `reply` varchar(100) DEFAULT NULL,
  `complaint` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `staff_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`reply`,`complaint`,`date`,`status`,`staff_id`) values 
(1,'ok\r\n','jgvg','ghjg','gvh','2'),
(2,'pending','csnbuihznma','2024-02-24','pending','7'),
(3,'pending','skjhabsniuwdhdj','2024-02-24','pending','7'),
(4,'pending','ksjhds','2024-02-24','pending','4'),
(5,'pending','asschsnxj','2024-02-24','pending','4'),
(6,'pending','jscnjkncj','2024-02-24','pending','6'),
(7,'pending','hsznxjhsjnxlk','2024-02-24','pending','6'),
(8,'pending','skjdhasjkndsj\r\n','2024-02-24','pending','5');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dpt_id` int(11) NOT NULL AUTO_INCREMENT,
  `dpt_name` varchar(100) DEFAULT NULL,
  `contact_no` int(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`dpt_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`dpt_id`,`dpt_name`,`contact_no`,`email`) values 
(1,'cs',657776,'rewes@gmail.com'),
(2,'cf',5447848,'rewes@gmail.com'),
(3,'pwd',346789965,'rewes@gmail.com');

/*Table structure for table `file` */

DROP TABLE IF EXISTS `file`;

CREATE TABLE `file` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `file` */

insert  into `file`(`file_id`,`file`,`title`,`description`) values 
(16,'static/3e50584f-036e-41e9-9a44-892c4d53cda0run code.png','yf','hgcg'),
(15,'static/3d6e00c8-88aa-49ed-bf83-eb0b3125b764run code.png','yf','hgcg'),
(14,'static/5847babe-2c6c-4849-ae79-21425d026d6erun code.png','yf','hgcg'),
(13,'static/1cd1d43b-df92-44d1-b34c-712e8aa4082cHealthID-51-4743-5655-5164.png','helo','helo'),
(12,'static/b2d90c04-bddc-47d7-93fb-89b6ed864d03HealthID-51-4743-5655-5164.png','helo','helo'),
(11,'static/28aa55bf-fb5f-43d1-b39f-56fe69e64f99HealthID-51-4743-5655-5164.png','helo','helo'),
(17,'static/83987a8b-4b94-4c06-9fd8-66c27a2f49acstaff5.jpg','sh','jhu'),
(18,'static/0cdcc64f-342a-4a16-a743-046cfd569ff7staff5.jpg','sh','jhu');

/*Table structure for table `image_upload` */

DROP TABLE IF EXISTS `image_upload`;

CREATE TABLE `image_upload` (
  `upload_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `partion_1` varchar(500) DEFAULT NULL,
  `partion_2` varchar(500) DEFAULT NULL,
  `partion_3` varchar(500) DEFAULT NULL,
  `partion_4` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`upload_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `image_upload` */

insert  into `image_upload`(`upload_id`,`staff_id`,`image`,`partion_1`,`partion_2`,`partion_3`,`partion_4`) values 
(1,5,'/static/Screenshot (2)_20240227-103248.png','/static/Screenshot (2)_face3enc.bmp','/static/Screenshot (2)_face2enc.bmp','/static/Screenshot (2)_face3enc.bmp','/static/Screenshot (2)_face4enc.bmp'),
(2,5,'/static/Screenshot (7)_20240227-103633.png','/static/Screenshot (7)_face1enc.bmp','/static/Screenshot (7)_face2enc.bmp','/static/Screenshot (7)_face3enc.bmp','/static/Screenshot (7)_face4enc.bmp');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'balu7365','123','manager'),
(2,'qq','qq','staff'),
(3,'arunkr','1234','staff'),
(4,'balu7365','1234','staff'),
(5,'balu7365','12345','staff'),
(6,'arunima','11','staff'),
(7,'admin','1','admin'),
(8,'mn','mn','manager');

/*Table structure for table `manager` */

DROP TABLE IF EXISTS `manager`;

CREATE TABLE `manager` (
  `manager_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(100) DEFAULT NULL,
  PRIMARY KEY (`manager_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `manager` */

insert  into `manager`(`manager_id`,`staff_id`) values 
(1,4),
(2,6);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `description` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`title`,`date`,`time`,`description`) values 
(1,'uyfuyf','2024-02-06','09:31','ertyvub'),
(2,'fcgf','2024-05-01','02:30','awtesrfcvghbjnkk'),
(3,'work','2024-02-08','10:04','sesdhgtyrtfgfghf'),
(4,'fdmk','2024-02-28','10:07','iojoij');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `contact_no` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`first_name`,`last_name`,`contact_no`,`place`,`gender`,`image`) values 
(4,1,'balu','krishna','657776','pala','Male','static/b953e13a-ae35-4af0-865a-976f3e134ce6run code.png'),
(5,2,'arunima','kr','87646895','thrissur','Male','static/e6b0c48d-50db-46b8-ac33-efb5c7af4a15run code.png'),
(6,8,'arun','kr','657776','thrissur','Male','static/e748ed6b-8454-403f-84e1-c41dddf60fe3run code.png');

/*Table structure for table `task` */

DROP TABLE IF EXISTS `task`;

CREATE TABLE `task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task` varchar(500) DEFAULT NULL,
  `manager_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `task` */

insert  into `task`(`task_id`,`task`,`manager_id`) values 
(1,'oudjnc',6),
(2,'ksuhiusdh',6);

/*Table structure for table `task_assign` */

DROP TABLE IF EXISTS `task_assign`;

CREATE TABLE `task_assign` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `report` varchar(1000) DEFAULT NULL,
  `task_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `task_assign` */

insert  into `task_assign`(`assign_id`,`staff_id`,`date`,`report`,`task_id`) values 
(1,5,'2024-02-24','static/work_report603e37a8-20e1-4188-8398-3c55939c59bawork_reportc30e2072-0870-4785-aba6-6ad4f7953538BUSINESS INTELLIGENCE.pptx',1),
(2,5,'2024-02-27','pending',1),
(3,4,'2024-02-27','pending',2);

/*Table structure for table `upload_file` */

DROP TABLE IF EXISTS `upload_file`;

CREATE TABLE `upload_file` (
  `up_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`up_file_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `upload_file` */

insert  into `upload_file`(`up_file_id`,`file`,`title`,`description`) values 
(1,'arun','balu','uutildygljpyrytoy'),
(2,'456','dfygu65t7i','8908764'),
(3,'static/e4d0d3ec-b5e0-4ba2-8696-e6e6b7dbe1d2Ashakr.pptx','sckmsac','snsn'),
(4,'static/cf8f141b-0681-41c5-ae13-e70c3bddc992Ashakr.pptx','sckmsac','snsn'),
(5,'static/6d92d162-9eb0-41ad-b722-cd57fb2977ddAshakr.pptx','sckmsac','snsn'),
(6,'static/152eb3d4-8506-413b-8422-57d5402e147cAshakr.pptx','sckmsac','snsn'),
(7,'static/39c0c0fc-12d1-4254-bf50-4c23d9af660dstaff4.jpg','jdjj','uhiu');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(100) DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  `date` varchar(101) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`work_id`,`staff_id`,`report`,`date`) values 
(2,4,'dfjadfmaoidjfe','2024-02-24'),
(3,4,'dfjadfmaoidjfe','2024-02-24'),
(4,4,'dfjadfmaoidjfe','2024-02-24'),
(5,6,'ur work','2024-02-24'),
(6,4,'dfjadfmaoidjfe','2024-02-24'),
(7,4,'dfjadfmaoidjfe','2024-02-24'),
(8,4,'dfjadfmaoidjfe','2024-02-24'),
(9,4,'dfjadfmaoidjfe','2024-02-24'),
(10,4,'dfjadfmaoidjfe','2024-02-24'),
(13,5,'Today work','2024-02-27'),
(12,5,'arun work','2024-02-24');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
