-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 25, 2023 at 05:58 AM
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
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(10, 'Abhishek.0564', '123@#890'),
(13, 'admin', '789456');

-- --------------------------------------------------------

--
-- Table structure for table `cars_data`
--

CREATE TABLE `cars_data` (
  `id` int(20) NOT NULL,
  `car_type` varchar(20) NOT NULL,
  `car_brand` varchar(20) NOT NULL,
  `car_model` varchar(20) NOT NULL,
  `car_variant` varchar(20) NOT NULL,
  `car_mileage` varchar(20) NOT NULL,
  `car_km_driven` varchar(20) NOT NULL,
  `car_registration_year` varchar(20) NOT NULL,
  `car_ownership` varchar(20) NOT NULL,
  `car_price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cars_data`
--

INSERT INTO `cars_data` (`id`, `car_type`, `car_brand`, `car_model`, `car_variant`, `car_mileage`, `car_km_driven`, `car_registration_year`, `car_ownership`, `car_price`) VALUES
(2, 'used', 'Maruti', 'Dzire', 'Diesel', '17.6 KM/H', '20,000 KM', '2018', '1st Owner', 'Rs. 17,00,000');

-- --------------------------------------------------------

--
-- Table structure for table `car_services`
--

CREATE TABLE `car_services` (
  `id` int(20) NOT NULL,
  `service_type` varchar(20) NOT NULL,
  `service_time` varchar(20) NOT NULL,
  `service_date` varchar(20) NOT NULL,
  `customer_name` varchar(20) NOT NULL,
  `customer_contact` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_services`
--

INSERT INTO `car_services` (`id`, `service_type`, `service_time`, `service_date`, `customer_name`, `customer_contact`) VALUES
(2, ' Repair', '11:00 am - 1:00 pm', '7/4/37', 'hgfhgfghf', '987949764547');

-- --------------------------------------------------------

--
-- Table structure for table `sell_car_data`
--

CREATE TABLE `sell_car_data` (
  `id` int(10) NOT NULL,
  `car_brand` varchar(20) NOT NULL,
  `car_registration_year` varchar(20) NOT NULL,
  `car_model` varchar(20) NOT NULL,
  `car_variant` varchar(20) NOT NULL,
  `car_ownership` varchar(20) NOT NULL,
  `car_km_driven` varchar(30) NOT NULL,
  `seller_name` varchar(20) NOT NULL,
  `seller_contact` varchar(20) NOT NULL,
  `seller_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sell_car_data`
--

INSERT INTO `sell_car_data` (`id`, `car_brand`, `car_registration_year`, `car_model`, `car_variant`, `car_ownership`, `car_km_driven`, `seller_name`, `seller_contact`, `seller_address`) VALUES
(9, 'BMW', '2021', 'x3', 'Petrol', '2nd owner', '50,000 km - 60,000 km', 'Abhishek', '895692', 'Hoshiarpur'),
(11, 'Tata', '2021', 'Nexon', 'Petrol', '1st owner', '10,000 km - 20,000 km', 'Tanjiro', '(012)-345-678', 'Japan'),
(12, 'Honda', '2020', 'civic', 'Petrol', '2nd owner', '40,000 km - 50,000 km', 'Nobita', '9465912389', 'Ludhiana'),
(13, 'Mahindra', '2023', 'scorpio N', 'Diesel', '1st owner', '10,000 km - 20,000 km', 'John', '01125932593', 'Jalandhar'),
(14, 'Mahindra', '2022', 'Thar 4x4', 'Diesel', '1st owner', '10,000 km - 20,000 km', 'Gurnoor Singh Saini', '6495286654', 'Street No. 2, house 28,Hoshiarpur'),
(16, 'sdfsf', '2020', 'sdfdsf', 'Diesel', '3rd owner', '40,000 km - 50,000 km', 'sdfsdf', 'sdfsfsdfsdfsdf', 'sdfsdf'),
(17, 'dfgfdgf', '2019', 'dfgfdg', 'Hybrid', '4th owner', '20,000 km - 30,000 km', 'dfgdfg', 'dfgdfgdf', 'dgfdfgd'),
(18, 'dfdsf', '2022', 'sdfsdf', 'Electric', '2nd owner', '40,000 km - 50,000 km', 'fsdfsd', 'sdfsdfsdf', 'sdfdsf');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cars_data`
--
ALTER TABLE `cars_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_services`
--
ALTER TABLE `car_services`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sell_car_data`
--
ALTER TABLE `sell_car_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `cars_data`
--
ALTER TABLE `cars_data`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `car_services`
--
ALTER TABLE `car_services`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sell_car_data`
--
ALTER TABLE `sell_car_data`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
