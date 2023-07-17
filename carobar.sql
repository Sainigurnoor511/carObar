-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2023 at 06:00 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carobar`
--

-- --------------------------------------------------------

--
-- Table structure for table `new_cars`
--

CREATE TABLE `new_cars` (
  `id` int(10) NOT NULL,
  `name` varchar(500) NOT NULL,
  `vehicle_type` varchar(500) NOT NULL,
  `engine_type` varchar(500) NOT NULL,
  `mileage` varchar(500) NOT NULL,
  `price` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `new_cars`
--

INSERT INTO `new_cars` (`id`, `name`, `vehicle_type`, `engine_type`, `mileage`, `price`) VALUES
(1, 'Honda Amaze', 'Sedan', 'DOHC i-VTEC + VTC (1199 cc)', '18.4 (km/l)', 'Rs. 7,50,000'),
(2, 'Hyundai Aura', 'Sedan', 'DOHC i-VTEC + VTC (1199 cc)', '18.4 (km/l)', 'Rs. 7,50,000'),
(3, 'Renault Kiger', 'SUV', 'DOHC i-VTEC + VTC (1199 cc)', '18.4 (km/l)', 'Rs. 11,50,000'),
(4, 'Toyota Glanza', 'SUV', 'DOHC i-VTEC + VTC (1199 cc)', '18.4 (km/l)', 'Rs. 11,50,000'),
(5, 'Maruti Dzire', 'Sedan', 'DOHC i-VTEC + VTC (1190 cc)', '18.4 (km/l)', 'Rs. 6,50,000');

-- --------------------------------------------------------

--
-- Table structure for table `used_cars`
--

CREATE TABLE `used_cars` (
  `id` int(10) NOT NULL,
  `name` varchar(500) NOT NULL,
  `vehicle_type` varchar(500) NOT NULL,
  `engine_type` varchar(500) NOT NULL,
  `mileage` varchar(500) NOT NULL,
  `price` varchar(500) NOT NULL,
  `kms_driven` varchar(500) NOT NULL,
  `ownership` varchar(500) NOT NULL,
  `rto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `used_cars`
--

INSERT INTO `used_cars` (`id`, `name`, `vehicle_type`, `engine_type`, `mileage`, `price`, `kms_driven`, `ownership`, `rto`) VALUES
(1, 'Maruti Alto 800', 'Hatchback', 'F8D Petrol Engine', '31.59 km/l', 'Rs. 3,14,000 ', '30,000 Kms', 'First Owner', 'KA03'),
(2, 'Hyunadai Verna', 'Sedan', 'F8D Petrol Engine', '31.59 km/l', 'Rs. 3,14,000 ', '4,000 Kms', 'Second Owner', 'PB07'),
(3, 'Hyunadai Verna', 'Sedan', 'F8D Petrol Engine', '31.59 km/l', 'Rs. 3,14,000 ', '4,000 Kms', 'Second Owner', 'PB07'),
(4, 'Hyunadai Verna', 'Sedan', 'F8D Petrol Engine', '31.59 km/l', 'Rs. 3,14,000 ', '4,000 Kms', 'Second Owner', 'PB07'),
(5, 'Maruti Alto 800', 'Hatchback', 'F8D Petrol Engine', '31.59 km/l', 'Rs. 3,14,000 ', '30,000 Kms', 'First Owner', 'KA03');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `new_cars`
--
ALTER TABLE `new_cars`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `used_cars`
--
ALTER TABLE `used_cars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `new_cars`
--
ALTER TABLE `new_cars`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `used_cars`
--
ALTER TABLE `used_cars`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
