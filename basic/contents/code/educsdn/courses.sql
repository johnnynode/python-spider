/*
 Navicat Premium Data Transfer

 Source Server         : mysql8
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost
 Source Database       : csdndb

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : utf-8

 Date: 10/29/2019 06:45:04 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `courses`
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `pic` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `teacher` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `time` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `price` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `courses`
-- ----------------------------
BEGIN;
INSERT INTO `courses` VALUES ('1', '程序员必备算法课！（揭秘淘宝购物车算法）', 'https://edu.csdn.net/course/detail/11029', 'https://img-bss.csdn.net/20191113112821434.jpg', 'CSDN讲师', '5', '11.80'), ('2', 'Python+OpenCV计算机视觉', 'https://edu.csdn.net/course/detail/10552', 'https://img-bss.csdn.net/20191113105314941.jpg', '李立宗', '57', '0.18'), ('3', '机器学习算法基础', 'https://edu.csdn.net/course/detail/10447', 'https://img-bss.csdn.net/2019111310440930.jpg', '覃秉丰', '83', '1.43'), ('4', '人工智能Python之Matplot基础系列视频课程', 'https://edu.csdn.net/course/detail/6773', 'https://img-bss.csdn.net/20191113100521350.jpg', '陆永剑', '7', '14.14'), ('5', 'YOLOv3目标检测实战：训练自己的数据集', 'https://edu.csdn.net/course/detail/24883', 'https://img-bss.csdn.net/20191113093631895.jpg', '白勇', '23', '2.52'), ('6', '基于海思35xx上nnie加速引擎进行yolov3模型推理', 'https://edu.csdn.net/course/detail/25677', 'https://img-bss.csdn.net/20191128105909191.jpg', '刘山', '18', '4.94'), ('7', '深度学习图像处理之垃圾分类', 'https://edu.csdn.net/course/detail/26295', 'https://img-bss.csdn.net/20191112164541580.jpg', '郭冰洋', '14', '2.79'), ('8', 'YOLOv3目标检测：原理与源码解析', 'https://edu.csdn.net/course/detail/25002', 'https://img-bss.csdn.net/20191112180235673.jpg', '白勇', '31', '2.52'), ('9', 'PyTorch版Mask R-CNN图像实例分割实战：训练自己的数据集', 'https://edu.csdn.net/course/detail/26350', 'https://img-bss.csdn.net/20191128115302932.jpg', '白勇', '19', '4.63'), ('10', 'U-Net图像语义分割实战：训练自己的数据集', 'https://edu.csdn.net/course/detail/25493', 'https://img-bss.csdn.net/20191112173509867.jpg', '白勇', '15', '5.87'), ('11', 'YOLOv3目标检测实战：交通标志识别', 'https://edu.csdn.net/course/detail/24887', 'https://img-bss.csdn.net/20191113093610427.jpg', '白勇', '16', '3.63'), ('12', '一学即懂的计算机视觉', 'https://edu.csdn.net/course/detail/26281', 'https://img-bss.csdn.net/20191112164617189.jpg', '屈桢深', '31', '2.55'), ('13', 'YOLOv3目标检测实战：网络模型改进方法', 'https://edu.csdn.net/course/detail/26159', 'https://img-bss.csdn.net/2019111216504163.jpg', '白勇', '26', '3.00'), ('14', '机器学习实战系列套餐（必备基础+经典算法+案例实战）', 'https://edu.csdn.net/combo/detail/1518', 'https://img-bss.csdn.net/2018121423458970_56781.png?imageMogr2/auto-orient/thumbnail/552x371!/format/png', '唐宇迪', '1088', '0.92'), ('15', '深度学习-Pytorch项目实战－垃圾分类', 'https://edu.csdn.net/course/detail/26983', 'https://img-bss.csdn.net/2019121312441781.jpg', '沈福利', '46', '3.67'), ('16', '基于海思35xx nnie引擎进行经典目标检测算法模型推理', 'https://edu.csdn.net/course/detail/26420', 'https://img-bss.csdn.net/20191128115725495.jpg', '刘山', '32', '2.75'), ('17', '机器学习系列实战套餐（经典算法+案例实战）', 'https://edu.csdn.net/combo/detail/681', 'https://img-bss.csdn.net/201712202321564859.png', '唐宇迪', '528', '1.70'), ('18', '机器学习系列套餐（经典算法+案例实战）', 'https://edu.csdn.net/combo/detail/505', 'https://img-bss.csdn.net/201707261427252845.png', '唐宇迪', '408', '1.47'), ('19', 'python数据分析与机器学习实战【2019新版】', 'https://edu.csdn.net/course/detail/3904', 'https://img-bss.csdn.net/20191112162647416.jpg', '唐宇迪', '207', '1.92'), ('20', 'DeepLabv3+图像语义分割实战：训练自己的数据集', 'https://edu.csdn.net/course/detail/25328', 'https://img-bss.csdn.net/20191112174430896.jpg', '白勇', '15', '5.87'), ('21', 'Google Developer Expert 带你玩转深度学习', 'https://edu.csdn.net/course/detail/26109', 'https://img-bss.csdn.net/20191112164810206.jpg', '彭靖田', '35', '1.69'), ('22', '深度学习原理+项目实战+算法详解+主流框架（套餐）', 'https://edu.csdn.net/combo/detail/1519', 'https://img-bss.csdn.net/201707261409476984.png', '唐宇迪', '862', '1.16'), ('23', 'Python数据分析师-实战系列', 'https://edu.csdn.net/combo/detail/1303', 'https://img-bss.csdn.net/201951623313471_38378.png?imageMogr2/auto-orient/thumbnail/552x371!/format/png', '唐宇迪', '683', '1.31');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
