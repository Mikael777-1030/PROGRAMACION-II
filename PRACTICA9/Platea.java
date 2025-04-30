public class Platea extends Boleto {
    private int diasAnticipacion;

    public Platea(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
        calcularPrecio();
    }

    @Override
    public void calcularPrecio() {
        if (diasAnticipacion >= 10) {
            precio = 50.0;
        } else {
            precio = 60.0;
        }
    }
}
