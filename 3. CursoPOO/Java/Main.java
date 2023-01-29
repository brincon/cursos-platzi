class Main{
    
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123"), "Chevrolet", "123");
        //uberX.passengenger = 3;
        uberX.setPassenger(3);
        uberX.printDataCar();

        /*Car car2 = new Car("QWE567", new Account("Andrea Herrera", "ANDA876"));
        car2.license = "QWE567";
        car2.driver = "Andrea Herrera";
        //car2.passengenger = 3;
        car2.printDataCar()*/

        UberVan uberVan = new UberVan("FGH123", new Account("Andrés Herrera", "AND123"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();
        



    }

    
}