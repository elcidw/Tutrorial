/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: department
# ------------------------------------------------------------

DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `parent_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKmgsnnmudxrwqidn4f64q8rp4o` (`parent_id`),
  CONSTRAINT `FKmgsnnmudxrwqidn4f64q8rp4o` FOREIGN KEY (`parent_id`) REFERENCES `department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: hibernate_sequence
# ------------------------------------------------------------

DROP TABLE IF EXISTS `hibernate_sequence`;
CREATE TABLE `hibernate_sequence` (
  `next_val` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: privilege
# ------------------------------------------------------------

DROP TABLE IF EXISTS `privilege`;
CREATE TABLE `privilege` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `parent_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKahyelx161ukoxm5ont8yfsbgu` (`parent_id`),
  CONSTRAINT `FKahyelx161ukoxm5ont8yfsbgu` FOREIGN KEY (`parent_id`) REFERENCES `privilege` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: role
# ------------------------------------------------------------

DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: role_privileges
# ------------------------------------------------------------

DROP TABLE IF EXISTS `role_privileges`;
CREATE TABLE `role_privileges` (
  `roles_id` bigint NOT NULL,
  `privileges_id` bigint NOT NULL,
  PRIMARY KEY (`roles_id`,`privileges_id`),
  KEY `FKas5s9i1itvr8tgocse4xmtwox` (`privileges_id`),
  CONSTRAINT `FK9n2w8s3aw0yk00s4nmqvucw6b` FOREIGN KEY (`roles_id`) REFERENCES `role` (`id`),
  CONSTRAINT `FKas5s9i1itvr8tgocse4xmtwox` FOREIGN KEY (`privileges_id`) REFERENCES `privilege` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `department_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKgkh2fko1e4ydv1y6vtrwdc6my` (`department_id`),
  CONSTRAINT `FKgkh2fko1e4ydv1y6vtrwdc6my` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: user_roles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_roles`;
CREATE TABLE `user_roles` (
  `users_id` bigint NOT NULL,
  `roles_id` bigint NOT NULL,
  PRIMARY KEY (`users_id`,`roles_id`),
  KEY `FKj9553ass9uctjrmh0gkqsmv0d` (`roles_id`),
  CONSTRAINT `FK7ecyobaa59vxkxckg6t355l86` FOREIGN KEY (`users_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FKj9553ass9uctjrmh0gkqsmv0d` FOREIGN KEY (`roles_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: department
# ------------------------------------------------------------

INSERT INTO
  `department` (`id`, `description`, `name`, `parent_id`)
VALUES
  (8, '', '采办部', NULL);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: hibernate_sequence
# ------------------------------------------------------------

INSERT INTO
  `hibernate_sequence` (`next_val`)
VALUES
  (4);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: privilege
# ------------------------------------------------------------

INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (1, '系统管理', NULL, NULL);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (2, '岗位管理', '/Role/dblist', 1);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (3, '部门管理', '/Department/dblist', 1);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (4, '用户管理', '/User/dblist', 1);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (5, '岗位列表', '/Role/role_list', 2);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (6, '岗位删除', '/Role/role_delete', 2);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (7, '岗位添加', '/Role/role_add', 2);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (8, '岗位修改', '/Role/role_edit', 2);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (9, '部门列表', '/Department/department_list', 3);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (10, '部门删除', '/Department/department_delete', 3);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (11, '部门添加', '/Department/department_add', 3);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (12, '部门修改', '/Department/department_edit', 3);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (13, '用户列表', '/User/user_list', 4);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (14, '用户删除', '/User/user_delete', 4);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (15, '用户添加', '/User/user_add', 4);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (16, '用户修改', '/User/user_edit', 4);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (17, '网上交流', NULL, NULL);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (18, '论坛管理', '/forumManage', 17);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (19, '论坛', '/forum_list', 17);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (20, '审批流程', NULL, NULL);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (21, '审批流程管理', '/Role/dblist', 20);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (22, '申请模板管理', '/Department/dblist', 20);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (23, '起草申请', '/User/dblist', 20);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (24, '待我审批', '/User/dblist', 20);
INSERT INTO
  `privilege` (`id`, `name`, `url`, `parent_id`)
VALUES
  (25, '我的申请查询', '/User/dblist', 20);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: role
# ------------------------------------------------------------

INSERT INTO
  `role` (`id`, `description`, `name`)
VALUES
  (8, '', 'Manager');
INSERT INTO
  `role` (`id`, `description`, `name`)
VALUES
  (9, '123', 'Contractor');
INSERT INTO
  `role` (`id`, `description`, `name`)
VALUES
  (11, 'administrator\r\n', 'Admin');

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: role_privileges
# ------------------------------------------------------------

INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 1);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (9, 1);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 1);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 2);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 2);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 3);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 3);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 4);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (9, 4);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 4);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 5);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 5);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 6);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 6);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 7);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 7);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 8);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 8);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 9);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 9);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 10);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 10);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 11);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 11);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 12);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 12);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 13);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 13);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 14);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 15);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 15);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 16);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 16);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 17);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 18);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 19);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 20);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 20);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 21);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 22);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 23);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (8, 24);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 24);
INSERT INTO
  `role_privileges` (`roles_id`, `privileges_id`)
VALUES
  (11, 25);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: user
# ------------------------------------------------------------

INSERT INTO
  `user` (
    `id`,
    `email`,
    `name`,
    `description`,
    `gender`,
    `password`,
    `phone_number`,
    `username`,
    `department_id`
  )
VALUES
  (
    17,
    '',
    'user1',
    '',
    'male',
    '$2a$10$HcS8yM4rpFUR90Glw/JFAOxO.q8gtU/xoSO4MBm5qjqsIfNcwLVWO',
    '1234567',
    'admin',
    NULL
  );
INSERT INTO
  `user` (
    `id`,
    `email`,
    `name`,
    `description`,
    `gender`,
    `password`,
    `phone_number`,
    `username`,
    `department_id`
  )
VALUES
  (
    18,
    '',
    'admin',
    '',
    NULL,
    '$2a$10$VwkO/HtfTg.Dvjicar4d4umlHxyj86l//KBbunLbz6eDDKFL/Gjqm',
    '',
    'user1',
    NULL
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: user_roles
# ------------------------------------------------------------

INSERT INTO
  `user_roles` (`users_id`, `roles_id`)
VALUES
  (18, 8);
INSERT INTO
  `user_roles` (`users_id`, `roles_id`)
VALUES
  (17, 11);

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
