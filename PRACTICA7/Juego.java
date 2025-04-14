class Juego {
    protected int numeroDeVidas;
    protected int record;

    public Juego(int vidas) {
        this.numeroDeVidas = vidas;
        this.record = 0;
    }

    public void reiniciaPartida() {
        this.numeroDeVidas = 3;
    }

    public void actualizaRecord() {
        this.record++;
    }

    public void quitaVida() {
        this.numeroDeVidas--;
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }
}
