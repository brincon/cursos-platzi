class Efectivo extends Payment {
    Integer id;
    Integer number;
    Integer cvv;
    String date;

    public Efectivo (Integer id, Integer number){
        this.id = id;
        this.number = number;
    }
} 