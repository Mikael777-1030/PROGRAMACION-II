class JuegoAdivinaNumero extends Juego {
    protected int numeroAdivinar;

    public JuegoAdivinaNumero(int vidas, int numeroAdivinar) {
        super(vidas);
        this.numeroAdivinar = numeroAdivinar;
    }

    public void juego() {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        while (numeroDeVidas > 0) {
            System.out.print("Adivina el número (0 al 10): ");
            int intento = sc.nextInt();
            if (validaNumero(intento)) {
                if (intento == numeroAdivinar) {
                    System.out.println("¡Acertaste!");
                    actualizaRecord();
                    break;
                } else {
                    System.out.println("Fallaste.");
                    quitaVida();
                }
            } else {
                System.out.println("Número fuera de rango.");
            }
        }

        if (numeroDeVidas == 0) {
            System.out.println("Te quedaste sin vidas.");
        }
    }
}

