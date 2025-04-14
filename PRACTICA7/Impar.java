class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    public JuegoAdivinaImpar(int vidas, int numeroAdivinar) {
        super(vidas, numeroAdivinar);
    }

    @Override
    public boolean validaNumero(int numero) {
        if (numero % 2 != 0 && numero >= 0 && numero <= 10) {
            return true;
        }
        System.out.println("El número no es impar o está fuera de rango.");
        return false;
    }
}