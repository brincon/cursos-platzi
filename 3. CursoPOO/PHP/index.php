<?php

require_once('car.php');
require_once('account.php');

$car = new Car("AW456", new Account("Andres Herrera", "123"));
$car->printDataCar();