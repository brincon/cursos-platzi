import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMateral;
    

    public UberVan(String license, Account driver, Map<String, Map<String,Integer>> typeCarAccepted, ArrayList<String> seatsMateral) {
        // super hace referencia a los atributos de la clase padre
        super(license, driver);
        // this hace referencia a los atributos de la clase hija
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMateral = seatsMateral;
    }

    public UberVan(String license, Account driver) {
        // super hace referencia a los atributos de la clase padre
        super(license, driver);

    }

    @Override
    public void setPassenger(Integer passenger) {
        // TODO Auto-generated method stub
        //super.setPassenger(passenger);
        if(passenger == 6){
            this.passegenger = passenger;
        } else {
            System.out.println("Necesitas asignar 6 pasajeros");
        }
    }

}