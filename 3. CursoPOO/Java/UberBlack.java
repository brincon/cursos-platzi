import java.util.ArrayList;

class UberBlack extends Car {
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMateral;

    public UberBlack(String license, Account driver, Map<String, Map<String,Integer>> typeCarAccepted, ArrayList<String> seatsMateral) {
        // super hace referencia a los atributos de la clase padre
        super(license, driver);
        // this hace referencia a los atributos de la clase hija
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMateral = seatsMateral;
    

    }

}
