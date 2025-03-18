
class Linea {
    private Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public String toString() {
        return "Línea desde " + p1 + " hasta " + p2;
    }

    public void dibujaLinea() {
        System.out.println("Dibujando línea desde " + p1 + " hasta " + p2);
    }
}