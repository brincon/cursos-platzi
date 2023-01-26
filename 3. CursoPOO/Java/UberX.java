class UberX extends Car {
    String brand;
    String model;

    public UberX(String license, Account driver, String brand, String model) {
        // super hace referencia a los atributos de la clase padre
        super(license, driver);
        // this hace referencia a los atributos de la clase hija
        this.brand = brand;
        this.model = model;


    }
    
}
