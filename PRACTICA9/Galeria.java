public class Galeria extends Boleto {
    private int diasAnticipacion;

    public Galeria(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
        calcularPrecio();
    }

    @Override
    public void calcularPrecio() {
        if (diasAnticipacion >= 10) {
            precio = 25.0;
        } else {
            precio = 30.0;
        }
    }
}
