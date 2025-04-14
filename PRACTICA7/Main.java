public class Main {
    public static void main(String[] args) {
        JuegoAdivinaNumero juego1 = new JuegoAdivinaNumero(3, 5);
        JuegoAdivinaPar juego2 = new JuegoAdivinaPar(3, 4);
        JuegoAdivinaImpar juego3 = new JuegoAdivinaImpar(3, 7);

        juego1.juego();
        juego2.juego();
        juego3.juego();
    }
}