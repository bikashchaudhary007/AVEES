-- phpMyAdmin SQL Dump
-- version 5.2.2-dev+20231218.fdb7583f7c
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 24, 2023 at 05:55 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aveesdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `regvehicle`
--

CREATE TABLE `regvehicle` (
  `Vehicle_id` int(11) NOT NULL,
  `Tag_id` varchar(50) DEFAULT NULL,
  `VehicleName` varchar(50) DEFAULT NULL,
  `VehicleNo` varchar(50) DEFAULT NULL,
  `VehicleOwner` varchar(50) DEFAULT NULL,
  `OwnerContact` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `regvehicle`
--

INSERT INTO `regvehicle` (`Vehicle_id`, `Tag_id`, `VehicleName`, `VehicleNo`, `VehicleOwner`, `OwnerContact`) VALUES
(1, 'A3377FA7', 'Tata EV', '5647', 'Bikash Chaudhary', '9812264188');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `username`, `pwd`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `vehicledetails`
--

CREATE TABLE `vehicledetails` (
  `Id` int(11) NOT NULL,
  `Tag_id` varchar(50) DEFAULT NULL,
  `Entry_Time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicledetails`
--

INSERT INTO `vehicledetails` (`Id`, `Tag_id`, `Entry_Time`) VALUES
(1, 'A3377FA7', '2023-12-05 18:25:05'),
(2, 'A3377FA7', '2023-12-05 18:25:07'),
(3, 'A3377FA7', '2023-12-05 18:25:09'),
(4, 'A3377FA7', '2023-12-05 18:25:17'),
(5, 'A3377FA7', '2023-12-05 19:31:33'),
(6, 'A3377FA7', '2023-12-05 19:31:35'),
(7, 'A3377FA7', '2023-12-05 19:31:39'),
(8, 'A3377FA7', '2023-12-05 19:31:51'),
(9, 'A3377FA7', '2023-12-05 19:33:02'),
(10, 'A3377FA7', '2023-12-05 19:33:10'),
(11, 'A3377FA7', '2023-12-05 19:34:25'),
(12, 'A3377FA7', '2023-12-05 20:29:06'),
(13, 'A3377FA7', '2023-12-05 20:29:09'),
(14, 'A3377FA7', '2023-12-05 20:29:11'),
(15, 'A3377FA7', '2023-12-05 20:29:19'),
(16, 'A3377FA7', '2023-12-05 20:29:21'),
(17, 'A3377FA7', '2023-12-05 20:33:10'),
(18, 'A3377FA7', '2023-12-05 20:33:12'),
(19, 'A3377FA7', '2023-12-05 20:33:40'),
(20, 'A3377FA7', '2023-12-05 20:33:45'),
(21, 'A3377FA7', '2023-12-05 20:34:08'),
(22, 'A3377FA7', '2023-12-05 20:34:10'),
(23, 'A3377FA7', '2023-12-05 20:34:16'),
(24, 'A3377FA7', '2023-12-05 20:35:35'),
(25, 'A3377FA7', '2023-12-05 20:42:53'),
(26, 'A3377FA7', '2023-12-05 20:42:55'),
(27, 'A3377FA7', '2023-12-05 20:43:09'),
(28, 'A3377FA7', '2023-12-05 20:43:11'),
(29, 'A3377FA7', '2023-12-05 20:43:46'),
(30, 'A3377FA7', '2023-12-05 20:44:00'),
(31, 'A3377FA7', '2023-12-05 20:44:56'),
(32, 'A3377FA7', '2023-12-05 20:45:09'),
(33, 'A3377FA7', '2023-12-06 02:33:04'),
(34, 'A3377FA7', '2023-12-06 02:33:06'),
(35, 'A3377FA7', '2023-12-06 02:33:31'),
(36, 'A3377FA7', '2023-12-06 02:33:37'),
(37, 'A3377FA7', '2023-12-06 02:33:41'),
(38, 'A3377FA7', '2023-12-06 02:34:00'),
(39, 'A3377FA7', '2023-12-06 02:34:12'),
(40, 'A3377FA7', '2023-12-20 01:23:05'),
(41, 'A3377FA7', '2023-12-20 01:23:20'),
(42, 'A3377FA7', '2023-12-20 01:46:46'),
(43, 'A3377FA7', '2023-12-20 01:47:03'),
(44, 'A3377FA7', '2023-12-20 01:47:18'),
(45, 'A3377FA7', '2023-12-20 01:47:22'),
(46, 'A3377FA7', '2023-12-20 01:47:46'),
(47, 'A3377FA7', '2023-12-20 01:48:00'),
(48, 'A3377FA7', '2023-12-20 01:48:44'),
(49, 'A3377FA7', '2023-12-20 01:48:47'),
(50, 'A3377FA7', '2023-12-20 01:48:52'),
(51, 'A3377FA7', '2023-12-20 01:50:50'),
(52, 'A3377FA7', '2023-12-20 01:50:55'),
(53, 'A3377FA7', '2023-12-20 01:51:57'),
(54, 'A3377FA7', '2023-12-20 01:52:01'),
(55, 'A3377FA7', '2023-12-20 02:00:02'),
(56, 'A3377FA7', '2023-12-20 02:01:36'),
(57, 'A3377FA7', '2023-12-20 02:02:29'),
(58, 'A3377FA7', '2023-12-20 02:04:42'),
(59, 'A3377FA7', '2023-12-20 02:07:52'),
(60, 'A3377FA7', '2023-12-20 02:15:57'),
(61, 'A3377FA7', '2023-12-20 02:18:48'),
(62, 'A3377FA7', '2023-12-20 02:19:03'),
(63, 'A3377FA7', '2023-12-20 02:21:27'),
(64, 'A3377FA7', '2023-12-20 02:22:18'),
(65, 'A3377FA7', '2023-12-20 02:25:44'),
(66, 'A3377FA7', '2023-12-20 02:26:31'),
(67, 'A3377FA7', '2023-12-21 16:48:44'),
(68, 'A3377FA7', '2023-12-21 16:48:46'),
(69, 'A3377FA7', '2023-12-21 16:48:48'),
(70, 'A3377FA7', '2023-12-21 16:48:50'),
(71, 'A3377FA7', '2023-12-21 16:48:53'),
(72, 'A3377FA7', '2023-12-21 16:48:56'),
(73, 'A3377FA7', '2023-12-21 16:49:38'),
(74, 'A3377FA7', '2023-12-21 16:49:42'),
(75, 'A3377FA7', '2023-12-21 16:50:20'),
(76, 'A3377FA7', '2023-12-21 16:51:41'),
(77, 'A3377FA7', '2023-12-21 16:51:48'),
(78, 'A3377FA7', '2023-12-21 16:52:03'),
(79, 'A3377FA7', '2023-12-22 16:16:36'),
(80, 'A3377FA7', '2023-12-22 16:18:11'),
(81, 'A3377FA7', '2023-12-22 16:18:15'),
(82, 'A3377FA7', '2023-12-22 16:22:07'),
(83, 'A3377FA7', '2023-12-22 16:26:13'),
(84, 'A3377FA7', '2023-12-22 16:26:18'),
(85, 'A3377FA7', '2023-12-24 00:57:48'),
(86, 'A3377FA7', '2023-12-24 00:57:59'),
(87, 'A3377FA7', '2023-12-24 01:08:34'),
(88, 'A3377FA7', '2023-12-24 01:10:42'),
(89, 'A3377FA7', '2023-12-24 01:11:36'),
(90, 'A3377FA7', '2023-12-24 01:12:11'),
(91, 'A3377FA7', '2023-12-24 01:15:10'),
(92, 'A3377FA7', '2023-12-24 01:16:15'),
(93, 'A3377FA7', '2023-12-24 01:16:45'),
(95, 'A3377FA7', '2023-12-24 01:25:30'),
(96, 'A3377FA7', '2023-12-24 01:27:48'),
(97, 'A3377FA7', '2023-12-24 01:28:25'),
(98, 'A3377FA7', '2023-12-24 01:31:06'),
(99, 'A3377FA7', '2023-12-24 01:31:22'),
(100, 'A3377FA7', '2023-12-24 01:33:56'),
(101, 'A3377FA7', '2023-12-24 01:34:08'),
(102, 'A3377FA7', '2023-12-24 01:36:00'),
(103, 'A3377FA7', '2023-12-24 01:54:51'),
(104, 'A3377FA7', '2023-12-24 01:55:01'),
(105, 'A3377FA7', '2023-12-24 02:36:23'),
(106, 'A3377FA7', '2023-12-24 02:36:26'),
(107, 'A3377FA7', '2023-12-24 02:52:45'),
(108, 'A3377FA7', '2023-12-24 02:53:32'),
(109, 'A3377FA7', '2023-12-24 02:54:44'),
(110, 'A3377FA7', '2023-12-24 02:54:46');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `regvehicle`
--
ALTER TABLE `regvehicle`
  ADD PRIMARY KEY (`Vehicle_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `vehicledetails`
--
ALTER TABLE `vehicledetails`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `regvehicle`
--
ALTER TABLE `regvehicle`
  MODIFY `Vehicle_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vehicledetails`
--
ALTER TABLE `vehicledetails`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
