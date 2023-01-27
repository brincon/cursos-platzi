<?php

require_once('car.php');
require_once('account.php');
require_once('UberX.php');
require_once('UberPool.php');

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$uberX->printDataCar();

$uberPool = new UberPool("TYU456", new Account("Andrea Ferran", "AND756"), "Dodge", "Attitude");
$uberPool->printDataCar();

?>