<?php
require_once('payment.php');
class Efectivo extends Payment {
    public $id;
    public $number;
    public $cvv;
    public $date;


    public function __construct($id, $number){
        $this->id = $id;
        $this->number = $number;
}

?>