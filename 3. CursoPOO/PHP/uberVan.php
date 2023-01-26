<?php
require_once('car.php');
class UberVan extends Car {
    public $typeCarAccepted;
    public $seatsMateral;

    public function __construct($license, $driver, $typeCarAccepted, $seatsMateral){
        parent::__construct($license, $driver);
        $this->typeCarAccepted = $typeCarAccepted;
        $this->seatsMateral = $seatsMateral;
        
    }
}

?>